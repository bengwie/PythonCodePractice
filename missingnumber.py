#!/usr/bin/python

def testMe(nums):
   maxRep = 0
   currentNum = None
   num_dict = dict()
   firstNum = None
   for (index, num) in enumerate(nums):
      print "num: %s" % num
      if index == 0:
         firstNum = num
      if num in num_dict:
         num_dict[num] += 1
      else:
         if (maxRep != 0 and num_dict[previousNum] < maxRep):
            return previousNum
         
         num_dict[num] = 1

      if maxRep < num_dict[num]:
         maxRep = num_dict[num]
      if index == len(nums) - 1:
         if num_dict[num] < maxRep:
            return num
         else:
            return nums[0]
      
      previousNum = num

if __name__ == '__main__':
   sample = "11222333"
   output = testMe(sample)
   print output
