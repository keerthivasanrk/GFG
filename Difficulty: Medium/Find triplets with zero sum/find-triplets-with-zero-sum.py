class Solution:
    def findTriplets(self, arr):
        #code here
        arr.sort()
        for i in range(len(arr)-2):
            l = i+1
            r = len(arr)-1
            
            while l<r:
                s = arr[i]+arr[l]+arr[r]
                if s==0:
                    return True
                    
                elif s>0:
                    r-=1
                else:
                    l+=1
                        