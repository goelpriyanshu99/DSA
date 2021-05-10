#include <bits/stdc++.h>
#define ll long long
#define f(s, e) for (int i = s; i < e; i++)
#define endl "\n"
using namespace std;

ll power(int p)
{
    ll mod = pow(10,9) + 7;
    ll res = 1;
    ll base = 2;
    while(p>0)
    {
        if(p&1)
        {
            res = (res*base)%mod;
        }
        base = (base*base)%mod;
        p >>= 1;
    }
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    int t;
    cin >> t;
    while (t--)
    {
       int n;
       cin>>n;
       ll res = power(n-1);
       cout<<res<<endl;
    }
    return 0;
}


# https://www.codechef.com/MAY21C/submit/XOREQUAL