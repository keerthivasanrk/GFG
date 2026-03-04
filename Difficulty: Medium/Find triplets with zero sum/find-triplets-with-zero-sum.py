class Solution:
    def findTriplets(self, arr):
        #code here
        for i in range(len(arr)-2):
            l = i+1
            arr.sort()
            r = len(arr)-1
            while l<r:
                s = arr[i]+arr[l]+arr[r]
                if s == 0:
                    return True
                elif s<0:
                    l+=1
                else:
                    r-=1
                    