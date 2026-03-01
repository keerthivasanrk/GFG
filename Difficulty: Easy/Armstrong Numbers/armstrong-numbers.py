#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        # code here
        a,o=0,n
        d = len(str(n))
        while n>0:
            a = a + ((n%10)**d)
            n//=10
        return a==o 