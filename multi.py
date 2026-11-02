# task_id,thread_name,burst_ms,priority,status
# T1,Worker_1,200,HIGH,PENDING
# T2,Worker_2,300,MEDIUM,PENDING
# T3,Worker_3,150,HIGH,PENDING
# T4,Worker_4,250,LOW,PENDING
# T5,Worker_5,100,MEDIUM,PENDING


import csv
import threading
import time

# Mutex lock
lock = threading.Lock()

# Shared completed task list
completed_tasks = []

# Worker function
def process_task(task):

    task_id = task["task_id"]
    worker = task["thread_name"]
    burst = int(task["burst_ms"])

    print(f"[THREAD STARTED] {worker} processing {task_id}")

    # Simulate task processing
    time.sleep(burst / 1000)

    # Acquire lock before modifying shared data
    lock.acquire()

    print(f"[LOCK ACQUIRED] {worker}")

    completed_tasks.append(task_id)

    print(f"[TASK COMPLETED] {task_id} by {worker}")

    # Release lock
    lock.release()

    print(f"[LOCK RELEASED] {worker}")


# Read CSV dataset
with open("tasks_12.csv", "r") as file:

    reader = csv.DictReader(file)
    tasks = list(reader)

# Create and start threads
threads = []

for task in tasks:

    t = threading.Thread(
        target=process_task,
        args=(task,)
    )

    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Display final result
print("\n===== FINAL COMPLETED TASKS =====")

for task in completed_tasks:
    print(task)

print("Total completed:", len(completed_tasks))




# [THREAD STARTED] Worker_1 processing T1
# [THREAD STARTED] Worker_2 processing T2
# [THREAD STARTED] Worker_3 processing T3
# [THREAD STARTED] Worker_4 processing T4
# [THREAD STARTED] Worker_5 processing T5

# [LOCK ACQUIRED] Worker_5
# [TASK COMPLETED] T5 by Worker_5
# [LOCK RELEASED] Worker_5

# [LOCK ACQUIRED] Worker_3
# [TASK COMPLETED] T3 by Worker_3
# [LOCK RELEASED] Worker_3

# [LOCK ACQUIRED] Worker_1
# [TASK COMPLETED] T1 by Worker_1
# [LOCK RELEASED] Worker_1

# [LOCK ACQUIRED] Worker_4
# [TASK COMPLETED] T4 by Worker_4
# [LOCK RELEASED] Worker_4

# [LOCK ACQUIRED] Worker_2
# [TASK COMPLETED] T2 by Worker_2
# [LOCK RELEASED] Worker_2

# ===== FINAL COMPLETED TASKS =====
# T5
# T3
# T1
# T4
# T2
# Total completed: 5