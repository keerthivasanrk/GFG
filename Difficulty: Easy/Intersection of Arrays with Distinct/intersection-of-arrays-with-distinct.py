class Solution:
    def intersectSize(self,a, b):
        # code here
        a.sort()
        b.sort()
        
        i =0 
        j =0 
        count = 0
        
        while i<len(a) and j<len(b):
            if a[i]<b[j]:
                i+=1
            elif a[i]>b[j]:
                j+=1
            else:
                count+=1
                i+=1
                j+=1
            
        return count
                
