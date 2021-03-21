/*
https://www.spoj.com/problems/LCA/
*/

#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define all(x) (x).begin(), (x).end()
vector<tuple<int,int,int>> circs;
int n,m,child,timer,l,q,tin[1005],tout[1005],up[1005][10];
vector<int>adj[1005];
void dfs(int v, int p){
    tin[v]=++timer;
    up[v][0]=p;
    for(int i=1;i<=l;i++){
        up[v][i]=up[up[v][i-1]][i-1];
    }
    for(int nbr:adj[v]){
        if(nbr!=p){
            dfs(nbr,v);
        }
    }
    tout[v]=++timer;
}

bool is_anc(int u,int v){
    return tin[u]<=tin[v]&&tout[u]>=tout[v];
}
int lca(int u, int v){
    if(is_anc(u,v)){
        return u;
    }
    if(is_anc(v,u)){
        return v;
    }
    for(int i=l;i>=0;--i){
        if(!is_anc(up[u][i],v)){
            u=up[u][i];
        }
    }
    return up[u][0];
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin>>t;
    int cas=1;
    while(t--){
        cin>>n;
        for(int i=1;i<=n;i++){
            adj[i].clear();
        }
        for(int i=1;i<=n;i++){
            cin>>m;
            while(m--){
                cin>>child;
                adj[i].push_back(child);
            }
        }
        timer=0;
        l=ceil(log2(n));
        dfs(1,1);
        cin>>q;
        cout<<"Case "<<cas<<":"<<endl;
        cas+=1;
        while(q--){
            int u,v;
            cin>>u>>v;
            cout<<lca(u,v)<<endl;
        }

    }
    return 0;
}