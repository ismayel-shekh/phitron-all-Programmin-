#include <bits/stdc++.h>
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

node *input_tree()
{
    int val;
    cin >> val;
    node *root;
    if (val == -1)
    {
        root = NULL;
    }
    else
    {
        root = new node(val);
        queue<node *> q;
        q.push(root);
        while (!q.empty())
        {
            node *p = q.front();
            q.pop();
            int l, r;
            cin >> l >> r;
            node *myleft = NULL;
            node *myright = NULL;
            if (l != -1)
            {
                myleft = new node(l);
                q.push(myleft);
            }
            if (r != -1)
            {
                myright = new node(r);
                q.push(myright);
            }

            p->left = myleft;
            p->right = myright;
        }
    }

    return root;
}

void level_order(node *root)
{
    if (root == NULL)
    {
        cout << "Tree is empty" << endl;
        return;
    }
    queue<node *> q;
    q.push(root);
    while (!q.empty())
    {
        node *f = q.front();
        q.pop();
        cout << f->val << " ";
        if (f->left)
            q.push(f->left);
        if (f->right)
            q.push(f->right);
    }
}
int max_hight(node* root){
    if(root == NULL){
        return 0;
    }
    int l=max_hight(root->left);
    int r=max_hight(root->right);
    return max(l,r) +1;
}
int count_leaf(node *root){
    if(root == NULL)
        return 0;
    if(root->left == NULL && root->right == NULL) return 1;
    else{
        
    }
}
int main()
{
    node *root = input_tree();
    level_order(root);
    cout<<endl<<max_hight(root)<<endl;
    return 0;
}
