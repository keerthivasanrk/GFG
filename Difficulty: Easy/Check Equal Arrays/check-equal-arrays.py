class Solution:
    def checkEqual(self, a, b) -> bool:
        #code here
        if len(a)!=len(b):
            return False
         
        fr ={}
        f={}
        
           
        for i in a :
            fr[i]= fr.get(i,0)+1
            
        for i in b :
            f[i]= f.get(i,0)+1
            
        return fr ==f