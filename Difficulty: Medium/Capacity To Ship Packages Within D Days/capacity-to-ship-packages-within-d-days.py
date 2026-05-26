class Solution:
    def isvalid(self,arr,D,m):
        bc = 0
        k =1
        for i in arr:
            if i+bc > m:
                bc = i
                k+=1
                if k>D:
                    return False
            else:
                bc+=i
        return True
    def leastWeightCapacity(self, arr, D):
        # code here
        l = max(arr)
        h = sum(arr)
        ans = -1
        while l<=h:
            m = (l+h)//2
            if self.isvalid(arr,D,m):
                ans = m
                h = m-1
            else:
                l =m+1
        return ans