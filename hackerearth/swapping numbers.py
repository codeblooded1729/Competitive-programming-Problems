'''
https://www.hackerearth.com/practice/data-structures/advanced-data-structures/fenwick-binary-indexed-trees/practice-problems/algorithm/move-minimization-8a9d3991/

Solution:
We use the fact that the pair that when swapped gives min inversion is argmin(a[i]-i),argmax(a[i]-i]).
'''

def inv(arr):
    if len(arr)==1:
        return 0,arr
    c1,arr1=inv(arr[:len(arr)//2])
    c2,arr2=inv(arr[len(arr)//2:])
    new=[]
    m,n=len(arr1),len(arr2)
    i,j=0,0
    while i<m and j<n:
        if arr1[i]<arr2[j]:
            new.append(arr1[i])
            i+=1
        else:
            new.append(arr2[j])
            j+=1
            c1+=m-i
    if i==m:
        new.extend(arr2[j:])
    if j==n:
        new.extend(arr1[i:])
    return c1+c2,new


n=int(input())
arr=list(map(int,input().split()))
currmin=float("inf")
currmax=-float("inf")
indi,indj=0,0
for i in range(n):
    if arr[i]-i<currmin:
        indi=i
        currmin=arr[i]-i
    if arr[i]-i>currmax:
        indj=i
        currmax=arr[i]-i
if indi==indj:
    print(0)
else:
    arr[indi],arr[indj]=arr[indj],arr[indi]
    print(inv(arr))
