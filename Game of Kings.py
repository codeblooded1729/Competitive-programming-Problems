''''
https://vijos.org/p/1779
'''
'''
solution:
if l_i*r_i>l_{i+1}*r_{i+1} then we can swap them and max of (x_i,x_{i+1})
will not increase. Hence we can sort according to l_i*r_i and that will be
the order.
'''


def prod(tup):
    return tup[0]*tup[1]
n=int(input())
king=tuple(map(int,input().split()))
arr=[]
for _ in range(n):
    a,b=map(int,input().split())
    arr+=[(a,b)]
arr=sorted(arr,key=prod)
currmax=king[0]//arr[0][1]
left=king[0]
for i in range(1,n):
    left*=arr[i-1][0]
    currmax=max(left//arr[i][1],currmax)
print(int(currmax))
    
