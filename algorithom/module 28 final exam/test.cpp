#include<bits/stdc++.h>
using namespace std;
const int N = 1e5+7;
const int INF = 1e9;
 
bool vis[N];
 
int main()
{
 
int n,e;
cin>>n>>e;
long long dis[n+1][n+1];
for(int i=1; i<=n; i++){
    for(int j=0; j<=n; j++){
        dis[i][j] = INF;1
        if(i==j) dis[i][j] = 0;
    }
}
 
 
while(e--){
  long long  a,b,w; cin>>a>>b>>w;
    dis[a][b] = w;
}
 
  for (int k = 1; k <= n; k++)
    {
        for (int i = 1; i <= n; i++)
        {
            for (int j = 1; j <= n; j++)
            {  
               if (dis[i][k] !=  INF && dis[k][j] != INF) {
                dis[i][j] = min(dis[i][j], dis[i][k] + dis[k][j]);
                }
            }
        }
    }
 
int tt;
cin>>tt; 
while(tt--){
    long long int x,y; cin>>x>>y;
 
    if(dis[x][y] != INF ){
        cout<<dis[x][y]<<endl;
    }
    else{
        cout<<-1<<endl;
    }
}
 
    return 0;
}
 
 
 
 
 