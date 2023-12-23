#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
const int inf = 1e9;
const int N = 1e3;
vector<pii>g[N];
vector<int> dis(N,inf);
vector<bool>visited(N);
void dijkstra(int source){
    priority_queue<pii,vector<pii>,greater<pii>>pq;
    dis[source] = 0;
    pq.push({0,source});
    while(!pq.empty()){
        int u= pq.top().second;
        pq.pop();
        visited[u] = true;
        for(pii vpair : g[u]){
            int v=vpair.first;
            int w=vpair.second;
            if(visited[v] )continue;
            if(dis[v] > dis[u]+w){
                dis[v] = dis[u]+w;
                pq.push({dis[v] ,v});
            }
        }
    }
}
int main()
{
    int n,m;
    cin>>n>>m;
    for(int i=0;i<m;i++){
        int u,v,w;
        cin>>u>>v>>w;
        g[u].push_back({v,w});
        g[v].push_back({u,w});
    }
    dijkstra(1);
    for(int i=1;i<=n;i++){
        cout<<dis[i]<<" ";
    }
    return 0;
}
