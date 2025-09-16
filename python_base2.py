import time

print("2. FILTERING AND TRANSFORMING DATA")
print("-" * 40)

students = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 72},
    {"name": "Charlie", "grade": 90},
    {"name": "Diana", "grade": 68},
    {"name": "Eve", "grade": 94},
    {"name": "Frank", "grade": 75},
    {"name": "Grace", "grade": 88},
  
]

# Normal Way - Multiple loops and temporary variables
def get_top_students_normal(students, threshold=80):
    result = []
    for student in students:
        if student["grade"] >= threshold:
            result.append(student["name"].upper())
    return result

# Python Optimal Way - List comprehension
def get_top_students_optimal(students, threshold=80):
    return [student["name"].upper() for student in students if student["grade"] >= threshold]

# Timing the normal way
start_time = time.time()
result_normal = get_top_students_normal(students)
end_time = time.time()
time_normal = end_time - start_time

# Timing the optimal way
start_time = time.time()
result_optimal = get_top_students_optimal(students)
end_time = time.time()
time_optimal = end_time - start_time

print(f"Normal way result: {result_normal}")
print(f"Normal way time: {time_normal:.8f} seconds")
print(f"Optimal way result: {result_optimal}")
print(f"Optimal way time: {time_optimal:.8f} seconds")
print(f"Speed improvement: {time_normal/time_optimal:.2f}x faster" if time_optimal > 0 else "Speed improvement: N/A")
print()