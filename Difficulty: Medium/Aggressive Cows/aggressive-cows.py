class Solution:
    def pc(self,stalls,k,mi):
        pv = stalls[0]
        c = 1
        for i in range(1,len(stalls)):
            if stalls[i]-pv >=mi:
                c+=1
                pv = stalls[i]
                if c>=k:
                    return True
        return False
    
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        l,h = 1, stalls[-1]-stalls[0]
        ans = 0
        while l<=h:
            m = (l+h)//2
            if self.pc(stalls,k,m):
                ans = m
                l = m+1
            else:
                h = m-1
        return ans
            
            
        