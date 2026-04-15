class Solution:
    def thirdLargest(self,arr):
        # code here
        if len(arr)<3:
            return -1
        f = s = t = float('-inf')
        for i in arr:
            if i>f:
                t = s
                s = f
                f =i
            elif i>s:
                t = s
                s = i
            elif i>t:
                t =i
            else  :
                continue
        return t