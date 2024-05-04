# Print the following pattern

# * * * *
# * * *
# * *
# *

# def Pattern(row, column = 0):    
#     if row < 1:
#         return
#     if row > column:
#         print("*", end=" ");
#         Pattern(row, column + 1)
#     else:
#         print()
#         Pattern(row - 1, 0)
        
# Pattern(6)  # Just pass the number of rows which should be printed

# ......................................................................
# print the following pattern

# *
# * *
# * * *
# * * * *

# def Pattern(row, column = 0):    
#     if row < 1:
#         return
#     if row > column:
#         Pattern(row, column + 1)
#         print("*", end=" ");
#     else:
#         Pattern(row - 1, 0)
#         print()

Pattern(4)
    