class Solution:
	def twoSum(self, arr, target):
		arr.sort()
		l=0
		r=len(arr)-1
		if len(arr)<2:
		    return False
		
		while l<r:
		    sum = arr[l] + arr[r]
		    if sum == target:
		        return True
		    elif sum<target:
		        l+=1
		    else:
		        r-=1
		        
	    else:
	        return False