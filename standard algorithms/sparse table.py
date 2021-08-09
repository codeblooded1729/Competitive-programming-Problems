'''
https://www.spoj.com/problems/RMQSQ/

Sparse Table for RMQ
'''

import math
import sys
sys.setrecursionlimit(1000000)
def ints():
    return map(int,input().split())


def make_table(arr,log2):
    ans=[[0 for i in range(log2+1)] for j in range(len(arr))]
    for i in range(len(arr)):
        ans[i][0]=arr[i]
    for j in range(1,log2+1):
        for i in range(len(arr)-(1<<j)+1):
            ans[i][j]=min(ans[i][j-1],ans[i+(1<<(j-1))][j-1])
    return ans

def query(ans,l,r):
    maxpow=int(math.log(r-l+1,2))
    return min(ans[l][maxpow],ans[r-(1<<maxpow)+1][maxpow])

n=int(input())
arr=list(ints())
log2=int(math.log(n,2))
ans=make_table(arr,log2)
q=int(input())
for _ in range(q):
    l,r=ints()
    print(query(ans,l,r))
