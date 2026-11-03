# event_id,process_id,event_action,target_process
# E1,P1,SEND,P2
# E2,P2,RECEIVE,P1
# E3,P2,LOCAL,-
# E4,P3,LOCAL,-
# E5,P1,LOCAL,-
# E6,P3,RECEIVE,P1



import csv

# Change filename for the second project
filename = "vector_events_6.csv"

processes = ["P1", "P2", "P3"]
index = {"P1": 0, "P2": 1, "P3": 2}

# Initially all vector clocks are zero
clocks = {
    "P1": [0, 0, 0],
    "P2": [0, 0, 0],
    "P3": [0, 0, 0]
}

# Stores sent message clocks
messages = {}
event_vectors = {}

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        event = row["event_id"]
        process = row["process_id"]
        action = row["event_action"].upper()
        target = row["target_process"]

        i = index[process]

        if action == "SEND":
            # Increment sender's clock
            clocks[process][i] += 1

            # Attach vector clock to message
            message_clock = clocks[process].copy()
            messages.setdefault((process, target), []).append(message_clock)

            print(f"\n{event}: {process} sends message to {target}")

        elif action == "RECEIVE":
            # Receive the message and merge clocks
            key = (target, process)

            if key not in messages or not messages[key]:
                print(f"\n{event}: No message available from {target}")
                continue

            received_clock = messages[key].pop(0)

            for j in range(3):
                clocks[process][j] = max(
                    clocks[process][j],
                    received_clock[j]
                )

            # Increment receiver's own clock
            clocks[process][i] += 1

            print(f"\n{event}: {process} receives message from {target}")

        elif action == "LOCAL":
            # Increment local process clock
            clocks[process][i] += 1

            print(f"\n{event}: Local event at {process}")

        # Save event's vector clock
        event_vectors[event] = clocks[process].copy()

        print("Updated vector clock:", clocks[process])


# Compare two vector clocks
def compare(v1, v2):
    less = all(a <= b for a, b in zip(v1, v2))
    greater = all(a >= b for a, b in zip(v1, v2))

    if less and v1 != v2:
        return "CAUSALLY PRECEDING"
    elif greater and v1 != v2:
        return "CAUSALLY FOLLOWING"
    elif v1 == v2:
        return "EQUAL"
    else:
        return "CONCURRENT"


# Display causal relationships between event pairs
print("\n--- EVENT RELATIONSHIPS ---")

events = list(event_vectors.keys())

for i in range(len(events)):
    for j in range(i + 1, len(events)):
        e1 = events[i]
        e2 = events[j]

        v1 = event_vectors[e1]
        v2 = event_vectors[e2]

        result = compare(v1, v2)

        if result == "CAUSALLY PRECEDING":
            print(f"{e1} {v1} < {e2} {v2} : Causally Preceding")
        elif result == "CAUSALLY FOLLOWING":
            print(f"{e2} {v2} < {e1} {v1} : Causally Preceding")
        elif result == "CONCURRENT":
            print(f"{e1} || {e2} : Concurrent")
        else:
            print(f"{e1} and {e2} : Equal")

print("\nVector Clock Execution Completed!")


# E1: P1 sends message to P2
# Updated vector clock: [1, 0, 0]

# E2: P2 receives message from P1
# Updated vector clock: [1, 1, 0]

# E3: Local event at P2
# Updated vector clock: [1, 2, 0]

# E4: Local event at P3
# Updated vector clock: [0, 0, 1]

# E5: P1 sends message to P3
# Updated vector clock: [2, 0, 0]

# E6: P3 receives message from P1
# Updated vector clock: [2, 0, 2]