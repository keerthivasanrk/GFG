class Solution:
    def frequencyCount(self, arr):
        #  code here
       
        n = len(arr)
        r = [0]*n
        
        for i in arr:
            r[i-1]+=1
        return r
                    
        

