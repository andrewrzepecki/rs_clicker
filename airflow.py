import yaml
import asyncio
import networkx as nx
import matplotlib.pyplot as plt
from asyncio.subprocess import create_subprocess_exec

# Function to run a task asynchronously and redirect the output to a log file
async def run_task(task, task_status, G, fig, ax):
    script = task['script']
    params = [f"--{key}={value}" for key, value in task['params'].items()]
    command = ["python", script] + params
    log_file_path = task.get('log_file', f"{task['id']}_output.log")

    print(f"Running command: {' '.join(command)}")
    
    # Mark task as running
    task_status[task['id']] = "running"
    update_graph(G, task_status, fig, ax)
    
    with open(log_file_path, 'w') as log_file:
        # Run the task asynchronously
        process = await create_subprocess_exec(
            *command,
            stdout=log_file,
            stderr=log_file
        )
        await process.communicate()

        if process.returncode == 0:
            task_status[task['id']] = "completed"
        else:
            task_status[task['id']] = "failed"

        # Update graph after task completion
        update_graph(G, task_status, fig, ax)
        print(f"Task {task['id']} finished with status: {task_status[task['id']]}")

# Function to create a DAG and visualize the tasks
def create_dag(tasks):
    G = nx.DiGraph()
    for task in tasks:
        G.add_node(task['id'], label=task['name'])
        for dep in task.get('dependencies', []):
            G.add_edge(dep, task['id'])
    return G

# Function to update the graph visualization
def update_graph(G, task_status, fig, ax):
    ax.clear()
    colors = []

    # Assign colors based on task status
    for node in G.nodes():
        status = task_status.get(node, "pending")
        if status == "completed":
            colors.append("green")
        elif status == "running":
            colors.append("yellow")
        elif status == "failed":
            colors.append("red")
        else:
            colors.append("lightgray")

    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color=colors, ax=ax, node_size=2000, font_size=10, font_color="black")
    plt.draw()
    plt.pause(0.1)

# Function to run the pipeline with live graph updates
async def run_pipeline(config_file):
    with open(config_file, 'r') as f:
        config = yaml.safe_load(f)

    tasks = {task['id']: task for task in config['pipeline']['tasks']}
    task_status = {task_id: "pending" for task_id in tasks}  # Track the status of each task

    # Create a DAG for task dependencies and initialize the plot
    G = create_dag(config['pipeline']['tasks'])
    
    fig, ax = plt.subplots()
    plt.ion()  # Enable interactive mode
    update_graph(G, task_status, fig, ax)

    running_tasks = {}

    async def run_dependent_tasks(task_id):
        task = tasks[task_id]
        dependencies = task.get('dependencies', [])
        
        # Wait for dependencies to complete
        await asyncio.gather(*(running_tasks[dep] for dep in dependencies))
        
        # Run the task and update the status
        running_tasks[task_id] = asyncio.create_task(run_task(task, task_status, G, fig, ax))
        await running_tasks[task_id]

    # Start tasks asynchronously, respecting dependencies
    await asyncio.gather(*[run_dependent_tasks(task_id) for task_id in tasks])

    plt.ioff()
    plt.show()  # Keep the graph open at the end

if __name__ == "__main__":
    asyncio.run(run_pipeline("pipeline_config.yaml"))
