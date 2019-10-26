# Tyler Cromack
# 10/17/19
# CIT-4205-DE1
# Homework #6 Compound Interest with Functions
# This program takes a user's Principle, Interest Rate, Times Compunded and
# Years in order to give their Future Value for their investment.

import math

fDeposit = fRATE = nTIMESCOMPOUNDED = iYEARS = 0 #Initialize the variables to 0
fGOAL = -1 #Set fGOAL to less than 0
nTIMESCOMPOUNDED_CONST = 12 #A year has 12 months

#Compund Interest Formula
def CompundFormula(fDeposit, fRATE, nTIMESCOMPOUNDED):
    return fDeposit * (1 + fRATE) ** (nTIMESCOMPOUNDED)

#Solve for Time in Compound Interest Equation
def YearsToReachGoal(fGOAL, fDeposit, nTIMESCOMPOUNDED, nMONTHLY_INTEREST_RATE):
    return math.log(fGOAL / fDeposit) / (nTIMESCOMPOUNDED * math.log(1 + nMONTHLY_INTEREST_RATE)) 

#Since many of the conditions are the same we can put them in a function
def RequestInput(question):
    try :
        ret = float(input(question)) 
        if ret <= 0:
            print("\nThe value entered must be greater than 0.\n")
            return 0
        else :
            return ret

    except ValueError:
        print("\ninput must be a numeric value")
        return 0

#Get User Inputs
while fDeposit <= 0 :
    fDeposit = RequestInput("Enter the starting principal: ") #Initial Deposit
    
while fRATE <= 0 :
    fRATE = RequestInput("Enter the annual interest rate: ") / 100 #Convert to decimal

while nTIMESCOMPOUNDED <= 0:
    nTIMESCOMPOUNDED = int(RequestInput("How many times per year is the interest compounded? ")) #Cast to int 

while iYEARS <= 0:
    iYEARS = int(RequestInput("How many years do you want to grow the account? ")) #Cast to int since years are not floats
      
while fGOAL < 0 :
    try :
        fGOAL = float(input("What is the Goal Amount?: ")) 
        if fGOAL < 0:
            print("\nThe value entered must be non-negative.")

    except ValueError:
        print("input must be a numeric value")

nMONTHLY_INTEREST_RATE = fRATE / nTIMESCOMPOUNDED #take the interest rate and divide by number of times coumpounded to find interest rate
iCompoundPeriod = iYEARS * nTIMESCOMPOUNDED #Calculate the number of times compunded

for month in range(iCompoundPeriod):
    print("Compound Period {:3}: Account Balance is: $ {:,.2f}".format(month + 1, CompundFormula(fDeposit, nMONTHLY_INTEREST_RATE, month + 1)))
    
print("It will take {:.0f} months to reach your desired goal of $ {:,.2f}".format(math.ceil(YearsToReachGoal(fGOAL, fDeposit, nTIMESCOMPOUNDED, nMONTHLY_INTEREST_RATE) * nTIMESCOMPOUNDED_CONST), fGOAL))
print("At the end of {:.1f} years you will have $ {:,.2f}".format(iYEARS,CompundFormula(fDeposit, nMONTHLY_INTEREST_RATE, nTIMESCOMPOUNDED * iYEARS)))