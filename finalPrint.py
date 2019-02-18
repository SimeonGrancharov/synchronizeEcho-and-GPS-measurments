from array import *

def printAllResults(finalArray):
    kraenFormat = open('FinalPoints.txt','w')

    for row in finalArray:
        kraenFormat.write("%i,%.3f,%.3f,%.2f\n"%(row[0]+1,row[1],row[2],row[3]))

    kraenFormat.close()
    return 1