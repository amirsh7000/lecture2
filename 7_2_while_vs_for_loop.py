year=int(input("please enter year\n"))
temp_year=year
while year<2029:
    year+=1
    print(year)

print("inside for loop")

year=int(input("please enter year\n"))
for x in range(temp_year,2029,2):
    print(x)
    
    
month=int(input("please enter month\n"))
temp_month=month
while month<12:
    month+=1
    print(month)

print("inside for loop")

month=int(input("please enter month\n"))
for x in range(temp_month,12,2):
    print(x)
