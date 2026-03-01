class Solution:
    def sort012(self, arr):
        # code here
        f=0
        m=0
        r=len(arr)-1
        
        while m<=r:
            if arr[m]==0:
                arr[f],arr[m]=arr[m],arr[f]
                f+=1
                m+=1
            elif arr[m]==1:
                m+=1
            else:
                arr[r],arr[m]=arr[m],arr[r]
                r-=1
        return arr
                
            
            
        