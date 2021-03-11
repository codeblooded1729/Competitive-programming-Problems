/*
https://atcoder.jp/contests/abc187/tasks/abc187_f

Solution:

Just the chromatic number of complement. Use the implementation here https://codeforces.com/blog/entry/57496


*/


#include <bits/stdc++.h>

using namespace std;

#define ll long long
ll a,b,n,m,adj[18],dp[1<<18],s[1<<18];
int chrom(){
    ll al=1<<n;
    ll bigp=1077563119;
    dp[0]=1;
    for(ll i=0;i<al;i++){
        if ((n-__builtin_popcount(i))%2){
            s[i]=1;
        }
        else{
            s[i]=-1;
        }
    }
    for(ll i=1;i<al;i++){
        int ctz = __builtin_ctz(i);
        dp[i]=dp[i-(1<<ctz)]+dp[(i-(1<<ctz))&adj[ctz]];
        dp[i]=dp[i]%bigp;
    }
    for(int k=1;k<n;k++){
        int ans=0;
        for(ll i=0;i<al;i++){
            s[i]=s[i]*dp[i];
            ans=ans+s[i];
        }
        if(ans!=0){
            return k;
        }
    }
    return n;
}
int main() {
    cin>>n>>m;
    memset(adj,0,sizeof(adj));
    for(int i=0;i<m;i++){
        cin>>a>>b;
        a=a-1;
        b=b-1;
        adj[a]|=1<<b;
        adj[b]|=1<<a;
    }
    cout<<chrom()<<endl;
    return 0;
}