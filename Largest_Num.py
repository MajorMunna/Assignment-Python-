'''Largest among Three Numbers: Write a Python program that takes
three numbers as input and prints out the largest among them'''

num1 = float(input("Enter your First Number: "))
num2 = float(input("Enter your Second Number: "))
num3 = float(input("Enter your Third Number: "))

if num1> num2 and num1 > num3:
    print("Largest Number is: ", num1)

elif num2 > num1 and num2 > num3:
    print("Largest Number is: ", num2)

else:
    print("Largest Number is: ", num3)