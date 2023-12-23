#include <bits/stdc++.h>
using namespace std;
int const N = 1e5;
vector<int>adj[N];
int hight[N];
bool visited[N];
void dps(int u){
    visited[u] = true;
    for(int v : adj[u]){
        if(!visited[v]){
            dps(v);
            hight[u] = max(hight[u],hight[v]+1);
        }
    }
}
int main()
{
    int n,m;
    cin>>n>>m;
    for(int i=0;i<m;i++){
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    dps(1);
    int x = 0;
    for(int i=1;i<=n;i++){
        // cout<<hight[i]<<" ";
        x=max(x,hight[i]);
    }
    cout<<x;
    return 0;
}
