#!/usr/bin/env python3

# Definiere die Variablen
boolean_variable = True
string_variable = "hello world!"
integer_variable = 42

# Gprint variables
print("Boolean Variable:", boolean_variable)
print("String Variable:", string_variable)
print("Integer Variable:", integer_variable)

# Functioin to check if it is a + or - number
def check_sign(num):
    if num > 0:
        print("this number is positiv.")
    elif num < 0:
        print("this number is negativ.")
    else:
        print("this number is zero.")


# examplenumber
number = -10

# Start of the function
check_sign(number)

# string

string1 = "coffee please"

# For-loop to run trough every numer in the string
for char in string1:
    print(char)
