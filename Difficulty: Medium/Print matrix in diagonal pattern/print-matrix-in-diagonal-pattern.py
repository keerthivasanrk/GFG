# Your task is to complete this function
from collections import defaultdict
class Solution:
    def matrixDiagonally(self,mat):
        # code here
        if not mat:
            return 0
        dig = defaultdict(list)
        for r in range(len(mat)):
            for c in range(len(mat[0])):
                dig[r+c].append(mat[r][c])
        res = []
        for s in range(len(mat)+len(mat[0])-1):
            if s%2==0:
                res.extend(dig[s][::-1])
            else:
                res.extend(dig[s])
        return res