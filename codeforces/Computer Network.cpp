/*
https://codeforces.com/gym/100114 Computer Networks

Solution:
Find all the bridges in graph, and let the components formed after removing them form a tree.
Just find longest path u-->v in this tree, and join any two vertices in component u and v. 
*/


#include <bits/stdc++.h>

using namespace std;

#define ar array
#define ll long long
#define all(x) (x).begin(), (x).end()
int n,m,a,b;
vector<int> adj[10001],curr;
vector<vector<int>> ans;
set<pair<int,int>> doub,edges,forb;
bool visited[10001];
int tin[10001],low[10001];
int timer=0;

void dfs(int v, int p = -1) {
    visited[v] = true;
    tin[v] = low[v] = timer++;
    for (int to : adj[v]) {
        if (to == p) continue;
        if (visited[to]) {
            low[v] = min(low[v], tin[to]);
        } else {
            dfs(to, v);
            low[v] = min(low[v], low[to]);
            if (low[to] > tin[v])
                if(not doub.count(make_pair(to,v))){
                    forb.insert(make_pair(to,v));
                    forb.insert(make_pair(v,to));
                };
        }
    }
}
void conn(int v){
    curr.push_back(v);
    visited[v]=true;
    for(int nbr: adj[v]){
        if(not forb.count(make_pair(v,nbr)) && not visited[nbr]){
            conn(nbr);
        }
    }
}
int bfs(int v,int x,vector<int> nadj[]){
    bool vis[10001];
    memset(vis,false,sizeof(vis));
    queue<int> q;
    q.push(v);
    vis[v]=true;
    int ans=v;
    int curr;
    while(!q.empty()){
        curr=q.front();
        q.pop();
        for(int nbr:nadj[curr]){
            if (!vis[nbr]){
                q.push(nbr);
                vis[nbr]=true;
                ans=nbr;
            }
        }

    }
    return ans;
}

int main() {

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    cin>>n>>m;
    for(int i=0;i<m;i++){
        cin>>a>>b;
        if (edges.count(make_pair(a,b))){
            doub.insert(make_pair(a,b));
            doub.insert(make_pair(b,a));

        }
        else {
            edges.insert(make_pair(a,b));
            edges.insert(make_pair(b,a));
            adj[a].push_back(b);
            adj[b].push_back(a);

        }
    }
    memset(visited,false,sizeof(visited));

    dfs(1);

    memset(visited,false,sizeof(visited));
    for(int i=1;i<n+1;i++){
        if(not visited[i]){
            conn(i);
            ans.push_back(curr);
            curr.clear();
        }
    }

    int x=ans.size();
    int loc[10001];
    for(int i=0;i<x;i++){
        for(auto e: ans[i]){
            loc[e]=i;
        }
    }
    vector<int> nadj[10001];
    for(auto p: forb){
        nadj[loc[p.first]].push_back(loc[p.second]);
    }
    int u=bfs(0,x,nadj);
    int v=bfs(u,x,nadj);
    cout<<ans[u][0]<<' '<<ans[v][0]<<endl;
    return 0;

}