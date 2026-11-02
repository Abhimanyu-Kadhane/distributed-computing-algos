# node_id,is_alive,is_current_coordinator
# 1,TRUE,FALSE
# 2,TRUE,FALSE
# 3,TRUE,FALSE
# 4,TRUE,FALSE
# 5,FALSE,TRUE


import csv

# Read nodes from CSV
with open("bully_cluster_26.csv", "r") as file:
    reader = csv.DictReader(file)
    nodes = list(reader)

# Find alive nodes
alive_nodes = []

for node in nodes:
    if node["is_alive"].upper() == "TRUE":
        alive_nodes.append(int(node["node_id"]))

# Find current coordinator
coordinator = None

for node in nodes:
    if node["is_current_coordinator"].upper() == "TRUE":
        coordinator = int(node["node_id"])

print("===== BULLY ALGORITHM =====")

print("Current Coordinator:", coordinator)

# Simulate coordinator failure
if coordinator not in alive_nodes:
    print("\n[FAILURE] Coordinator", coordinator, "has failed")

# Initiator node
initiator = 3

print("\n[INITIATOR] Node", initiator, "starts election")

# Send election messages to higher ID nodes
higher_nodes = []

for node_id in alive_nodes:
    if node_id > initiator:
        higher_nodes.append(node_id)

for node_id in higher_nodes:
    print("[ELECTION] Node", initiator,
          "sends ELECTION to Node", node_id)

    print("[OK] Node", node_id,
          "responds OK to Node", initiator)

# Highest alive node becomes leader
if alive_nodes:
    new_leader = max(alive_nodes)

    print("\n[LEADER ELECTION] Highest alive node:", new_leader)

    # Broadcast coordinator message
    for node_id in alive_nodes:
        if node_id != new_leader:
            print("[COORDINATOR] Node", new_leader,
                  "announces itself to Node", node_id)

    print("\n===== ELECTION COMPLETED =====")
    print("New Coordinator: Node", new_leader)



# ===== BULLY ALGORITHM =====
# Current Coordinator: 5

# [FAILURE] Coordinator 5 has failed

# [INITIATOR] Node 3 starts election

# [ELECTION] Node 3 sends ELECTION to Node 4
# [OK] Node 4 responds OK to Node 3

# [LEADER ELECTION] Highest alive node: 4

# [COORDINATOR] Node 4 announces itself to Node 1
# [COORDINATOR] Node 4 announces itself to Node 2
# [COORDINATOR] Node 4 announces itself to Node 3

# ===== ELECTION COMPLETED =====
# New Coordinator: Node 4