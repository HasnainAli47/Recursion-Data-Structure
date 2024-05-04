# Write a recursive function to reverse a string.

def ReverseString(str):
    if len(str) <= 1:
        return str;
    return str[-1] + ReverseString(str[:-1])

str = "aabb"
print(ReverseString(str))


# This will work like
# ReverseString("abc")
#       c + ReverseString("ab")
#                   b + ReverseString(a)
#                                  a


# And will print like    cba