
import time
print("1. FINDING MAXIMUM VALUES")
numbers = [23, 45, 12, 67, 89, 34, 56]
# Normal Way - Manual iteration
def find_max_normal(lst):
    if not lst:
        return None
    max_val = lst[0]
    for i in range(1, len(lst)):
        if lst[i] > max_val:
            max_val = lst[i]
    return max_val

# Python Optimal Way - Built-in function
def find_max_optimal(lst):
    return max(lst) if lst else None

# Timing the normal way
start_time = time.time()
result_normal = find_max_normal(numbers)
end_time = time.time()
time_normal = end_time - start_time

# Timing the optimal way
start_time = time.time()
result_optimal = find_max_optimal(numbers)
end_time = time.time()
time_optimal = end_time - start_time

print(f"Normal way result: {result_normal}")
print(f"Normal way time: {time_normal:.8f} seconds")
print(f"Optimal way result: {result_optimal}")
print(f"Optimal way time: {time_optimal:.8f} seconds")
print(f"Speed improvement: {time_normal/time_optimal:.2f}x faster" if time_optimal > 0 else "Speed improvement: N/A")
print()
print("I'm Aziz")