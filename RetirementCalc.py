age = int(input("Current age: "))
age2 = age

while age < 0:
    age = int(input("Cannot be negative, try again: "))


year_start = float(input("Starting balance: "))
year_start2 = year_start
while year_start < 0:
    year_start = float(input("Cannot be negative, try again: "))

retirement_age = int(input("Target retirement age: "))
retirement_age_2 = retirement_age
while retirement_age < age:
    retirement_age = int(input("Cannot be less than current age, try again: "))

target_balance = float(input("Target balance at retirement: "))
target_balance2 = target_balance

total_age = retirement_age - age
total_age2 = total_age

while target_balance < year_start:
    target_balance = float(input("Cannot be less than starting balance, try again: "))

extra = float(input("Annual contribution amount: "))
extra2 = extra
while extra < 0:
    extra = float(input("Cannot be negative, try again: "))

annual_percent = float(input("Projected annual growth (percent): ")) / 100
annual_percent2 = annual_percent

while annual_percent < 0:
    annual_percent = float(input("Cannot be negative, try again: ")) / 100

year_end = 0
year_end2 = year_end

coast_found = True
growth = 0
growth2 = growth

stopping_age = total_age
counter = 0

while coast_found == True:

    for count in range(total_age):

        growth = year_start * annual_percent

        if count >= stopping_age:
            extra = 0

        year_end = year_start + growth + extra

        year_start = year_end

        age = age + 1


        if age >= retirement_age:
            break

    if not (target_balance  < year_end):
        counter = counter + 1
        break

    growth = growth2
    year_start = year_start2
    year_end = year_end2
    age = age2
    retirement_age = retirement_age_2
    annual_percent = annual_percent2
    stopping_age = stopping_age - 1
    counter = stopping_age
    extra = extra2



growth = growth2
year_start = year_start2
year_end = year_end2
age = age2
retirement_age = retirement_age_2
annual_percent = annual_percent2
extra = extra2

print()

print("Yay! You can reach that goal by contributing your annual amount for", (counter), "year(s) until age", (counter + age), "then coasting the rest of the way to", retirement_age)

print()

print("Age\tYear Start\tGrowth\t\tExtra\t\tYear End")

while coast_found == True:
    for count in range(total_age):
        growth = year_start * annual_percent

        if count >= counter:
           extra = 0

        year_end = year_start + growth + extra

        year_start = year_end
       
        print(f"{age}:\t${year_start:10.2f}\t${growth:10.2f}\t${extra:10.2f}\t${year_end:10.2f}")

        year_start = year_end
        age = age + 1
        
        if age >= retirement_age:
            coast_found = False
            break