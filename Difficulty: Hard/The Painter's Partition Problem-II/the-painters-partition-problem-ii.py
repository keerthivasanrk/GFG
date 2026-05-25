class Solution:
    def p(self,arr,k,m):
        pc =1
        s = 0
        for i in arr:
            if i+s>m:
                pc+=1
                s = i
                if pc>k:
                    return False
            else :
                s+=i
        return True
    def minTime (self, arr, k):
        # code here
        l = max(arr)
        h = sum(arr)
        while l<=h:
            m = (l+h)//2
            if self.p(arr,k,m):
                ans = m
                h = m-1
            else:
                l = m+1
        return ans