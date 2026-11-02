# node_id,next_node_id,is_active,priority_rank
# 1,2,TRUE,85
# 2,3,TRUE,70
# 3,4,TRUE,90
# 4,5,FALSE,60
# 5,1,TRUE,95



import csv

# Read nodes from CSV
with open("ring_nodes_15.csv", "r") as file:
    reader = csv.DictReader(file)
    nodes = list(reader)

# Store active nodes
active_nodes = []

for node in nodes:
    if node["is_active"].upper() == "TRUE":
        active_nodes.append(int(node["node_id"]))

# Sort active nodes by ID
active_nodes.sort()

# Current coordinator
coordinator = 3

print("===== RING ELECTION ALGORITHM =====")

# Detect coordinator failure
if coordinator not in active_nodes:
    print("[FAILURE] Coordinator Node", coordinator, "has failed")
else:
    print("[FAILURE] Simulating failure of Node", coordinator)
    active_nodes.remove(coordinator)

print("\n[DETECTED] Coordinator failure detected")

# Initiate election
initiator = 1

print("\n[ELECTION] Node", initiator, "starts election")

# Circulate election token
token = []

print("\n===== TOKEN CIRCULATION =====")

for node_id in active_nodes:
    token.append(node_id)

    print("[TOKEN] Election message passed to Node", node_id)

# Elect highest ID node
new_leader = max(token)

print("\n===== ELECTION RESULT =====")

print("Election token:", token)
print("New Coordinator: Node", new_leader)

# Broadcast coordinator message
print("\n===== COORDINATOR ANNOUNCEMENT =====")

for node_id in active_nodes:
    if node_id != new_leader:
        print("[COORDINATOR] Node", new_leader,
              "announces itself to Node", node_id)

print("\nElection completed successfully!")



# ===== RING ELECTION ALGORITHM =====

# [FAILURE] Coordinator Node 3 has failed

# [DETECTED] Coordinator failure detected

# [ELECTION] Node 1 starts election

# ===== TOKEN CIRCULATION =====

# [TOKEN] Election message passed to Node 1
# [TOKEN] Election message passed to Node 2
# [TOKEN] Election message passed to Node 5

# ===== ELECTION RESULT =====

# Election token: [1, 2, 5]
# New Coordinator: Node 5

# ===== COORDINATOR ANNOUNCEMENT =====

# [COORDINATOR] Node 5 announces itself to Node 1
# [COORDINATOR] Node 5 announces itself to Node 2

# Election completed successfully!