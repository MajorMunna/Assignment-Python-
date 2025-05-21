num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

if operator == '+':
    print("Result is: ", num1+num2)
elif operator == '-':
    print("Result is: ", num1-num2)
elif operator == '*':
    print("Result is: ", num1*num2)
elif operator == '/':
            if num2 != 0:  # Handle division by zero
                print("Result is: ", num1/num2)
            else:
                print("Error: Can't division by zero.")
else:
    print("Invalid operator. Please use +, -, *, or /.") 