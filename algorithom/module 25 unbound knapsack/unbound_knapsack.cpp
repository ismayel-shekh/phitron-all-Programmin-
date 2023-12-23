#include<bits/stdc++.h>
using namespace std;
int dp[1005][1005];
int unbound_knpsack(int n,int s,int val[],int w[]){
    if(n==0 || s==0) return 0;
    if(dp[n][s] != -1) return dp[n][s];
    if(w[n-1] <= s) {
        int ch1 = val[n-1] + unbound_knpsack(n,s-w[n-1],val,w);
        int ch2 = unbound_knpsack(n-1,s,val,w);
        return dp[n][s] = max(ch1,ch2);
    } 
    else return dp[n][s] = unbound_knpsack(n-1,s,val,w);
}
int main(){
    int n,s;
    cin>>n>>s;
    int val[n],w[n];
    for(int i=0;i<=n;i++){
        for(int j=0;j<=s;j++){
            dp[i][j] = -1;
        }
    }
    for(int i=0;i<n;i++){
        cin>>val[i];
    }
    for(int i=0;i<n;i++){
        cin>>w[i];
    }
    cout<<unbound_knpsack(n,s,val,w);
    return 0;
}
