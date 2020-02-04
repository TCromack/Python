# Tyler Cromack
# 10/1/19
# CIT-4205-DE1
# Homework #3 BMI Analyzer
# This program takes a user's height and weight then calculates the user's BMI Category.

print("Welcome to Tyler Cromack's BMI Calculator\n")
sNAME = input("Name of the person we are calculating the BMI for:  ")
nHEIGHT = int(input("Enter your height in Inches: ")) 
nWEIGHT = int(input("Enter your weight in Pounds: ")) 
fMETERS = nHEIGHT/39.36 #Convert Height to Meters
fKILOS = nWEIGHT/2.2    #Convert pounts to Kilograms

fBmi = fKILOS / fMETERS**2 #Calculate the user BMI

#Check what category the user's BMI fall
sBmiType = None #Declare an empty state to in order to display user's BMI type
if fBmi <= 18.50:
    sBmiType = "Underweight"
elif fBmi >= 18.51 and fBmi <= 24.90:
    sBmiType = "Normal"
elif fBmi >= 24.91 and fBmi <= 29.90:
    sBmiType = "Overweight"
else:                       #anything over 29.90 is implied obese since other case are taken care of
    sBmiType = "Obese"

#Print and format the user's BMI findings
print(sNAME + "'s BMI is: " + '{:.2f}'.format(fBmi) + "\nBMI finding is the subject is: " + sBmiType)
    


