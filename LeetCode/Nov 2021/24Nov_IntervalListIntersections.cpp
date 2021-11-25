class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& fL, vector<vector<int>>& sL) {
        vector<vector<int>> res;
        int m = fL.size(), n = sL.size();
        // if(m == 0 || n  == 0) return res;
        
        int i = 0, j = 0;
        while(i < m && j < n) {
            if(fL[i][1] < sL[j][0]) {
                i++;
                continue;
            }
            else if(sL[j][1] < fL[i][0]) {
                j++;
                continue;
            }
            
            vector<int> t;
            if(fL[i][0] <= sL[j][0]) t.push_back(sL[j][0]);
            else t.push_back(fL[i][0]);
            
            if(fL[i][1] <= sL[j][1]) {
                t.push_back(fL[i][1]);
                i++;
            }
            else {
                t.push_back(sL[j][1]);
                j++;
            }
            
            res.push_back(t);
        }
        
        return res;
    }
};
