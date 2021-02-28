#http://bailian.openjudge.cn/practice/2811/
'''
solution:
Just brute force through all possible first rows and uniquely complete the matrix
We are done if matrix is all 0.
'''

def switch(arr,i,j):
    arr[i][j]^=1
    if i>=1:
        arr[i-1][j]^=1
    if i<=3:
        arr[i+1][j]^=1
    if j>=1:
        arr[i][j-1]^=1
    if j<=4:
        arr[i][j+1]^=1
def main():
    for n in range(2**6):
        out=[[0 for i in range(6)] for j in range(5)]
        out[0]=list(map(int,'{0:06b}'.format(n)))
        new=[[arr[i][j] for j in range(6)] for i in range(5)]
        for j in range(6):
            if out[0][j]==1:
                switch(new,0,j)
        for k in range(1,5):
             for j in range(6):
                 if new[k-1][j]==1:
                     switch(new,k,j)
                     out[k][j]=1
        if new[-1]!=[0,0,0,0,0,0]:
            continue
        return out
             
             
            
    
arr=[]
for _ in range(5):
    arr.append(list(map(int,input().split())))
fin=main()
for lis in fin:
    print(' '.join(map(str,lis)))
