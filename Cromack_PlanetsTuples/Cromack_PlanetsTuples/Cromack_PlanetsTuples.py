# Tyler Cromack
# CromackT@student.elms.edu
# 9/23/19
# CIT-4205-DE1
# Homework #1 Inter Planetary Weights
# This program takes a users weight and multiplys theere weight by another planets gravity coefficent to return their weight on that planet.

# Planet Surface Gravity Factors
nMERCURY = 0.38
nVENUS = 0.91
nMOON = 0.165
nMARS = 0.38
nJUPITER = 2.34
nSATURN = 0.93
nURANUS = 0.92
nNEPTUNE = 1.12
nPLUTO = 0.066

#Creates Tuples of Planet and Gravity Coefficents
Gravity_Coeff = (nMERCURY, nVENUS, nMOON, nMARS, nJUPITER, nSATURN, nURANUS, nNEPTUNE, nPLUTO)
Planets = ("Mercury", "Venus", "our Moon", "Mars", "Jupiter" ,"Saturn" ,"Uranus" ,"Neptune" ,"Pluto")

#Get user input
sName = input("Please enter your name: ") #Name
nWeight = float(input("Please enter your weight: ")) #Weight

#Print user input
print(sName + " here are your weights on our Solar System's planets: ")

#Grabs Planet name and Gravity Coefficent then perform math on User weight with Gravity Coefficent then print the result
for i in range(9):
    print('{:27}'.format("Weight on " + Planets[i] + ": ") +  '{:10,.2f}'.format((nWeight * Gravity_Coeff[i])))
