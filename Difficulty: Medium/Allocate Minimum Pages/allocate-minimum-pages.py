class Solution:
    def mp(self, mi, arr, k):
        sc = 1
        pc = 0
        for i in arr:
            if pc + i > mi:
                sc += 1
                pc = i
                if sc > k:
                    return False
            else:
                pc += i
        return True
        
    def findPages(self, arr, k):
        # Handle edge case where there are fewer books than students
        if len(arr) < k:
            return -1
            
        l, r = max(arr), sum(arr)
        ans = -1
        
        while l <= r:
            m = (l + r) // 2
            if self.mp(m, arr, k):
                ans = m
                r = m - 1  # Fixed: changed 'h' to 'r'
            else:
                l = m + 1
        return ans
