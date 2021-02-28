# https://codeforces.com/contest/464/problem/C
'''
solution:
Process the queries from last to first to find where a digit gets substituted
into. Keep v[x] and d[x], which are values and number of digits of the number
x gets substituted into.
'''


mod=pow(10,9)+7
def sub_and_eval(n):
    if n=='':
        return 0
    ans=v[int(n[0])]
    for i in range(1,len(n)):
        ans=(d[int(n[i])]*ans+v[int(n[i])])%mod
    return ans
def prod_d(n):
    ans=1
    for e in n:
        ans=ans*d[int(e)]%mod
    return ans
s=input()
v={i:i for i in range(10)}
d={i:10 for i in range(10)}
 
k=int(input())
arr=[]
for _ in range(k):
    a,b=input().split('->')
    arr.append((a,b))
for a,b in reversed(arr):
    v[int(a)]=sub_and_eval(b)
    d[int(a)]=prod_d(b)
print(sub_and_eval(s))
