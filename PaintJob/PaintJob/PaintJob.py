# Tyler Cromack
# 10/17/19
# CIT-4205-DE1
# Homework #7 Paint Job with Functions
# This program takes a user's input and calculates the various costs of the Paint Job to be performed

import math
import re

def main() :   
    fSquareFeet = fPaintPrice = fFeetPerGallon = fLaborHoursPerGallon = fLaborChargePerHour = sWorkState = 0

    #Used Regex to validate user input for state of worked performed, Must be characters a thru z with a length of 2
    while True :
        sWorkState = input("What State is the work done in? ")
        if not re.match("^[A-Za-z]{2}$", sWorkState):
            print("INPUT MUST BE A TWO CHARACTER STRING!")
    
        else :
            break
    
    #Get User Inputs
    while fSquareFeet <= 0 :
        fSquareFeet = getFloatInput("Enter the square footage of the wall to be painted: ")

    while fPaintPrice <= 0 :
        fPaintPrice = getFloatInput("Enter the price of the paint: ")

    while fFeetPerGallon <= 0 :
        fFeetPerGallon = getFloatInput("Enter the feet per gallon of the paint: ")

    while fLaborHoursPerGallon <= 0 :
        fLaborHoursPerGallon = getFloatInput("Enter the labor hours per gallon of the paint: ")

    while fLaborChargePerHour <= 0 :
        fLaborChargePerHour = getFloatInput("What is the Labor charge per hour? ")
    
    #Run the Output Function 
    showCostEstimate(fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour, sWorkState)

#Calculate Gallons of paint needed for the job
def getGallonsOfPaint(fSquareFeet, fFeetPerGallon) :
    return int(math.ceil(fSquareFeet / fFeetPerGallon))

#Calculate hours to finish job
def getLaborHours(fSquareFeet, fFeetPerGallon, fLaborHoursPerGallon) :
    return math.ceil(fSquareFeet / fFeetPerGallon * fLaborHoursPerGallon)

#Calculate cost of the labor
def getLaborCost(fSquareFeet, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour) :
    return getLaborHours(fSquareFeet, fFeetPerGallon, fLaborHoursPerGallon) * fLaborChargePerHour

#Calculate the cost of the paint
def getPaintCost(fSquareFeet, fPaintPrice, fFeetPerGallon) :
    return getGallonsOfPaint(fSquareFeet, fFeetPerGallon) * fPaintPrice

#Function to Validate the user input
def getFloatInput(question):
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

#Return a tax rate based on the state entered by the user
def getSalesTax(sWorkState) :
    if sWorkState == 'CT' or sWorkState == 'VT' :
        return 0.06
    elif sWorkState == 'MA' :
        return 0.0625
    elif sWorkState == 'ME' :
        return 0.085
    elif sWorkState == 'NH' :
        return 0.0
    elif sWorkState == 'RI' :
        return 0.07
    else :
        return 0.0

#Calculate the cost of all work performed
def workCostEstimate(fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour) :
    return getPaintCost(fSquareFeet, fPaintPrice, fFeetPerGallon) + getLaborCost(fSquareFeet, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour)

#Calculate the tax based on the cost of all work performed as well as paint cost
def getTaxCost (fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour , sWorkState) :
    return workCostEstimate(fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour) * getSalesTax(sWorkState)

#Calculate the total cost of all work performed plus the tax
def getTotalCost (fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour , sWorkState) :
    return workCostEstimate(fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour) + getTaxCost (fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour , sWorkState)

#Returns a string of all relevant values 
def getCostEstimateString(fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour, sWorkState) :
    return "Gallons of Paint needed: {:3}\nHours of labor: {:.1f}\nLabor Charges: {:.2f}\nPaint Charges: {:.2f}\nTotal Tax: {:.2f}\nTotal Cost: {:.2f}".format(
        getGallonsOfPaint(fSquareFeet, fFeetPerGallon), getLaborHours(fSquareFeet, fFeetPerGallon, fLaborHoursPerGallon), 
        getLaborCost(fSquareFeet, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour), 
        getPaintCost(fSquareFeet, fPaintPrice, fFeetPerGallon), 
        getTaxCost (fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour , sWorkState),
        getTotalCost (fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour , sWorkState))

#Write data to .txt file
def writeToFile(fileName, data) :
    file = open(fileName, "w")
    file.write(data)
    file.close()

#Prints and writes calculated values to txt file
def showCostEstimate(fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour, sWorkState) :
    retString = getCostEstimateString(fSquareFeet, fPaintPrice, fFeetPerGallon, fLaborHoursPerGallon, fLaborChargePerHour, sWorkState)
    print(retString) 
    writeToFile("PaintJobOutput.txt", retString) 

main()