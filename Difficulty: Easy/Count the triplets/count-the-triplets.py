class Solution:
	def countTriplet(self, arr):
		# code here
		arr.sort()
		
	
		count =0
		for i in range(len(arr)-1,-1,-1):
		    l=0
		    r=i-1
	
    		while l<r:
    		    s = arr[l] + arr[r]
    		    if arr[i]==s :
    		        count+=1
    		        l+=1
    		        r-=1
    		    elif s<arr[i]:
    		        l+=1
    		    else:
    		        r-=1
		return count