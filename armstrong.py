digit=int(input('to check if it is armstrong numbers: '))
reverse = digit 
store = digit 
count = 0
while digit!= 0:
    digit//=10
    print (digit) 
    count+=1 
print("Total digit is: ", count)

print (store)

temp = 0
arm = 0
while store!= 0:
    temp = store % 10 
    temp**=count
    arm+=temp
    print("this is arm: ", arm)
    store //= 10 

if (arm == reverse) :
    print("It's a Armstrong Number")
else: 
    print("It's not a Armstrong Number")

