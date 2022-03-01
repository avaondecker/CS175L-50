#CS175
#Ava Ondecker
#rainfall.py

x = 0

total = 0

year = int(input("Enter the number of years: "))

while year < 1 or year > 3:
    year = int(input("Enter the number of years: "))
    if year < 1 or year > 3:
        print("Invalid number")

for rf in range(year):
    
    print("For year", rf+1,": ")
    
    for rf in range(12):
        
        print("Enter the rainfall amount for the month: ", end = '  ')


        r = float(input())
        total = total + r
        x = x + 1

avg = total / x
print("For" , year * 12 , "months")
print("Total rainfall = " , total, "inches")
print("Average monthly rainfall = ", avg, "inches")
