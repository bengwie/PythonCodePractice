#!/usr/bin/python

def bubbleSort(inputList):
   for i in range(len(inputList)):
      for j in range(i + 1, len(inputList)):
         #print "comparing i: %d value: %d, j: %d, value: %d" % (i, inputList[i], j, inputList[j])
         if inputList[i] > inputList[j]:
            temp = inputList[i]
            inputList[i] = inputList[j]
            inputList[j] = temp
   return inputList

import time

if __name__ == "__main__":
   #temps = [3, 2, 5, 1, 2, 100, 200, 300, 50, 29, 23, 22, 89, 90]
   temps = [90, 89, 22, 23, 29, 50, 300, 200, 100, 2, 1, 5, 2, 3] 
   time1 = time.time() * 1000000
   bubbleSort(temps)
   time2 = time.time() * 1000000
   print temps
   print "time1: %d, time2: %d, detla: %d" % (time1, time2, time2-time1)
   
