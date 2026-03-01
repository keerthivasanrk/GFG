#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        count = 0
        b=n
        while b>0:
            a = b%10
            b//=10
            if a == 0:
                continue
            if n%a==0:
                count+=1
            
        return count