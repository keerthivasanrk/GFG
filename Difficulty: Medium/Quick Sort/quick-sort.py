class Solution:
    
    def quickSort(self, arr, low, high):
        if low < high:
            
            p_idx = self.partition(arr, low, high)
            
            
            self.quickSort(arr, low, p_idx - 1)
            self.quickSort(arr, p_idx + 1, high)
    
    def partition(self, arr, low, high):
       
        pivot = arr[high]
        
       
        i = low - 1
        
        for j in range(low, high):
            
            if arr[j] <= pivot:
                i += 1
                
                arr[i], arr[j] = arr[j], arr[i]
                
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
