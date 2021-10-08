'''
https://www.spoj.com/problems/PERIOD/

Solution: Find the length of border f[i] of s[:i+1]. Then period of s[:i+1] is i+1/(i+1-f[i])
if its an integer
'''



def border(w):
    n=len(w)
    f=[0 for i in range(n)]
    k=0
    for i in range(1,n):
        while w[k]!=w[i] and k>0:
            k=f[k-1]
        if w[k]==w[i]:
            k+=1
        f[i]=k
    return f

t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    f=border(s)
    print(f"Test case #{_+1}")
    for i in range(2,n+1):
        if i%(i-f[i-1])==0 and f[i-1]>0:
            print(i,i//(i-f[i-1]))
    
