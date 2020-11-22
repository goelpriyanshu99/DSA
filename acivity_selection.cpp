#include<bits/stdc++.h>
using namespace std;

bool cmp(pair<int,int> a, pair<int,int> b) {
	return a.second < b.second;
}

int main() {
    
    int t, n, x, y;
	cin>>t;
	while(t--) {
	    vector<pair<int, int>> v;
	    int res = 1, e = 0;
		cin>>n;
		
		for(int i = 0; i < n; i++) {
			cin>>x>>y;
			v.push_back(make_pair(x,y));
		}
		
		sort(v.begin(), v.end(),cmp);
		
		for(int i = 1; i < n; i++) {
			if(v[i].first >= v[e].second) {
				res++;
				e = i;
			}
		}
		
		cout<<res<<endl;
	}

	return 0;
}

// Problem: You are given n activities (from 0 to n-1) with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
// Input: 
// 1 
// 3
// 10 20
// 12 15
// 20 30
// Output:
// 2
// Explanation
// Person can only do 0th and 2nd activities. (Sort in  ascending order of finish time)
