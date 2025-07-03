# Write a program to print the frequencies of elements in an array
my_array = [1, 2, 2, 3, 1, 4, 2, 3, 5]

# by using dictionaries

dict_array = {}

for element in my_array:
    if element in dict_array:
        dict_array[element] += 1
    else:
        dict_array[element] = 1 


for key, value in dict_array.items():
    print(f"Element {key} appears: {value} times")

