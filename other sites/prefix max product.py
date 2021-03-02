#https://app.codility.com/programmers/task/prefix_max_product/
'''
solution:
Make an array f which stores the length of boundries of string s[:i]. Now a string
of length i is a boundry of s[:j+1] iff iterating f again and again from position j gives i.
So we can make a graph where i-->j if i=f[j-1]. Then number of substring with prefix s[:i+1] is
exactly all the descendents of i. By using dp idea, we memoiz the array ans from bottom to top
and then we have to only add values of neighbors of i.
'''
s=input()
n=len(s)
f=[0]*n
k=0
for i in range(1,n):
    while s[i]!=s[k] and k>0:
        k=f[k-1]
    if s[i]==s[k]:
        k+=1
    f[i]=k

ans=[1 for i in range(n+1)]
for i in range(n-1,-1,-1):
    ans[f[i]]+=ans[i+1]
print(max(i*ans[i] for i in range(1,n+1)))

            
            
    
