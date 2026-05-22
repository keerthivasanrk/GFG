class Solution:
    def rowWithMax1s(self, arr):
        # code here
        m,n = len(arr), len(arr[0])
        maxi = 0
        c= 0
        index =0
        for i in range(m):
            for j in range(n):
                if arr[i][j] == 1:
                    c+=1
            
            if c>maxi:
                index =i
            c=0
        return index