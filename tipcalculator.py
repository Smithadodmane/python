("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total=(bill*(1+tip/100))/people
final=round(total,3)
print(f"each person should pay {final}")