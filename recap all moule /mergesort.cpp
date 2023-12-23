#include <bits/stdc++.h>
using namespace std;
int const N = 1e5;
int ara[N];
void marge_sort(int l,int r,int mid){
    int left = (mid-l)+1;
    int L[left+1];
    int right = r-mid;
    int R[right];
    int k=0;
    for(int i=l;i<=mid;i++){
        L[k] = ara[i];
        k++;
    }
    k=0;
    for(int i=mid+1;i<=r;i++){
        R[k]=ara[i];
        k++;
    }
    L[left] = INT_MAX;
    R[right] = INT_MAX;
    int lp=0,rp=0;
    for(int i=l;i<=r;i++){
        if(L[lp] <= R[rp]){
            ara[i] = L[lp];
            lp++;
        }
        else{
            ara[i] = R[rp];
            rp++;
        }
    }
}
void marge(int l,int r){
    if(l==r) return;
    int mid = (l+r) / 2;
    marge(l,mid);
    marge(mid+1,r);
    marge_sort(l,r,mid);
}
int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++){
        cin>>ara[i];
    }
    marge(0,n-1);
    for(int i=0;i<n;i++){
        cout<<ara[i]<<" ";
    }
    return 0;
}
