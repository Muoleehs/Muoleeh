from array import *

# The * above implies the need to work with all array functions
parameter = []
arr = array('I', [])
# 'I' represents a type code for unsigned/positive integers as the task demands
array_list = []
length = int(input("Enter the length of the array: "))
# This collects the number of integers expected in the array

for i in range(length):
    x = int(input("Input Number: "))
    array_list.append(x)
print(array_list)
parameter.append(array_list)
# The code above collects the numbers to be in the array using a for-loop in the range of numbers collected in variable "z"
# The append function also inserts the numbers into the array
num = int(input("Input separate Number: "))
parameter.append(num)
print("The parameter is", (parameter))
for i in array_list:
    if num == i + i + i:
        print(i)
    else:
        print(-1)
