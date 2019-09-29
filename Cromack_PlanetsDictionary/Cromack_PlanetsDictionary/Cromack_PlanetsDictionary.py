# Tyler Cromack
# CromackT@student.elms.edu
# 9/23/19
# CIT-4205-DE1
# Homework #1 Inter Planetary Weights
# This program takes a users weight and multiplys theere weight by another planets gravity coefficent to return their weight on that planet.

#Create a Dictionary of Planet names and Gravity Coefficents
planets = {"Mercury" : 0.38, "Venus" : 0.91, "our Moon" : 0.165, "Mars" : 0.38, "Juptier" : 2.34, "Saturn" : 0.93, "Uranus" : 0.92, "Neptune" : 1.12, "Pluto" : 0.066}

#Get user input
sName = input("Please enter your name: ")
nWeight = float(input("Please enter your weight: "))

#Print user input
print(sName + " here are your weights on our Solar System's planets:")

#Go through the dictionary and retrive Planet name and Gravity Coefficent then perform math on User weight with Gravity Coefficent then print the result
for planet, nGRAVITY_COEFF in planets.items():
    print('{:29}'.format("Weight on " + planet + ":"), '{:10,.2f}'.format(float(nGRAVITY_COEFF * nWeight)))
