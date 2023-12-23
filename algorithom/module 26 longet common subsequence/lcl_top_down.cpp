#include <bits/stdc++.h>
using namespace std;
int dp[1005][1005];
int ics(string a,int n,string b,int m){
    if(m==0 || n==0) return 0;
    if(dp[n][m] != -1) return dp[n][m];
    if(a[n-1] == b[m-1]){
        int ans=ics(a,n-1,b,m-1);
        return dp[n][m] = ans+1;
    }
    else{
        int ans1 = ics(a,n-1,b,m);
        int ans2 = ics(a,n,b,m-1);
        return dp[n][m] = max(ans1,ans2);
    }
}
int main()
{
    string a,b;
    cin>>a>>b;
    memset(dp,-1,sizeof(dp));
    cout<<ics(a,a.size(),b,b.size());
    return 0;
}
