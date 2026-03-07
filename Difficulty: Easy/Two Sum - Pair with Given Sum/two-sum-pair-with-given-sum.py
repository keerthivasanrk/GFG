class Solution:
	def twoSum(self, arr, target):
		arr.sort()
		l=0
		r=len(arr)-1
		
		while l<r:
		    s = arr[l]+arr[r]
		    if s<target:
		        l+=1
		    elif s>target:
		        r-=1
		    else:
		        return True