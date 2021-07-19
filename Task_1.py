# Write a function that takes an array of positive integers.
# The function should calculate the sum of all even and odd integers and return an array containing the sums.
# The first index in the returned array should hold the sum of the even integers and the second index should hold the sum of the odd integers.

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

even_arr = []
# The code above will be used to collect a list of even numbers in the array

odd_arr =[]
# The code above will be used to collect a list of odd numbers in the array


for num in arr:
    if num%2==0:
        even_arr.append(num)
    else:
        odd_arr.append(num)
# The code above tells if the number is even or odd by getting the remainder of the number when divided by 2

sum_even = sum(even_arr)
sum_odd = sum(odd_arr)
# The codes above collects the sum of the even numbers and the sum of the odd in variable

new_array = []
new_array.extend((sum_even, sum_odd))
# The code above extends sum_even and sum_odd into the new variable, new_array
print (new_array)
