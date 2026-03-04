class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        if len(arr)<3:
		    return False
		arr.sort()
		for i in range (len(arr)-1):
		    
    		l=i+1
    		r=len(arr)-1
    		
    		
    		while (l<r):
    		    sum = arr[l] + arr[r] + arr[i]
    		    if sum == target:
    		        return True
    		    elif sum<target:
    		        l+=1
    		        
    		    else:
    		        r-=1
    	return False
    		        
    	