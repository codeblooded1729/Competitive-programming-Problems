'''
https://codeforces.com/problemset/problem/126/B

Solution: Compute array z as Z function of the string. Then we just need to find
an element z[i] such that z[i]=n-i and z[i]<max(z) or z[i]==max(z) and count(z[i])>=2 

'''


def Z(s):
    n=len(s)
    z=[0 for i in range(n)]
    l,r=0,0
    for i in range(1,n):
        if i>r:
            l=r=i
            while r<n and s[r-l]==s[r]:
                r+=1
            z[i]=r-l
            r-=1
        else:
            k=i-l
            if z[k]<r-i+1:
                z[i]=z[k]
            else:
                l=i
                while r<n and s[r-l]==s[r]:
                    r+=1
                z[i]=r-l
                r-=1
    return z

s=input()
n=len(s)
z=Z(s)
m=max(z)
e=-float("inf")
count={i:0 for i in z}
for i in range(1,n):
    if z[i]==n-i:
        if z[i]<m or (z[i]==m and count[z[i]]>0):
            e=max(z[i],e)
    count[z[i]]+=1   
    
if e!=-float("inf"):
    print(s[-e:])
else:
    print("Just a legend")

    
