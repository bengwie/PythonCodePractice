#!/usr/bin/python

def quickSort(inputList):
   start = 0
   end = len(inputList) - 1
   quickSortHelper(inputList, start, end)

def quickSortHelper(inputList, start, end):
   splitPoint = partition(inputList, start, end)
   if splitPoint > start: 
      quickSortHelper(inputList, start, splitPoint - 1)
   if splitPoint < end:
      quickSortHelper(inputList, splitPoint + 1, end)

def partition(inputList, start, end):
   print "beginning partition from start: %d end: %d analyzing: %s" % (start, end, inputList[start:end + 1])
   pivot = inputList[start]
   leftMark = start + 1
   rightMark = end
   done = False

   while not done:
      while leftMark <= rightMark and inputList[leftMark] <= pivot:
         leftMark += 1
         print "leftMark is changed to: %d" % leftMark
      while rightMark >= leftMark and inputList[rightMark] >= pivot:
         rightMark -= 1
      if rightMark < leftMark:
         done = True
      else:
         temp = inputList[leftMark]
         inputList[leftMark] = inputList[rightMark]
         inputList[rightMark] = temp

   # Swapping right mark with pivot
   if rightMark > start:
      temp = inputList[rightMark]
      inputList[rightMark] = inputList[start]
      inputList[start] = temp
      print "Exiting rightMark is: %d" % rightMark
   return rightMark

import time

if __name__ == "__main__":
   temps = [90, 89, 22, 23, 29, 50, 300, 200, 100, 2, 1, 5, 2, 3]
   time1 = time.time() * 1000000
   quickSort(temps)
   time2 = time.time() * 1000000
   print temps
   print "time1: %d, time2: %d, detla: %d" % (time1, time2, time2-time1)
