import math
# Create a program that will accept the two legs of a right-angle triangle, a and b, and display the length of the hypotenuse, c. 
# Remember to use prompts for the input and labels for the output. Use the formula a2 + b2 = c2 to calculate your answer.
a = int(input("Input a:\n"))
b = int(input("Input b:\n"))
c = a**2 + b**2
c = math.sqrt(c)
print(c)