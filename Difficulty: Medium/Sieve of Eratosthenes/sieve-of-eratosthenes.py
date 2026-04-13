class Solution:
    def sieve(self, n):
        # code here 
        prime = [True for _ in range(n+1)]
        prime[0],prime[1] = False, False
        res = []
        
        for i in range (2,int(n**0.5)+1):
            for j in range (2*i,n+1,i):
                prime[j]=False
        for i,p in enumerate(prime):
            if p==True:
                res.append(i)
        return res
        
