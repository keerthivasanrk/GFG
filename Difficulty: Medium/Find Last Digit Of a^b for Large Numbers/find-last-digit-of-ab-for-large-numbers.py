#User function Template for python3

class Solution:
    def getLastDigit(self, a, b):
        # code here 
        if b == "0":
            return 1
        lastd = int(a[-1])
        cycles = {
            0: [0],
            1: [1],
            2: [2, 4, 8, 6],
            3: [3, 9, 7, 1],
            4: [4, 6],
            5: [5],
            6: [6],
            7: [7, 9, 3, 1],
            8: [8, 4, 2, 6],
            9: [9, 1]
        }
        
        cycle = cycles[lastd]
        k = len(cycle)
        r = int(b) % k
        if r==0:
            r = k
        return cycle[r-1]