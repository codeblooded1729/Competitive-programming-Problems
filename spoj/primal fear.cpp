#include <bits/stdc++.h>

using namespace std;


#define ll long long
#define all(x) (x).begin(), (x).end()
const int maxn=1000001;
int sieve[maxn];
int ans[maxn];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    fill(sieve,sieve+maxn,2);
    sieve[2]=1;
    sieve[3]=1;
    sieve[5]=1;
    sieve[7]=1;
    int curr=0;
    for(ll i=2;i<maxn;i++){
        if(sieve[i]){
            for(ll j=i*i;j<maxn;j+=i){
                sieve[j]=0;
            }
            if(sieve[i]==1){
                curr++;
            for(int p=1;p<10;p++){
                int nex=p*((int)(pow(10,ceil(log10(i)))))+i;
                if (nex<maxn && sieve[nex]==2) {
                    sieve[nex] = 1;
                }
            }
        }
        }
        ans[i]=curr;

    }
    int n,t;

    cin>>t;

    while(t--){
        cin>>n;
        cout<<ans[n]<<endl;
    }



}