#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cin >> n;

    while (n--)
    {
        string x;
        cin >> x;

        int zaza = 0;
        int kaza= 0;

       
        bool f = true;
        for (int i = 0; i < x.size(); i++)
        {
            int c = x[i] - 48;
            if (f)
            {
                if (c == 1)
                {
                    zaza++;
                }
                if (c == 0)
                {
                    f = false;
                }

            }
            else{
                 if (c == 1)
                {
                    kaza++;
                    f=true;
                }
                if (c == 0)
                {
                    f = true;
                }
            }
        }

        cout << zaza << endl;
    }

    return 0;
}