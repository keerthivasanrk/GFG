class Solution:
    def getMinMax(self, arr):
        # code here
        min = arr[0]
        max = arr[0]
        for i in arr:
            if min>i:
                min = i
            if max < i:
                max = i
        return min,max