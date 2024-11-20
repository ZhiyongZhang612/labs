import time

def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper

@memoize
def recur_fibo(n):
    if n <= 1:
        return n
    return recur_fibo(n - 1) + recur_fibo(n - 2)

# Original recursive Fibonacci
def original_recur_fibo(n):
    if n <= 1:
        return n
    return original_recur_fibo(n - 1) + original_recur_fibo(n - 2)

# Compare execution speeds
n = 35

start = time.time()
print("Original Fibonacci:", original_recur_fibo(n))
print("Original Execution Time:", time.time() - start)

start = time.time()
print("Optimized Fibonacci:", recur_fibo(n))
print("Optimized Execution Time:", time.time() - start)
