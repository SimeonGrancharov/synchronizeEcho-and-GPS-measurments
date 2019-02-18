#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from array import *
from math import *

def calculateEchoCoords(synchornizedArray, vEholotno):
    a = float(raw_input('Insert cons a:'))
    b = float(raw_input('Insert const b:'))
    Ho = float(raw_input('Insert Hlata [m]:'))
    dh = float(raw_input('Insert height of water level [m]:'))

    c = sqrt(a*a + b*b)
    print c
    constAngle = atan2(b,a)
    if constAngle < 0:
        constAngle += 2*pi
    endResArr = []
    for row in range(0,len(synchornizedArray),1):
        if synchornizedArray[row+1][3] == 0:
            break
        dx = synchornizedArray[row+1][3]  - synchornizedArray[row][3]
        dy = synchornizedArray[row + 1][4] - synchornizedArray[row][4]
        alpha = atan2(dy,dx)
        if alpha < 0 : alpha+=2*pi
        alphaO = alpha + pi
        if alphaO>2*pi: alphaO-=2*pi
        endResArr.insert(row, [])
        endResArr[row].insert(0,row)
        X = synchornizedArray[row][3] + cos(alphaO + constAngle) * c
        Y = synchornizedArray[row][4] + sin(alphaO+constAngle) * c

        endResArr[row].insert(1,X)
        endResArr[row].insert(2,Y)
        dxi = endResArr[row][1] - synchornizedArray[row][3]
        dyi = endResArr[row][2] - synchornizedArray[row][4]
        endResArr[row].insert(3,sqrt(dxi*dxi + dyi*dyi))
        H = Ho + dh + vEholotno/1000 - float(synchornizedArray[row][1])
        endResArr[row].insert(3,H)
    return endResArr