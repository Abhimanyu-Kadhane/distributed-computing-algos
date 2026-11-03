# event_id,process_id,event_type,message_to,initial_clock
# E1,P1,SEND,P2,0
# E2,P2,RECEIVE,P1,0
# E3,P1,LOCAL,-,0
# E4,P2,LOCAL,-,0
# E5,P3,LOCAL,-,0
# E6,P1,SEND,P3,0
# E7,P3,RECEIVE,P1,0


import csv

# Change this filename for the second project
filename = "events_29.csv"

# Store logical clock for each process
clocks = {}

# Store timestamps of sent messages
messages = {}

# Store final event timestamps
event_timestamps = []

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        event = row["event_id"]
        process = row["process_id"]
        event_type = row["event_type"].upper()
        message_to = row["message_to"]
        initial = int(row["initial_clock"])

        # Initialize process clock only once
        if process not in clocks:
            clocks[process] = initial

        if event_type == "SEND":
            clocks[process] += 1

            # Save timestamp for receiver
            messages[(process, message_to)] = clocks[process]

            print(f"\n{event}: {process} sends message to {message_to}")
            print(f"Clock updated: L = {clocks[process]}")

        elif event_type == "RECEIVE":
            # message_to contains the sender's process ID
            sender = message_to
            key = (sender, process)

            if key not in messages:
                print(f"\nERROR: No message from {sender} to {process}")
                continue

            message_time = messages.pop(key)

            old_clock = clocks[process]
            clocks[process] = max(old_clock, message_time) + 1

            print(f"\n{event}: {process} receives message from {sender}")
            print(f"L = max({old_clock}, {message_time}) + 1")
            print(f"Clock updated: L = {clocks[process]}")

        elif event_type == "LOCAL":
            clocks[process] += 1

            print(f"\n{event}: Local event at {process}")
            print(f"Clock updated: L = {clocks[process]}")

        # Save event and its logical timestamp
        event_timestamps.append(
            (event, process, clocks[process])
        )


# Sort events by timestamp.
# Process ID and event ID break ties to produce a total order.
event_timestamps.sort(key=lambda x: (x[2], x[1], x[0]))

print("\n--- FINAL CAUSAL ORDER ---")

for event, process, timestamp in event_timestamps:
    print(f"{event} | {process} | Timestamp: {timestamp}")

print("\nLamport Clock Execution Completed!")



# E1: P1 sends message to P2
# Clock updated: L = 1

# E2: P2 receives message from P1
# L = max(0, 1) + 1
# Clock updated: L = 2

# E3: Local event at P1
# Clock updated: L = 2

# E4: Local event at P2
# Clock updated: L = 3

# E5: Local event at P3
# Clock updated: L = 1

# E6: P1 sends message to P3
# Clock updated: L = 3

# E7: P3 receives message from P1
# L = max(1, 3) + 1
# Clock updated: L = 4

# --- FINAL CAUSAL ORDER ---
# E1 | P1 | Timestamp: 1
# E5 | P3 | Timestamp: 1
# E2 | P2 | Timestamp: 2
# E3 | P1 | Timestamp: 2
# E4 | P2 | Timestamp: 3
# E6 | P1 | Timestamp: 3
# E7 | P3 | Timestamp: 4

# Lamport Clock Execution Completed!