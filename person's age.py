'''Write a Python program that takes a person's age as input and
prints out whether they are an infant (0-1), toddler (2-3), child (4-12), teenager
(13-19), adult (20+).'''

age = int(input("Enter the person's age: "))

if 0 <= age <= 1:
        print("level = infant")    
elif 2 <= age <= 3:
    print("level = toddler")          
elif 4 <= age <= 12:
    print("level = child")         
elif 13 <= age <= 19:
     print("level = teenager")         
elif age >= 20:
    print("level = adult")          
else:
    print("Age Can't be negative")          