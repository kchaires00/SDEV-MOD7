Python 3.13.2 (tags/v3.13.2:4f8bb39, Feb  4 2025, 15:23:48) [MSC v.1942 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Author: Kelli Chaires
>>> # Description: This program creates a list of 15 numbers and checks if each number is even or odd.
>>> # It then prints the result in the format: "1 is odd" or "2 is even".
>>> 
>>> # Initialize a list with 15 integers
>>> 
>>> numberList = [5, 7, 12, 22, 4, 13, 6, 8, 10, 1, 14, 17, 9]
>>> 
>>> # Loop through each number in the list
>>> for number in numberList:
...     # Check if the number is even
...     if number % 2 == 0:
...         print (str(number) + "is even")
...     else
...     
SyntaxError: expected ':'
>>> for number in numberList:
...     # Check if the number is even
...     if number % 2 == 0:
...         print (str(number) + "is even")
...     else:
...         print (str(number) + "is odd")
... 
...         
5is odd
7is odd
12is even
22is even
4is even
13is odd
6is even
8is even
10is even
1is odd
14is even
17is odd
9is odd
