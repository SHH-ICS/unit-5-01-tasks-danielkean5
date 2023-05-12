# Create a program that will ask the user an addition question. 
# The program will generate two random numbers between 1 and 100, and display them as an addition question with appropriate prompts.
import math

num1 = int(input("Pick your first number between 1-100\n"))
num2 = int(input("Pick your second number between 1-100\n"))

ans = num1 + num2

user = int(input("What are these two numbers added together?\n"))
if ans == user:
  print("Correct!")
else:
  print("Incorrect.")