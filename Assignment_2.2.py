''' Q) Write a Python program to print a dictionary whose keys should be the alphabet 
from a-z and the value should be corresponding ASCII values? '''

dict1 = {}

for i in range(97, 97 + 26):
    dict1[chr(i)] = i

print(dict1)