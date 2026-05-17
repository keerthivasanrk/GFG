class Solution:
    def reverseexponentiation(self, n):
        # code here
        def revs(n,rev=0):
            if n==0:
                return rev
            return revs(n//10,n%10+rev*10)
        def pow(b,e):
            if e<1:
                return 1
            return b*pow(b,e-1)
            
        return pow(n,revs(n))
            