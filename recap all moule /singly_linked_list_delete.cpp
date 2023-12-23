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
void delete_node(node *head, int pos){
    node *temp = head;
    for(int i=1;i<= pos-1;i++){
        temp = temp->next;
    }
    node *deletenode = temp->next;
    temp->next = temp->next->next;
    delete deletenode;
}
void delete_head(node *&head){
    node *deletenode = head;
    head = head->next;
    delete deletenode;
}
void insert(node*& head,int val){
    node *newnode = new node(val);
    if(head == NULL){
        head = newnode;
    }
    else{
        node *temp = head;
        while(temp->next != NULL){
            temp=temp->next;
        }
        temp->next = newnode;
    }
}
void print(node * head){
    node * temp = head;
    while(temp != NULL){
         cout<<temp->val<<" ";
        temp = temp->next;
    }
}
int main()
{
    node* head = NULL;
    int val;
    while(true){
        cin>>val;
        if(val == -1) break;
        insert(head,val);
    }
    delete_node(head,3);
    delete_head(head);
    print(head);
    return 0;
}