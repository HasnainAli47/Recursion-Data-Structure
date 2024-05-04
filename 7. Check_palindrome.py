# Write a recursive function to check if a given string is a palindrome or not. 
# A palindrome is a string that reads the same backward as forward.

def CheckPalandrome(str):
    if len(str) <= 1:
        return True
    return str[0] == str[len(str) - 1] and CheckPalandrome(str[1:-1])
    
str = "baab"
if CheckPalandrome(str):
    print("String is palandrome.");
else:
    print("String is not palandrome.");