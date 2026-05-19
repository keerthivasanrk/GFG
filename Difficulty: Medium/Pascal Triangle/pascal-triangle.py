class Solution:
	def nthRowOfPascalTriangle(self, n):
	    # code here
	    mod = 10**9 +7
	    r = [1]
	    for i in range(1,n):
	        nr = [1]*(1+i)
	        for j in range(1,i):
	            nr[j] = (r[j-1]+r[j]) % mod
	        r = nr
	    return r