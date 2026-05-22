class Solution:
    def searchMatrix(self, mat, x): 
    	# code here 
    	m,n = len(mat), len(mat[0])
    	l,r = 0, (m*n) -1
    	
    	while l<=r:
    	    mi = (l+r)//2
    	    ro,co = mi//n,mi%n
    	    if mat[ro][co]==x:
    	        return True
    	    elif mat[ro][co]<x:
    	        l = mi+1
    	    else:
    	        r = mi-1
        return False
    	        
    	       
    	
    	
