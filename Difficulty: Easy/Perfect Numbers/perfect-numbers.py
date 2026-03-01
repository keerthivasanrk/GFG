class Solution:
    def isPerfect(self, n):
        # code here 
        if n <2 :
            return n
        o = n    
        i = 2
        total = 1
        while i*i<=n:
            if n%i==0:
                total+=i
                if i!=n//i:
                    total += n//i
            i+=1
        return total == o
                    