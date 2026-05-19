class Solution:
    def findFloor(self, arr, x):
        # code here
        l,r = 0,len(arr)-1
        ln = -1
        while l<=r:
            m = (l+r)//2
            if arr[m]<=x:
                ln = m
                l = m+1
            else:
                r= m-1
        return ln
        