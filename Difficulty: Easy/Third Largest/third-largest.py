class Solution:
    def thirdLargest(self,arr):
        # code here
        if len(arr)<3:
            return -1
        f = 0
        s = 0
        t = 0
        
        for i in arr:
            if f<i:
                t=s
                s=f
                f=i
            elif s<i:
                t=s
                s=i
            elif t<i:
                t=i
        return t
        