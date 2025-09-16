print("FIBONACCI SEQUENCE GENERATION")
print("-" * 40)

# Normal Way - Recursive approach (inefficient for large numbers)
def fibonacci_recursive(n):
    """Classic recursive Fibonacci - exponential time complexity O(2^n)"""
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Better Normal Way - Iterative approach
def fibonacci_iterative(n):
    """Iterative Fibonacci - linear time complexity O(n)"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for i in range(2, n + 1):
        a, b = b, a + b
    return b

# Python Optimal Way 1 - Using memoization with lru_cache decorator
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_memoized(n):
    """Memoized recursive Fibonacci - cached results for efficiency"""
    if n <= 1:
        return n
    return fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)

# Python Optimal Way 2 - Generator for Fibonacci sequence
def fibonacci_generator(n):
    """Generator that yields Fibonacci numbers up to n"""
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

# Python Optimal Way 3 - List comprehension with generator for first n numbers
def fibonacci_sequence(n):
    """Generate first n Fibonacci numbers using generator"""
    def fib_gen():
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    gen = fib_gen()
    return [next(gen) for _ in range(n)]

# Performance testing with different approaches
print("Computing Fibonacci numbers:")
print()

# Test small numbers
n = 10
print(f"Fibonacci({n}) using different methods:")
print(f"Recursive:     {fibonacci_recursive(n)}")
print(f"Iterative:     {fibonacci_iterative(n)}")
print(f"Memoized:      {fibonacci_memoized(n)}")
print(f"Sequence:      {fibonacci_sequence(n)}")
print()

# Show first 15 numbers using generator
print("First 15 Fibonacci numbers using generator:")
fib_sequence = fibonacci_sequence(15)
print(fib_sequence)
print()

# Show Fibonacci numbers up to 100 using generator
print("Fibonacci numbers up to 100:")
fib_up_to_100 = list(fibonacci_generator(100))
print(fib_up_to_100)
print()

# Performance comparison
import time

def time_function(func, n, description):
    """Helper function to time execution"""
    start = time.time()
    try:
        result = func(n)
        end = time.time()
        execution_time = end - start
        print(f"{description}: {result} (Time: {execution_time:.8f} seconds)")
        return execution_time
    except RecursionError:
        print(f"{description}: RecursionError - too deep!")
        return float('inf')

print("Performance comparison for Fibonacci(20) - safe for recursive:")
n_small = 20

print("\nSmall number test (n=20):")
times_small = {}
times_small['recursive'] = time_function(fibonacci_recursive, n_small, "Recursive   ")
times_small['iterative'] = time_function(fibonacci_iterative, n_small, "Iterative   ")
times_small['memoized'] = time_function(fibonacci_memoized, n_small, "Memoized    ")

# Clear cache for fair comparison
fibonacci_memoized.cache_clear()

print(f"\nPerformance comparison for Fibonacci(35) - larger number:")
n_test = 35

times_large = {}
times_large['iterative'] = time_function(fibonacci_iterative, n_test, "Iterative   ")
times_large['memoized'] = time_function(fibonacci_memoized, n_test, "Memoized    ")
print("Recursive skipped for n=35 (would be too slow)")

# Speed comparison
print(f"\nSpeed comparison for n=20:")
if times_small['recursive'] > 0 and times_small['iterative'] > 0:
    print(f"Iterative is {times_small['recursive']/times_small['iterative']:.1f}x faster than Recursive")
if times_small['recursive'] > 0 and times_small['memoized'] > 0:
    print(f"Memoized is {times_small['recursive']/times_small['memoized']:.1f}x faster than Recursive")

print(f"\nSpeed comparison for n=35:")
if times_large['iterative'] > 0 and times_large['memoized'] > 0:
    ratio = times_large['iterative']/times_large['memoized']
    if ratio > 1:
        print(f"Memoized is {ratio:.1f}x faster than Iterative")
    else:
        print(f"Iterative is {1/ratio:.1f}x faster than Memoized")

# Clear the cache for fair comparison
fibonacci_memoized.cache_clear()

print("\n" + "-" * 60)
print("FIBONACCI ALGORITHM COMPARISON:")
print("• Recursive: O(2^n) - exponential time, very slow")
print("• Iterative: O(n) - linear time, good for most cases")
print("• Memoized: O(n) - cached results, excellent for repeated calls")
print("• Generator: Memory efficient, produces sequence on-demand")
print("-" * 60)
print("")
