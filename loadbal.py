# job_id,compute_units,assigned_worker,status
# J101,35,UNASSIGNED,PENDING
# J102,50,UNASSIGNED,PENDING
# J103,20,UNASSIGNED,PENDING
# J104,45,UNASSIGNED,PENDING
# J105,30,UNASSIGNED,PENDING
# J106,60,UNASSIGNED,PENDING
# J107,25,UNASSIGNED,PENDING
# J108,40,UNASSIGNED,PENDING



import csv

# Worker nodes and their current loads
workers = {
    "Worker_1": 0,
    "Worker_2": 0,
    "Worker_3": 0
}

# Store allocated jobs
worker_jobs = {
    "Worker_1": [],
    "Worker_2": [],
    "Worker_3": []
}

# Read incoming jobs from CSV
with open("workload_13.csv", "r") as file:

    reader = csv.DictReader(file)

    jobs = list(reader)

print("===== LOAD BALANCING STARTED =====")

# Allocate jobs using Least Connections
for job in jobs:

    job_id = job["job_id"]
    compute = int(job["compute_units"])

    # Find worker having minimum load
    selected_worker = min(workers, key=workers.get)

    # Assign job to selected worker
    workers[selected_worker] += compute

    worker_jobs[selected_worker].append(job_id)

    job["assigned_worker"] = selected_worker
    job["status"] = "COMPLETED"

    print("\n[NEW JOB]", job_id)
    print("Compute Units:", compute)
    print("[ALLOCATED TO]", selected_worker)

    print("[CURRENT WORKER LOADS]")
    for worker, load in workers.items():
        print(worker, ":", load)

# Final summary
print("\n===== FINAL LOAD SUMMARY =====")

for worker in workers:

    print("\n", worker)
    print("Total Load:", workers[worker])
    print("Assigned Jobs:", worker_jobs[worker])

print("\n===== ALL JOBS PROCESSED =====")



# ===== LOAD BALANCING STARTED =====

# [NEW JOB] J101
# Compute Units: 35
# [ALLOCATED TO] Worker_1
# [CURRENT WORKER LOADS]
# Worker_1 : 35
# Worker_2 : 0
# Worker_3 : 0

# [NEW JOB] J102
# Compute Units: 50
# [ALLOCATED TO] Worker_2

# [NEW JOB] J103
# Compute Units: 20
# [ALLOCATED TO] Worker_3

# [NEW JOB] J104
# Compute Units: 45
# [ALLOCATED TO] Worker_3

# [NEW JOB] J105
# Compute Units: 30
# [ALLOCATED TO] Worker_1

# [NEW JOB] J106
# Compute Units: 60
# [ALLOCATED TO] Worker_2

# [NEW JOB] J107
# Compute Units: 25
# [ALLOCATED TO] Worker_1

# [NEW JOB] J108
# Compute Units: 40
# [ALLOCATED TO] Worker_3

# ===== FINAL LOAD SUMMARY =====

# Worker_1
# Total Load: 90
# Assigned Jobs: ['J101', 'J105', 'J107']

# Worker_2
# Total Load: 110
# Assigned Jobs: ['J102', 'J106']

# Worker_3
# Total Load: 105
# Assigned Jobs: ['J103', 'J104', 'J108']

# ===== ALL JOBS PROCESSED =====