#include <bits/stdc++.h>
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
void print_norlmal(node *head){
    node *temp = head;
    while(temp != NULL){
        cout<<temp->val <<" ";
        temp= temp->next;

    }
    cout<<endl;
}
void insert_tail(node *& head,node *&tail,int val){
    node * newnode = new node(val);
    if(head == NULL){
        head = newnode;
        tail = newnode;
    }
    else{
        tail->next = newnode;
        newnode->prev = tail;
        tail = newnode;
    }
}
void print_reverse(node *tail){
    node *temp = tail;
    while(temp != NULL)
    {
        cout<<temp->val <<" ";
        temp = temp->prev;
    }
    cout<<endl;
}
int main()
{
    node* head = NULL;
    node* tail = NULL;
    int val;
    while(true){
        cin>>val;
        if(val == -1){
            break;
        }
        insert_tail(head,tail,val);
    }
    print_norlmal(head);
    print_reverse(tail);
    return 0;
}
