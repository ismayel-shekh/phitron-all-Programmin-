#include <bits/stdc++.h>
using namespace std;
class edge
{
    public:
    int a,b,w;
    edge(int a,int b,int w){
        this->a = a;
        this->b = b;
        this->w = w;
    }
};
bool cmp(edge a, edge b){
    return a.w < b.w;
}
const int N = 1e5 +5;
int parent[N];
int parentsize[N];
void dsu_set(int n){
    for(int i=1;i<=n;i++){
        parent[i] = -1;
        parentsize[i] = 1;
    }
}
int dsu_find(int node){
    while(parent[node] != -1){
        node = parent[node];
    }
    return node;
}
void dsu_union(int a,int b){
    int leaderA = dsu_find(a);
    int leaderB = dsu_find(b);
    if(leaderA != leaderB) 
    {
        if(parentsize[leaderA] > parentsize[leaderB])
        {
            parent[leaderB] = leaderA;
            parentsize[leaderA] += parentsize[leaderB];
        }
        else
        {
            parent[leaderA] = leaderB;
            parentsize[leaderB] += parentsize[leaderA];
        }
    }
}
int main()
{
    int n,e;
    cin>>n>>e;
    vector<edge>v;
    vector<edge>ans;
    dsu_set(n);
    while(e--){
        int a,b,w;
        cin>>a>>b>>w;
        v.push_back(edge(a,b,w));
    }
    sort(v.begin(),v.end(),cmp);
    for(edge val : v )
    {
        int a = val.a;
        int b = val.b;
        int w = val.w;
        int leaderA = dsu_find(a);
        int leaderB = dsu_find(b);
        if(leaderA == leaderB) continue;
        ans.push_back(val);
        dsu_union(a,b);
        for(edge val : ans)
        {
            cout<<val.a << " "<<val.b<<" "<<val.w<<endl;
        }
    }
    return 0;
}
