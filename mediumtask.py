#!/usr/bin/env python3

# ask for age
age = int(input("Enter your age: "))

# check status (minor/adult/senior)
if age < 18:
    print("you're a minor.")
elif age >= 18 and age <= 65:
    print("you're an adult.")
else:
    print("damn you're old.")

# Initiation summary
total = 0

# while loop that runs until a negative number is given out
while True:
    number = int(input("enter a number(negative number to end the loop)): "))
    if number < 0:
        break
    total += number

# print the summary
print("the summary of all given numbers is:", total)

# for loop to caculate the ² 
for i in range(1, 11):
    square = i * i
    print("the ² of", i, "is", square)

