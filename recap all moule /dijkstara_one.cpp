#include<bits/stdc++.h>
using namespace std;
    typedef pair<int,int >pii;
    const int N = 1e3+7;
    const int INF = 1e9 + 7;
    vector<pii>g[N];
    vector<int>dis(N,INF);
    vector<bool>visited(N);
    void dijkstara(int source){
        priority_queue<pii, vector<pii>,greater<pii>> pq;
        dis[source] = 0;
        pq.push({0,source});
        while(!pq.empty()){
            int u = pq.top().second;
            pq.pop();
            visited[u] = true;
            for(pii vpair: g[u]){
                int v= vpair.first;
                int w = vpair.second;
                if(visited[v]) continue;
                if(dis[v] > dis[u]+w){
                    dis[v] = dis[u]+w;
                    pq.push({dis[v],v});
                }
            }
        }
    }
int main()
{
    int n,m;
    cin>>n>>m;
    while(m--)
    {
        int u,v,w;
        cin>>u>>v>>w;
        g[u].push_back({v,w});
        g[v].push_back({u,w});
    }
    int l,r;
    cin>>l>>r;
    dijkstara(l);
    if(dis[r] == INF){
        cout<<"no path exits"<<endl;
    }
    else{
        cout<<dis[r];
    }
}