'''
https://atcoder.jp/contests/abc213/tasks/abc213_e

Solution: 0-1 BFS
'''


from collections import Counter,deque
from math import gcd



def bfs01(start):
    q=deque()
    q.append(start)
    dist={start:0}
    while q:
        curr=q.popleft()
        for nbr in graph[curr]:
            if nbr not in dist:
                if graph[curr][nbr]==0:
                    dist[nbr]=dist[curr]
                    q.appendleft(nbr)
                else:
                    dist[nbr]=dist[curr]+1
                    q.append(nbr)
                if nbr==(h-1,w-1):
                    return dist[nbr]
    return dist[(h-1,w-1)] 
h,w=map(int,input().split())
arr=[]
for i in range(h):
    arr.append(input())
graph={}

no=[(-2,-2),(-2,2),(2,2),(2,-2)]
for i in range(h):
    for j in range(w):
        graph[(i,j)]={}
        for k in range(-2,3):
            for l in range(-2,3):
                if 0<=i+k<h and 0<=j+l<w and (k,l) not in no and arr[i+k][j+l]=='#':
                    graph[(i,j)][(i+k,j+l)]=1
toadd=[(0,1),(0,-1),(1,0),(-1,0)]
for i in range(h):
    for j in range(w):
        for k,l in toadd:
            if 0<=i+k<h and 0<=j+l<w and arr[i+k][j+l]=='.':
                graph[(i,j)][(i+k,j+l)]=0

print(bfs01((0,0)))

            
