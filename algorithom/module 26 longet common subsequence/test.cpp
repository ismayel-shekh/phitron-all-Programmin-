#include<bits/stdc++.h>
using namespace std;

const int N = 1e5 + 7;
int dp[N];

bool fun(int n, int target) {
    if (target == n) return true;
    if (n < target) return false;
    if (dp[target] != -1) return dp[target];//corret line
    // if (dp[target]) return true;

    int option1 = fun(n, target + 3);
    int option2 = fun(n, target * 2);
    
    // if (option1 || option2) {
    //     dp[target] = true;
    //     return true;
    // }
    return dp[target] =(option1 || option2);
    

}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;

        memset(dp, -1, sizeof(dp));
        
        if (fun(n, 1))
            cout << "YES"<<endl;
        else
            cout << "NO"<<endl;
    }

    return 0;
}