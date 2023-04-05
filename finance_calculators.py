# Import Math module
import math

#Have user specify which calculator they'd like to use, investment interest or bond interest

print("Welcome to the Interest Calculator. Please type in the calculator you'd like to use: ")
print("Investment: To calculate the amount of interest you'll earn on your investment.")
print("Bond: To calculate the amount you'll have to pay on a home loan.")
selection = input("Enter either 'investment' or 'bond' from the menu above to proceed: ")

#Cleans user input by converting to capital letters and removing white space
selection = selection.upper()
selection = selection.strip()

# Investment Tree
if selection == "INVESTMENT":
    print("Investment selected!")
    deposit = int(input("Please enter the amount of your initial deposit: "))
    interest_rate = input("Please enter your interest rate: ")
    interest_rate = int(interest_rate.replace("%", ""))
    interest_rate = interest_rate/100
    investment_period = int(input("How many years are you going to invest? :"))
    interest = input("Please enter interest type: Simple or Compound: ")
    interest = interest.upper()
    if interest == "SIMPLE":
        print("You've selected simple interest.")  
        total = deposit*(1+(interest_rate*investment_period))
        print(f"Your total is: ${total}.")
        print(f"You are depositing ${deposit}, at an interest rate of {interest_rate}% for a period of {investment_period} years.")
    elif interest == "COMPOUND":
        print("You've selected compound interest.")
        total = deposit * math.pow((1 + interest_rate),investment_period)
        print(f"Your total is ${total}.")
        print(f"You are depositing ${deposit}, at an interest rate of {interest_rate}% for a period of {investment_period} years.")
#Bond Tree
elif selection == "BOND":
    print("Bond Selected!")
    home_value = input("Please enter the value of your house: ")
    interest_rate = input("Please enter the interest rate: ")
    interest_rate = (interest_rate/100) / 12
    investment_period = int(input("How many years are you repaying the bond?: "))
    total = (interest_rate * deposit)/(1-(1 + interest_rate))**(-investment_period)
    print(f"Your total is ${total}.")
    print(f"You are depositing ${deposit}, at an interest rate of {interest_rate}% for a period of {investment_period} years.")
#Bond Tree

else:
    print("Error- Please enter a valid option: 'Bond' or 'Investment' ")