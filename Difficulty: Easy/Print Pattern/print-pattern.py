class Solution:
    def pattern(self, n):
        # code here
        
        res = []
        
        def com(cur):
            res.append(cur)
            if cur<=0:
                return
            com(cur-5)
            res.append(cur)
        com(n)
        return res