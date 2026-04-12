class Solution:
	def maxProduct(self,arr):
		# code here
		mx,mi = 1,1
		fr = arr[0]
		if not arr:
		    return 0
		for i in arr:
		    if i ==0:
		        mx , mi = 1,1
		        fr = max(fr,0)
		        continue
		    t = mx*i
		    mx = max(mx*i,mi*i,i)
		    mi = min(t,mi*i,i)
		    fr = max(fr,mx)
		return fr