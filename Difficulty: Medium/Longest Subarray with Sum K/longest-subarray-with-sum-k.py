class Solution:
    def longestSubarray(self, arr, k):  
        s = 0 
        m = 0
        seen = {}
        
        for i in range (len(arr)):
            s+=arr[i]
            if s==k:
                m = i+1
            if s-k  in seen:
                m = max(m , i-seen[s-k])
            if s not in seen:
                seen[s]=i
        return m