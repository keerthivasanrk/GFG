class Solution:
    def hasTripletSum(self, arr, target):
        # Code Here
        if len(arr)<3:
            return False
		arr.sort()
		
		for i in range(len(arr)-2):
		    l = i+1
		    r = len(arr)-1
		    
		    while l<r:
		    
    		    s = arr[i]+arr[l] + arr[r]
    		    
    		    if s<target:
    		        l+=1
    		    elif s>target:
    		        r-=1
    		    else:
    		        return True
    		        
		        