class Solution:
    def binarySearch(self, arr, k):
        # code here
        l,r=0,len(arr)-1
        while l<=r:
            m= (l+r)//2
            if arr[m]==k:
                return True
            elif arr[m]<k:
                l+=1
            else:
                r-=1
        else:
            return False