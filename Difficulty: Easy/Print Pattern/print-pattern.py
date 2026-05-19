class Solution:
    def pattern(self, n,res=None):
        if res is None:
            res = []
        res.append(n)
        if n>0:
            
            self.pattern(n-5,res)
            res.append(n)
        return res
        