cluster_config = {
    "cluster_name": "dhaka-prod-east",
    "total_max_slots": 8,
    "active_nodes": ["10.0.1.15", "10.0.1.16", "10.0.1.17", "10.0.1.18", "10.0.1.19"]
}

def calculate_capacity(config):
    # Calculate how many items are in the active_nodes list
    total_active_nodes = len(config["active_nodes"])

    # Run the mathematical formula to find utilization percentage
    utilization = (total_active_nodes / config["total_max_slots"]) * 100

    # Print the status statement
    print(f"Cluster {config['cluster_name']} utilization: {utilization:.2f}% ({total_active_nodes}/{config['total_max_slots']} active)")

calculate_capacity(cluster_config)