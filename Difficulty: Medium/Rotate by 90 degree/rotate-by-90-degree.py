class Solution:
    def rotateMatrix(self, mat):
        # code here
        n = len(mat)
        
        for i in range(n):
            for j in range(i+1,n):
                mat[i][j],mat[j][i] =mat[j][i],mat[i][j]
        
        for j in range(n):
            t,b = 0, n-1
            while t<=b:
                mat[t][j],mat[b][j] = mat[b][j],mat[t][j]
                t+=1
                b-=1
        return mat