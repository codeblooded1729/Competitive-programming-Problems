#include <bits/stdc++.h>

using namespace std;
int n;
vector<int> v;
int LIS(vector<int> &v, int n){
    vector<int> d(n+1,200005);
    for(int i=0;i<n;i++){
        *upper_bound(d.begin(),d.end(),v[i])=v[i];
    }
    for(int i=0;i<n;i++){
        if(d[i]==200005){
            return i;
        }
    }
}
int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cin>>n;
    for(int i=0;i<n;i++){
        int x;cin>>x;
        v.push_back(x);
    }
    cout<<LIS(v,n)<<endl;

}