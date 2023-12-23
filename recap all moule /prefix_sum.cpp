#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int pre[n];
    pre[0] = a[0];
    for(int i=1;i<n;i++){
        pre[i] = a[i]+pre[i-1];
    }
    int sum = pre[4] - pre[2];
    cout<<sum; 
    return 0;
}
