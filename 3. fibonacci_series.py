# Write a recursive function to calculate the nth Fibonacci number.
def NFibonacciNumber(n):
    if n == 1 or n == 0:
        return n;
    return NFibonacciNumber(n-1) + NFibonacciNumber(n-2);

print(NFibonacciNumber(7))