#include<bits/stdc++.h>
using namespace std;
int main()
{
    int test;
    cin>>test;
    while(test--)
    {
        string s;
        cin>>s;

            int c =0;
            if(s[0] == 'a') c++;
            if(s[1] == 'b') c++;
            if(s[2] == 'c') c++;
            if(c >= 1) cout<<"YES"<<endl;
            else cout<<"NO"<<endl;
         
         
    }
    return 0;
}