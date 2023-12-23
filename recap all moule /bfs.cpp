#include <bits/stdc++.h>
using namespace std;
int const N = 1000;
vector<int> adj[N];
bool visited[N];
int level[N];
int bfs(int s){
    queue<int>q;
    level[s] = 0;
    q.push(s);
    int x =0;
    visited[s] = true;
    while(!q.empty()){
        int u = q.front();
        q.pop();
        for(int v: adj[u]){
            if(visited[v]) continue;
            q.push(v);
            visited[v] = true;
            level[v] = level[u]+1;
            x=max(x,level[v]);
        }
    }
    return x;
}
int main()
{
    int n,m;
    cin>>n>>n;
    for(int i=0;i<n;i++){
        int u,v;
        cin>>u>>v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }
    cout<<bfs(1);
    return 0;
}
