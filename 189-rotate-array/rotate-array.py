class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        a=[]
        for i in range(k%n):
            b=nums.pop()
            a.append(b)
        a.reverse()
        nums[:]=a+nums
        return nums
