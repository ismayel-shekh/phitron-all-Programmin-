#include <bits/stdc++.h>
using namespace std;
int const N = 1e9;
vector<pair<int,int>>adj[N];
int main() {
    int n, e;
    cin >> n >> e;
    for (int i = 0; i < e; i++) {
        int a, b, w;
        cin >> a >> b >> w;
        adj[a].push_back({b, w});
    }
    vector<vector<int>> adjacencyMatrix(n + 1, vector<int>(n + 1, INT_MAX));
    for (int i = 1; i <= n; i++) {
        adjacencyMatrix[i][i] = 0; // No self-loops.
        for (const pair<int, int>& edge : adj[i]) {
            int j = edge.first; 
            int weight = edge.second; 
            adjacencyMatrix[i][j] = weight;
        }
    }
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (adjacencyMatrix[i][j] == INT_MAX) {
                cout << "INF\t";
            } else {
                cout << adjacencyMatrix[i][j] << "\t";
            }
        }
        cout << endl;
    }
    return 0;
}
