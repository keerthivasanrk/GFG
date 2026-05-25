class Solution:
    def p(self,arr,k,m):
        sd = 1
        s = 0
        for i in arr:
            if s+i > m:
                sd+=1
                s = i
                if sd>k:
                    return False
            else:
                s+=i
        return True
    def splitArray(self, arr, k):
        # code here
        l = max(arr)
        h = sum(arr)
        while l<=h:
            m=(l+h)//2
            if self.p(arr,k,m):
                ans=m
                h = m-1
            else:
                l = m+1
        return ans
        