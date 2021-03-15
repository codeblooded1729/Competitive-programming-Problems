'''
https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/uhihuih/

Solution:
Process everything from end. Keep two Fenwick trees for following purpose:
1)find number of processed robots with less humour than than of ith robot
2)find sum of intel of above such robots

since intel,humour<=3x10^5, we can actually do the above. Now its easy to compute
personality index.
'''

def add(bit,p,x):
    while p<=300004:
        bit[p]+=x
        p+=p&-p

def query(bit,x):
    ans=0
    while x>0:
        ans+=bit[x]
        x-=x&-x
    return ans

n=int(input())
hum=[]
intel=[]
for _ in range(n):
    x,y=map(int,input().split())
    hum.append(x)
    intel.append(y)
bit1=[0 for i in range(300005)]
bit2=[0 for i in range(300005)]
ans=[]
curr=0
for i in range(n-1,-1,-1):
    less=query(bit1,hum[i]-1)
    sumless=query(bit2,hum[i]-1)
    ans+=[2*sumless-curr+(n-1-i-2*less)*intel[i]]
    add(bit1,hum[i],1)
    add(bit2,hum[i],intel[i])
    curr+=intel[i]
    
for e in reversed(ans):
    print(e)
