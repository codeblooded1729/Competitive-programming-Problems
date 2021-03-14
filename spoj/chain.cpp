/*
https://www.spoj.com/problems/CHAIN/
Solution:
Keep a union find data structure. Also let r(s,parent[s]) be 0 if they are same species, 1 if 
s eats parent[s] and 2 if parent[s] eats s. Then we have r(a,b)+r(b,c)=r(a,c) mod 3. So  now given
an information about x,y if they belong to same component we can check if is true by checking sum
of r along the path root[x]--->x--->y--->root[x] is 0 mod 3 or not. I they are in different component, we 
find the relationship between root[x] and root[y] by using the transitivity and merge with appropriate
value of r[root[x],root[y]].
*/


#include <bits/stdc++.h>

using namespace std;
int t,d,n,m,k,x,y,ans,s,s1,s2,p;
map<pair<int,int>,int> r;
vector<int> parent;

tuple<int,int> find_set(int i){
    if(parent[i]==i){
        return make_tuple(i,0);
    }
    tie(p,s)=find_set(parent[i]);
    s=(s+r[{i,parent[i]}])%3;
    parent[i]=p;
    r[{i,parent[i]}]=s;
    return make_tuple(p,s);
}
int union_set(int x,int y, int d){
    tie(x,s1)=find_set(x);
    tie(y,s2)=find_set(y);
    if (x==y){
        if((s1-s2+d-1)%3){
            return 1;
        }
        else{
            return 0;
        }
    }
    else{
        parent[x]=y;
        r[{x,y}]=(s2-s1-d+1)%3;
        return 0;
    }
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>t;
    while (t--){
        cin>>n>>k;
        ans=0;
        parent.clear();
        r.clear();
        for(int i=0;i<n;i++){
            parent.push_back(i);
        }
        for(int i=0;i<k;i++){
            cin>>d>>x>>y;
            if(x>n||y>n){
                ans++;
            }
            else {
                ans = ans + union_set(x - 1, y - 1, d);
            }
        }
        cout<<ans<<endl;
    }

    return 0;
}