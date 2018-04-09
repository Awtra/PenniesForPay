#Ali Mody
#This program calculates the total of what the person payed in the
#form of pennies.

#Initialize Variables
total = 0
pennies = 1
day = int(input("Please input the amount of days you would like to calculate for.  "))
day2 = 1

#Use a For Loop in order to calculate the pennies.
for day in range (1, day + 1, 1):
    print("You have $", pennies / 100, "day", day2)
    day = day -1
    day2 = day2 + 1
    pennies = pennies*2
    total += pennies

# Print the total

print("You have $", total / 200, "in all. ")
