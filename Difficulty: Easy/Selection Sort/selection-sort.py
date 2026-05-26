class Solution: 
    def selectionSort(self, arr):
        #code herew
        for i in range(len(arr)):
            mi = i
            for j in range(i+1,len(arr)):
                if arr[j]<arr[mi]:
                    mi = j
            arr[i],arr[mi] = arr[mi],arr[i]
        return arr