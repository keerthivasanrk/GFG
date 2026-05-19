class Solution:
    def find(self, arr, x):
        # code here
        res = [-1,-1]
        l,r = 0,len(arr)-1
        
        while l<=r:
            m = (l+r)//2
            if arr[m]==x:
                res[0]=m
                r=m-1
            elif arr[m]<x:
                l=m+1
            else:
                r=m-1
                
        l,r = 0,len(arr)-1
        
        while l<=r:
            m = (l+r)//2
            if arr[m]==x:
                res[1]=m
                l=m+1
            elif arr[m]<x:
                l=m+1
            else:
                r=m-1
        return res
                    