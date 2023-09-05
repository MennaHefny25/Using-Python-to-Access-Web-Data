"""

In this assignment you will read through and parse 
a file with text and numbers. 
You will extract all the numbers in the file 
and compute the sum of the numbers.

"""
import re

filename = 'regex_sum_1882180.txt'
with open(filename) as file:
    text = file.read()


numbers = re.findall('[0-9]+', text)

sum_of_numbers = sum(int(number) for number in numbers)

print("The sum of the numbers is:", sum_of_numbers)
