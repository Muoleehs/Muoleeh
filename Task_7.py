import statistics
from array import *
# The * above implies the need to work with all array functions

arr = array ('I', [])
# 'I' represents a type code for unsigned/positive integers as the task demands

length = int(input("Enter the length of the array: "))
# This collects the number of integers expected in the array

for i in range(length):
    x = int(input("Input Number: "))
    arr.append(x)
# The code above collects the numbers to be in the array using a for-loop in the range of numbers collected in variable "z"
# The append function also inserts the numbers into the array
std = statistics.stdev(arr)
print("The standard deviation is ",std)
