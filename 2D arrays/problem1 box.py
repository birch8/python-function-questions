# You are to write a program which asks the user for a size.  
# It will then print a box made up of asterisks which is of that size.
size = int(input("Enter size: "))
empty_rows = size - 2
full_row = "*" * size
empty_row = "*" + " "*empty_rows + "*"
print(full_row)
for i in range(empty_rows):
    print(empty_row)
print(full_row)