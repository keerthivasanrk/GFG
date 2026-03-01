#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        f = {}
        for i in a:
            f[i]=f.get(i,0)+1
        
        for i in b:
            if i not in f or f[i]==0:
                return False
            f[i]-=1
        return True
    
    
    
    
