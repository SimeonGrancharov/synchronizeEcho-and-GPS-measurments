from array import *
def boundaryScript(inputFile):
    boundaryArr=[]
    boundScript = open('boundScript.txt','w')
    boundScript.write("pline\n")
    for index in range(0,len(inputFile),1):
        myStr = inputFile[index].replace('\t',' ')
        boundaryArr.insert(index,myStr.split(' '))

        while(len(boundaryArr[index]) >  4):
            indexOf = boundaryArr[index].index('')
            boundaryArr[index].pop(indexOf)
        print boundaryArr[index]
        boundScript.write(("%8.3f,%8.3f,%7.3f\n")%(float(boundaryArr[index][2]),float(boundaryArr[index][1]),float(boundaryArr[index][3])))

    boundScript.close()
    return 1
