class Solution:
    def maxWater(self, arr):
        # code here
        l=0
        r = len(arr)-1
        lmax = 0
        rmax=0
        s = 0
        
        while l<r:
            if arr[l]<arr[r]:
                if arr[l]>=lmax:
                    lmax = arr[l]
                else:
                    s+=lmax-arr[l]
                l+=1
            else:
                if arr[r]>=rmax:
                    rmax=arr[r]
                else:
                    s+=rmax-arr[r]
                r-=1
        return s