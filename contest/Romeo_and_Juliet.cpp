#include<bits/stdc++.h>
using namespace std;

const int N = 1e3+5;
vector<int> adj[N];
bool visited[N];
int level[N];
int parent[N];

void bfs(int s)
{
	queue<int> q;
	q.push(s);
	visited[s] = true;
	level[s] = 0;
	parent[s] = -1;

	while(!q.empty())
	{
		int u = q.front();
		q.pop();

		for(int v: adj[u])
		{
			if(visited[v] == true) continue;
			q.push(v);
			visited[v] = true;
			level[v] = level[u] + 1;
			parent[v] = u;
		}

	}
}

int main()
{


    int n,m;
    cin >> n >> m;

    for(int i=0;i<m;i++)
    {
    	int u,v;
    	cin >> u >> v;
    	adj[u].push_back(v);
    	adj[v].push_back(u);
    }

    int s,d,k;
    cin >> s >> d>>k;

    bfs(s); 

    // cout <<"Distance : "<< level[d] << endl;

    // //Path Finding O(n)
    vector<int> path;
    int current = d;
    while(current != -1)
    {
    	path.push_back(current);
    	current = parent[current];
    }
   int x = path.size();
    // reverse(path.begin(), path.end());

    // cout << "Path : ";
    // for(int node:path)
    // {
    // 	cout << node << " ";
    // }
    int l = x/k;
    if(x < k) cout<<"NO";
    else if(k+1 >= l){
        cout<<"YES";
    }
    else{
        cout<<"NO";
    }
 	return 0;
    
}