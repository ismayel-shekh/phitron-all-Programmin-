#include<bits/stdc++.h>
using namespace std;

class edge{
    public:
        int u,v,w;
        edge(int u, int v, int w)
        {
            this -> u = u; this -> v = v; this -> w = w;
        }
};
const int N = 1e3;
int main()
{
    bool worked[N][N];
    int numberOfNode; cin >> numberOfNode; int numberOfEdge; cin >> numberOfEdge;
    vector<int>dist(numberOfNode+1, INT_MAX);
    map<pair<int,int>,int> mp; // first pair for vertex A to vertex B 

    vector<edge>v;
    for(int i = 0; i< numberOfEdge; i++)
    {
        int a, b, c;
        cin >> a >> b >> c;
        if(worked[a][b])
        {
            int index = mp[{a,b}];
            int value = min(v[index].w,c);
            edge e(a,b,value);
            v[index] = e;
        }
        else
        {
            worked[a][b] = true;
 
            edge ed(a,b,c);
            v.push_back(ed);
            mp[{a,b}] = v.size() - 1;
        }
    }

    dist[1] = 0;

    for (int i = 1; i <= numberOfNode - 1; i++)
        {
        for (int j = 0; j < v.size(); j++)
            {
                edge ed = v[j];
                int a = ed.u;
                int b = ed.v;
                int w = ed.w;
                if (dist[a] + w < dist[b])
                {
                    dist[b] = dist[a] + w;
                }
            }
    }



    for(int i = 1; i<= numberOfNode; i++)
    {
        if(dist[i] != INT_MAX) cout <<dist[i] << " ";
        else cout << 30000 << " ";
    }
    return 0;
}