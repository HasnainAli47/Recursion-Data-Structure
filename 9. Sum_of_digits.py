# Write a recursive function to calculate the sum of digits of a positive integer.

def SumOfDigits(num):
    if num % 10 == 0:
        return num
    return (num % 10) + SumOfDigits(num // 10)
    # return SumOfDigits(num // 10) + (num % 10) #Will give same result becuase in addition order dosen't matter


num = 1234
print(SumOfDigits(num))

# This will work like
# SumOfDigits(123)
#       3 + SumOfDigits(12)
#                   2 + SumOfDigits(1)
#                               1
# These will be added recursively and will print 6