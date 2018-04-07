#!/usr/bin/python

def testMe(nums):
   maxRep = 0
   num_dict = dict()
   previousNum = None

   for (index, num) in enumerate(nums):
      print "num: %s" % num
      if num in num_dict:
         num_dict[num] += 1
      else:
         if maxRep != 0:
            if num_dict[previousNum] < maxRep:
               return previousNum
            elif len(num_dict.keys()) == 2 and maxRep > num_dict[nums[0]]:
               return nums[0]
         num_dict[num] = 1
         

      if maxRep < num_dict[num]:
         maxRep = num_dict[num]

      if index == len(nums) - 1:
         if len(num_dict.keys()) == 1:
            return -1
         else:
            return num

      previousNum = num

   
if __name__ == '__main__':
   samples = ["11222333",
              "11122333",
              "11122233",
              "11222333444555666777888",
              "1112233344455666777888",
              "11122233344455566777888",
              "11122233344455566677788",
              "111"
             ]
   import time

   for sample in samples:
      print "Sample is: %s" % sample
      time1 = time.time()
      output = testMe(sample)
      time2 = time.time()
      print "start time: %d" % time1
      print "end time: %d" % time2

      delta = time2 - time1
      print "output: %s with time: %d" % (output, delta)
      
