Python 3.12.3 (tags/v3.12.3:f6650f9, Apr  9 2024, 14:05:25) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def calculate():
...     try:
...         num1 = float(input("Enter the first number: "))
...         operator = input("Enter the operator (+, -, *, /): ")
...         num2 = float(input("Enter the second number: "))
...         
...         if operator == '+':
...             result = num1 + num2
...         elif operator == '-':
...             result = num1 - num2
...         elif operator == '*':
...             result = num1 * num2
...         elif operator == '/':
...             
...             if num2 == 0:
...                 return "Error: Division by zero is not allowed."
...             result = num1 / num2
...         else:
...             return "Error: Invalid operator."
...         
...         return f"The result is: {result}"
...     
...     except ValueError:
...         return "Error: Invalid input. Please enter numeric values."
... 
