class Solution:
    def rotateMatrix(self, k, mat):
        # code here
        if not mat or not mat[0]:
            return 0
        m = len(mat[0])
        k = k%m
        if k==0:
            return mat
        rm = []
        for row in mat:
            nr = row[k:]+row[:k]
            rm.append(nr)
        return rm
