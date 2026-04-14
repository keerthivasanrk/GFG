class Solution:
    def minRow(self,a):
        #code here
        mini = float ('inf')
        ans = 0
        for i in range(len(a)):
            cr = sum(a[i])
            if cr<mini:
                mini = cr
                ans = i+1
        
        return ans    