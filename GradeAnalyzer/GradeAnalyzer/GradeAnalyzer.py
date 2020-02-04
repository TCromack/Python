# Tyler Cromack
# 10/1/19
# CIT-4205-DE1
# Homework #4 Grade Analyzer
# This program takes a user's Tests and takes the sum of Gradess and number of Test taken to give the user a final Grade.

test = [] #Declare the test array to hold values in the future
nARRAYLENGTH = 4 #Set the array length
nArraySum = 0 #Set sum value to 0
nArrayLength = 0 #Set array count value to 0
nFinalGrade = 0 #Set grade average to zero
sNAME = input("Name of person that we are calculating the grades for:  ") #get the user's name

#Get however many tests the user wishes to enter and add the scores to the array
for i in range(nARRAYLENGTH):
    
    nUserValues = int(input("Test " + str(i + 1) + ": "))
    test.append(nUserValues)

#Ask if user would like to drop lowest Letter Grade
sLowGrade = input("Should the lowest test score be dropped Y or N? ")

#Make sure values given by user are greater than 0 in the array
for i in test:
    if i <= 0:
        print("Test scores must be greater than 0.")
        exit("Test scores must be greater than 0.")

#Calculate the length of the array
for i in test:
        nArrayLength = nArrayLength + 1              

minimum = test[0] #Set the minimum value of the array to index 0

if sLowGrade == "Y":
    
    for i in range(nArrayLength): #If the user wants to drop the grade iterate through the length of the array
        
        if test[i] < minimum: #If the current number is less than the current minimum value set the minimum value to the new value
                              
           minimum = test[i]

    #Remove the lowest value from the array
    test.remove(minimum)
    nArrayLength = nArrayLength - 1
 
    #Sum the values of the array
    for i in test:
        nArraySum += i
   
    nFinalGrade = nArraySum / nArrayLength #Calculate the Average of the Grades using the Sum and Length of the array
    print(sNAME + " test average is: " + '{:.1f}'.format(nFinalGrade)) #Print the users final grade

elif sLowGrade == "N":
   
   #Sum the values of the array
    for i in test:
        nArraySum += i
    
    nFinalGrade = nArraySum / nArrayLength #Calculate the Average of the Grades using the Sum and Length of the array
    print(sNAME + " test average is: " + '{:.1f}'.format(nFinalGrade)) #Print the users final grade
else:
    print("Enter Y or N to Drop the Lowest Grade.")
    exit("Enter Y or N to Drop the Lowest Grade.")

#Give user a letter grade base on the final grade average
if nFinalGrade >= 97.0:
    sLetterGrade = "A+"
elif nFinalGrade >= 94.0 and nFinalGrade <= 96.9:
    sLetterGrade = "A"
elif nFinalGrade >= 90.0 and nFinalGrade <= 93.9:
    sLetterGrade = "A-"
elif nFinalGrade >= 87.0 and nFinalGrade <= 89.9:
    sLetterGrade = "B+"
elif nFinalGrade >= 84.0 and nFinalGrade <= 86.9:
    sLetterGrade = "B"
elif nFinalGrade >= 80.0 and nFinalGrade <= 83.9:
    sLetterGrade = "B-"
elif nFinalGrade >= 77.0 and nFinalGrade <= 79.9:
    sLetterGrade = "C+"
elif nFinalGrade >= 74.0 and nFinalGrade <= 76.9:
    sLetterGrade = "C"
elif nFinalGrade >= 70.0 and nFinalGrade <= 73.9:
    sLetterGrade = "C-"
elif nFinalGrade >= 67.0 and nFinalGrade <= 69.9:
    sLetterGrade = "D+"
elif nFinalGrade >= 64.0 and nFinalGrade <= 66.9:
    sLetterGrade = "D"
elif nFinalGrade >= 60.0 and nFinalGrade <= 63.9:
    sLetterGrade = "D-"
else:
    sLetterGrade = "F" #Since 60.0 and above has a condition, a grade of less than 60.0 is implied to be an 'F'.

print("Letter Grade for the test is: " + sLetterGrade)