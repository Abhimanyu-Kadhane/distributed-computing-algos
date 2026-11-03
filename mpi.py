# row_id,col_0,col_1,col_2,col_3
# R0,2,4,1,5
# R1,3,1,2,4
# R2,5,2,3,1
# R3,1,3,4,2



import csv
from concurrent.futures import ThreadPoolExecutor

# Change filename for the second project
filename = "matrix_38.csv"


# Worker function: calculates one output row
def calculate_row(task):
    row_id, row, matrix = task

    print(f"Worker processing row {row_id}")

    result = []

    for other_row in matrix:
        dot_product = sum(a * b for a, b in zip(row, other_row))
        result.append(dot_product)

    print(f"Worker completed row {row_id}: {result}")

    return row_id, result


# Read matrix from CSV
matrix = []

with open(filename, "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        values = [
            int(row["col_0"]),
            int(row["col_1"]),
            int(row["col_2"]),
            int(row["col_3"])
        ]
        matrix.append(values)


print("Original Matrix:")
for row in matrix:
    print(row)


# MASTER: Scatter rows to workers
print("\n--- MASTER: SCATTER ---")

tasks = []

for i, row in enumerate(matrix):
    print(f"Scattering row R{i} to Worker {i + 1}")
    tasks.append((f"R{i}", row, matrix))


# WORKERS: Parallel computation
print("\n--- WORKERS: PARALLEL COMPUTATION ---")

result_matrix = [None] * len(matrix)

with ThreadPoolExecutor(max_workers=4) as executor:
    futures = [
        executor.submit(calculate_row, task)
        for task in tasks
    ]

    for future in futures:
        row_id, result = future.result()
        index = int(row_id[1:])
        result_matrix[index] = result


# MASTER: Gather results
print("\n--- MASTER: GATHER ---")

for i, row in enumerate(result_matrix):
    print(f"Gathered result for R{i}: {row}")


print("\nFinal Matrix Product (A x A transpose):")

for row in result_matrix:
    print(row)

print("\nMPI Scatter-Gather Completed!")


# Original Matrix:
# [2, 4, 1, 5]
# [3, 1, 2, 4]
# [5, 2, 3, 1]
# [1, 3, 4, 2]

# --- MASTER: SCATTER ---
# Scattering row R0 to Worker 1
# Scattering row R1 to Worker 2
# Scattering row R2 to Worker 3
# Scattering row R3 to Worker 4

# --- WORKERS: PARALLEL COMPUTATION ---
# Worker processing row R0
# Worker completed row R0: [46, 32, 26, 28]
# Worker processing row R1
# Worker completed row R1: [32, 30, 27, 22]
# Worker processing row R2
# Worker completed row R2: [26, 27, 39, 25]
# Worker processing row R3
# Worker completed row R3: [28, 22, 25, 30]

# --- MASTER: GATHER ---
# Gathered result for R0: [46, 32, 26, 28]
# Gathered result for R1: [32, 30, 27, 22]
# Gathered result for R2: [26, 27, 39, 25]
# Gathered result for R3: [28, 22, 25, 30]

# Final Matrix Product (A x A transpose):
# [46, 32, 26, 28]
# [32, 30, 27, 22]
# [26, 27, 39, 25]
# [28, 22, 25, 30]

# MPI Scatter-Gather Completed!