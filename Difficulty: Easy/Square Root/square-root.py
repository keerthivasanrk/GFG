class Solution:
    def floorSqrt(self, n): 
        # code here
        if n<2:
            return n
            
        l=0
        r=n
        ans = 0
        while l<=r:
            
            mid = (l+r)//2
            
            if mid * mid <= n:
                ans = mid
                l =mid+1
            else:
                 r -=1
        return ans
        