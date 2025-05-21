x = float(input("Enter the x-coordinate: "))
y = float(input("Enter the y-coordinate: "))

if x == 0 and y == 0:
            print(f"The point ({x}, {y}) is at the Origin.")
elif x == 0:
        print(f"The point ({x}, {y}) is on the Y-axis.")
elif y == 0:
            print(f"The point ({x}, {y}) is on the X-axis.")
elif x > 0 and y > 0:
            print(f"The point ({x}, {y}) is in the 1st Quadrant.")
elif x < 0 and y > 0:
            print(f"The point ({x}, {y}) is in the 2nd Quadrant.")
elif x < 0 and y < 0:
            print(f"The point ({x}, {y}) is in the 3rd Quadrant.")
elif x > 0 and y < 0:
            print(f"The point ({x}, {y}) is in the 4th Quadrant.")