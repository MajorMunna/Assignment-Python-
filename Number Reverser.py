num = int(input("Enter an integer: "))

reversed_num = 0

while num > 0:
            digit = num % 10  # Get the last digit
            reversed_num = (reversed_num * 10) + digit  # Append the digit to reversed_num
            num //= 10
            
print(reversed_num)