# Create a program that accepts 2 numbers from the user. 
# Your program will output a random number between the range given by the user.
import random

num1 = int(input("Input first number:\n"))
num2 = int(input("Input second number:\n"))
random = random.randint(num1,num2)
print("Your number is:\n",random)