#include <bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--){
        int n,x;
        cin>>n>>x;
        int s= 1000-x;
        int a[n];
        for(int i=0;i<n;i++){
            cin>>a[i];
        }
         int dp[n+1][s+1];
         dp[0][0] = 1;
         for(int i=1;i<=s;i++){
            dp[0][i] = 0;
         }
         for(int i=1;i<=n;i++){
            for(int j=0;j<=s;j++){
                if(a[i-1] <= j){
                    dp[i][j] = dp[i][j-a[i-1]] + dp[i-1][j];
                }
                else dp[i][j] = dp[i-1][j];
            }
         }
         if(dp[n][s]) cout<<"YES"<<endl;
         else{
            cout<<"NO"<<endl;
         }
    }

    return 0;
}
