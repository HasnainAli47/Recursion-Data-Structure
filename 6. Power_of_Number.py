# Write a recursive function to calculate the power of a number. 
# The function should take two parameters, base and exponent, and return base raised to the power of exponent. 
# Exponent should be a positive integer else return -1

def POwerOfNumber(base, exponent):
    if exponent < 0:
        return 0
    if exponent == 0:
        return 1;
    return base * POwerOfNumber(base, exponent-1);

print(POwerOfNumber(2, 2)) # 2 * 2 