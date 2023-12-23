#include<bits/stdc++.h>
using namespace std;
class node
{
public:
    int val;
    node *next;
    node *prev;
    node(int val)
    {
        this->val = val;
        this->next = NULL;
        this->prev = NULL;
    }
};
void insert_tail(node*& head, node *& tail,int val){
    node* newnode = new node(val);
    if(head == NULL){
        head = newnode;
        tail = newnode;
    }
    tail->next = newnode;
    tail=newnode;
}
void print_reverse(node *head){
    if(head == NULL) return;
    print_reverse(head->next);
    cout<<head->val<<" ";
}
int main()
{
    node* head = NULL;
    node* tail = NULL;
    int n;
    while(true){
        cin>>n;
        if(n==-1) break;
        insert_tail(head,tail,n);
    }
    print_reverse(head);
    return 0;
}