class Solution:
    def myAtoi(self, s):
        # code here
        mini, maxi = -2**31, 2**31 - 1
        
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        index = 0
        if s[0] == '-':
            sign = -1
            index = 1
        elif s[0] == '+':
            sign = 1
            index = 1
            
        def res(idx, cur):
            # FIXED: Corrected index bound check and method name
            if idx == len(s) or not s[idx].isdigit():
                return cur * sign
            
            ns = cur * 10 + int(s[idx])
            
            if ns * sign < mini: return mini
            if ns * sign > maxi: return maxi
            
            return res(idx + 1, ns)
            
        return res(index, 0)
