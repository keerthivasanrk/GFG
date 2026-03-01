class Solution:
    def isPrime(self, n):
        # code here
        if n<2:
            return False
        i=2
        while i*i<=n:
            if n%i==0:
                return False
            i+=1
        return True