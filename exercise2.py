# Write a function that takes a list of numbers and returns a list with only the even numbers.
def filter_even(number_list): return [number for number in number_list if number % 2 == 0] # Returns item if it is divisible by 2 (even)
print(filter_even([1, 2, 3, 5, 7, 8, 9, 10, 12, 13])) # Example list of numbers