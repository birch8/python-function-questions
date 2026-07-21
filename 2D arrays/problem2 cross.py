# You are to write a program which asks the user for a size.  
# It will then print a cross made up of asterisks which is of that size.
import math
size = int(input("Enter size: "))
gap = size - 2
for i in range(size-1):
    padding = math.floor((size - abs(gap) -2)/2)
    print(f"{' ' * padding}*{' ' * abs(gap)}*{' ' * padding}")
    if gap - 2 == -gap: # 1 star in the middle
        print(f"{' ' * (padding + 1)}*")
    elif gap == 0:
        print(f"{' ' * (padding)}**")
    gap = gap - 2
