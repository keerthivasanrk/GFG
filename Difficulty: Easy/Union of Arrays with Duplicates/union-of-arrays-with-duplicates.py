class Solution:    
    def findUnion(self, a, b):
        # code here
        a.sort()
        b.sort()
        c=0
        d=0
        ans=[]
        while c<len(a) and d<len(b):
            if a[c]<b[d]:
                if not ans or ans[-1]!=a[c]:
                    ans.append(a[c])
                c+=1
            elif a[c]>b[d]:
                if not ans or ans[-1]!=b[d]:
                    ans.append(b[d])
                d+=1
            else:
                if not ans or ans[-1]!=a[c]:
                    ans.append(b[d])
                c+=1
                d+=1
        while c<len(a):
            if ans[-1]!=a[c]:
                ans.append(a[c])
            c+=1
        while d<len(b):
            if ans[-1]!=b[d]:
                ans.append(b[d])
            d+=1
        return ans