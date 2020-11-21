#include<iostream>
#include<algorithm>

using namespace std;

// comparator
bool cmp(int a, int b) {
    return a<=b;
}

int main() {
    // Available currency in India
    int avl_curr[] = {1,2,5,10,20,50,100,200,500,2000};
    int n = sizeof(avl_curr)/sizeof(int);
    // Amount you want to check
    int money = 409;
    cout<<"Minimum number of currency value needed : \n";
    while(money > 0 ) {
        int pos = lower_bound(avl_curr, avl_curr+n, money, cmp) - avl_curr - 1;
        cout<<avl_curr[pos]<<" + ";
        money -= avl_curr[pos];
    }
    return 0;
}

// Problem: To get minimum currency to pay money
// Solution: Used lower_bound method with comparator
