# client_id,t0_send_ms,t_server_ms,t1_recv_ms
# C1,1000,1050,1100
# C2,2000,2070,2120
# C3,3000,3040,3100
# C4,4000,4080,4140
# C5,5000,5060,5120



import csv

# Read clock records from CSV
with open("cristian_clocks_40.csv", "r") as file:

    reader = csv.DictReader(file)

    records = list(reader)

print("===== CRISTIAN CLOCK SYNCHRONIZATION =====")

# Process each client
for record in records:

    client = record["client_id"]

    t0 = float(record["t0_send_ms"])
    server_time = float(record["t_server_ms"])
    t1 = float(record["t1_recv_ms"])

    print("\nClient:", client)

    # Calculate Round Trip Time
    rtt = t1 - t0

    print("RTT:", rtt, "ms")

    # Calculate estimated server time
    estimated_time = server_time + (rtt / 2)

    print("Estimated Server Time:", estimated_time, "ms")

    # Calculate client clock offset
    client_offset = estimated_time - t1

    print("Clock Offset:", client_offset, "ms")

    # Adjust client clock
    adjusted_time = t1 + client_offset

    print("Adjusted Client Time:", adjusted_time, "ms")

print("\n===== SYNCHRONIZATION COMPLETED =====")


# ===== CRISTIAN CLOCK SYNCHRONIZATION =====

# Client: C1
# RTT: 100.0 ms
# Estimated Server Time: 1100.0 ms
# Clock Offset: 0.0 ms
# Adjusted Client Time: 1100.0 ms

# Client: C2
# RTT: 120.0 ms
# Estimated Server Time: 2130.0 ms
# Clock Offset: 10.0 ms
# Adjusted Client Time: 2130.0 ms

# Client: C3
# RTT: 100.0 ms
# Estimated Server Time: 3090.0 ms
# Clock Offset: -10.0 ms
# Adjusted Client Time: 3090.0 ms

# Client: C4
# RTT: 140.0 ms
# Estimated Server Time: 4150.0 ms
# Clock Offset: 10.0 ms
# Adjusted Client Time: 4150.0 ms

# Client: C5
# RTT: 120.0 ms
# Estimated Server Time: 5120.0 ms
# Clock Offset: 0.0 ms
# Adjusted Client Time: 5120.0 ms

# ===== SYNCHRONIZATION COMPLETED =====