# Write a recursive function to calculate the sum of all natural numbers up to a given number n.
# def SumOfNumbers(n):
#     if n < 1:
#         return n;
#     return n + SumOfNumbers(n-1)

# print(SumOfNumbers(3))

# ..............................................................................
# We can also do it to start from 1 and go till n
# def SumOfNumbers(n, base = 0):
#     if base >= n:
#         return n;
#     return base + SumOfNumbers(n, base + 1);

# print(SumOfNumbers(3))