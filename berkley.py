# node_id,clock_time_sec,is_faulty
# N1,3600,FALSE
# N2,3605,FALSE
# N3,3598,FALSE
# N4,3610,FALSE
# N5,3900,TRUE
# N6,3602,FALSE



import csv

# Change this filename for the second project
filename = "node_clocks_57.csv"

node_times = []
valid_times = []

# Read node clocks from CSV
with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        node_id = row["node_id"]
        clock = float(row["clock_time_sec"])
        faulty = row["is_faulty"].upper()

        node_times.append((node_id, clock, faulty))

        print(f"Polled {node_id}: {clock} seconds")

        if faulty == "TRUE":
            print(f"Discarding faulty node: {node_id}")
        else:
            valid_times.append((node_id, clock))

# Calculate average time of healthy nodes
total_time = sum(clock for node, clock in valid_times)
average_time = total_time / len(valid_times)

print("\n--- Berkeley Clock Synchronization ---")
print("Average Clock Time:", average_time, "seconds")

# Calculate adjustment for each healthy node
print("\n--- Clock Adjustments ---")

for node_id, clock in valid_times:
    adjustment = average_time - clock

    if adjustment > 0:
        print(f"{node_id}: Add {adjustment} seconds")
    elif adjustment < 0:
        print(f"{node_id}: Subtract {abs(adjustment)} seconds")
    else:
        print(f"{node_id}: No adjustment required")

print("\nClock Synchronization Completed!")



# Polled N1: 3600.0 seconds
# Polled N2: 3605.0 seconds
# Polled N3: 3598.0 seconds
# Polled N4: 3610.0 seconds
# Polled N5: 3900.0 seconds
# Discarding faulty node: N5
# Polled N6: 3602.0 seconds

# --- Berkeley Clock Synchronization ---
# Average Clock Time: 3603.0 seconds

# --- Clock Adjustments ---
# N1: Add 3.0 seconds
# N2: Subtract 2.0 seconds
# N3: Add 5.0 seconds
# N4: Subtract 7.0 seconds
# N6: Add 1.0 seconds

# Clock Synchronization Completed!