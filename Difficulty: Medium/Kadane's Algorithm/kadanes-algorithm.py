class Solution:
    def maxSubarraySum(self, arr):
        sumi = 0
        fsum = arr[0]
        for i in arr:
            sumi = max ( i, sumi+i)
            fsum = max (fsum, sumi)
        return fsum