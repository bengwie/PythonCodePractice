#!/usr/bin/python

def mergeSort(temps):
   if len(temps) > 1:
      middle = len(temps) / 2

      left = temps[0:middle]
      right = temps[middle:]
      mergeSort(left)
      mergeSort(right)

      i = 0
      j = 0
      k = 0

      while(i < len(left) and j < len(right)):
         if left[i] < right[j]:
            temps[k] = left[i]
            i += 1
         else:
            temps[k] = right[j]
            j += 1
         k += 1

      while i < len(left):
         temps[k] = left[i]
         i += 1
         k += 1

      while j < len(right):
         temps[k] = right[j]
         j += 1
         k += 1

import time
if __name__ == "__main__":
   temps = [3, 2, 5, 1, 2, 100, 200, 300, 50, 29, 23, 22, 89, 90] 
   time1 = time.time() * 1000000
   mergeSort(temps)
   time2 = time.time() * 1000000
   print temps
   print "time1: %d, time2: %d, detla: %d" % (time1, time2, time2-time1)
