#include<bits/stdc++.h>
using namespace std;
int main(){
    int test;cin>>test;
    cin.ignore();
    while(test--){
        string s;
        getline(cin,s);
        string word;
        stringstream ss(s);
        map<string,int>mp;
        int l=0;
        string m;
        while(ss>>word){
            mp[word]++;
            if(mp[word] > l){
                l=mp[word];
                m = word;
            }
        }
        cout<<m<<" "<<l<<endl;
    }
    return 0;
}