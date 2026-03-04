class Solution(object):
    def missingNumber(self, nums):
        i=0
        while True:
            if i not in nums:
                return i
                break
            i+=1