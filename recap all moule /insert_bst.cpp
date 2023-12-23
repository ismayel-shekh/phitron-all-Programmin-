#include<bits/stdc++.h>
using namespace std;
class node
{
public:
    int val;
    node *left;
    node *right;
    node(int val)
    {
        this->val = val;
        this->left = NULL;
        this->right = NULL;
    }
};
node *input_tree(){
    int val;
    cin>>val;
    node * root;
    if(val == -1) root =NULL;
    else root = new node(val);
    queue<node* >q;
    if(root) q.push(root);
    while(!q.empty()){
        node* p = q.front();
        q.pop();
        int l,r;
        cin>>l>>r;
        node *myleft;
        node* myright;
        if(l==-1) myleft = NULL;
        else myleft = new node(l);
        if(r==-1) myright = NULL;
        else myright = new node(r);
        p->left = myleft;
        p->right = myright;
        if(p->left) q.push(p->left);
        if(p->right) q.push(p->right);
    }
    return root;
}
void level_order(node *root){
    if(root == NULL) {
        cout<<"tree nhi"<<endl;
        return;
    }
    queue <node* >q;
    q.push(root);
    while(!q.empty()){
        node* f = q.front();
        q.pop();
        cout<<f->val <<" ";
        if(f->left) q.push(f->left);
        if(f->right) q.push(f->right);
    }
}
void insert(node*& root,int x){
    if(root == NULL) {
        root = new node(x);
        return;
    }
    if(x < root->val) {
        if(root->left == NULL){
            root->left = new node(x);
        }
        else{
            insert(root->left,x);
        }
    }
    else{
        if(root->right == NULL){
            root->right = new node(x);
        }
        else{
            insert(root->right,x);
        }
    }
}
int main()
{
    node *root = input_tree();
    insert (root,13);
    insert(root,100);
    level_order(root);
    return 0;
}