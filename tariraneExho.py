#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from array import *
from math import *
def tarirane (inputFile):
    workArr = []
    inputFile = inputFile.readlines()
    print inputFile
    for index in range(0,len(inputFile),1):
        workArr.insert(index,inputFile[index].replace(',','.').split(' '))
        workArr[index].insert(3, (float(workArr[index][1]) - float(workArr[index][2])) * 1000)
    vEH = 0
    for arr in workArr:
        vEH+=arr[3]

    vEH = vEH / len(workArr)
    print vEH;
    vv = 0
    for arr in workArr:
        arr.insert(4,vEH - arr[3])
        vv+=arr[4]*arr[4]

    mu = sqrt(vv/(len(workArr)-1))
    resFile = open(raw_input('Choose output file:'),'w')
    resFile.write("|No |Z_lot [m]|Z_eholot [m]| dZi [mm]|\n")
    for res in workArr:
        resFile.write("|%3i|%9.2f|%12.2f|%9.1f|\n"%(int(res[0]),float(res[1]),float(res[2]),res[3]))

    resFile.write('Обща поправка на ехолота v = ' + str(vEH) + ' mm')
    resFile.write('\nСредна квадратна грешка на поправката  mu = ' + str(mu) + ' mm')
    resFile.close()
    return vEH

