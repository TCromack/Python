# Tyler Cromack
# 12/10/2019
# CIT-4205-DE1
# Homework #8 Rainfaill
# This program takes a user's input and returns rainfaill totals highs lows and a graph

import matplotlib.pyplot as plt

def main() :

    Months = ("January", "February", "March", "April", "May" ,"June" ,"July" ,"August" ,"September", "October", "November", "December")
    monthRain = [None] * 12
    totalRain = 0
    
    #Continue to loop until user enters correct input until we reach the end of the tuple
    for index,month in enumerate(Months):
       while True:
            monthRain[index] = getRainfallInput(month)
            if monthRain[index] > -1 :
                break
    totalRain = sum(monthRain)
    #Print the Results
    print("Total Rainfall: {:.2f} ".format(totalRain))
    print("Average Rainfall: {:.2f} ".format(totalRain / 12))
    print("Highest Rainfall: {:1} ".format(Months[monthRain.index(max(monthRain))]))
    print("Lowest Rainfall: {:1} ".format(Months[monthRain.index(min(monthRain))]))
    showRainFallGraph(Months, monthRain)
      
        
def getRainfallInput(month):
    #Logic for the user input if not numeric ask again if less than 0 ask again
    try :
        ret = float(input("Enter the rainfall for {:3}:".format(month))) 
        
        if ret < 0:
            print("\nThe value entered must be non-negative.\n")
            return -1
           
    except ValueError:
        print("input must be a numeric value")
        return -1
    return ret

def showRainFallGraph(Months, monthRain):
    #plots the graph
    plt.plot(list(map(lambda monthName:monthName[:3], Months)), monthRain, 's-')
    plt.grid(True)
    plt.title("Line graph Rainfall Averages")
    plt.xlabel("Months of the Year")
    plt.ylabel("Average Rainfall in inches")
    plt.show()
     
main()
