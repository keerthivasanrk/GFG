class Solution:
    def reverseexponentiation(self, n):
        # code here
        rev = 0
        o=n

        while n > 0:
            rev = rev * 10 + (n % 10)
            n //= 10
        rev = o**rev
        return rev