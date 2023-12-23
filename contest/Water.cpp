#include<bits/stdc++.h>
using namespace std;
int main()
{
   int t;
   cin>>t;
   while(t--){
    int n;
    cin>>n;
    int f=INT_MIN;
    int s= INT_MIN;
    int l,m;
    vector<int>v;
    for(int i=0;i<n;i++){
        int a;cin>>a;
        v.push_back(a);
    }

    for(int i=0;i<v.size();i++){
        if(v[i] > f){
            l=i;
            f=v[i];
        }
    }
    for(int i=0;i<v.size();i++){
        if(v[i] > s && v[i] < f){
            m=i;
            s=v[i];
        }
    }
    cout<<min(l,m)<< " "<<max(l,m)<<endl;
   }
    return 0;
}