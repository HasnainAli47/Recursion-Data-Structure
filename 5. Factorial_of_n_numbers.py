# Write a recursive function to calculate the factorial of a non-negative integer.
# def Factorial(n):
#     if n <= 1:
#         return n;
#     return n * Factorial(n - 1)

# print(Factorial(5)) # this will calculate 5 * 4 * 3 * 2 * 1 = 120

# ....................................................................
# We can also do the factorial starting form 1 and go till
# def Factorial(n, base=1):
#     if n == base:
#         return n
#     return base * Factorial(n, base+1)

# print(Factorial(5))  # This will calculate 1 * 2 * 3 * 4 * 5 = 120
