class Solution {
public:
    int minCost(vector<int>& startPos, vector<int>& homePos, vector<int>& rowCosts, vector<int>& colCosts) {
        int res = 0;
        
        // if row of startPos < homePos
        for(int i = startPos[0]; i < homePos[0]; ) {
            res += rowCosts[++i];
        }
        
        // if row of startPos > homePos
        for(int i = startPos[0]; i > homePos[0]; ) {
            res += rowCosts[--i];
        }
        
        // if col of startPos < homePos
        for(int i = startPos[1]; i < homePos[1]; ) {
            res += colCosts[++i];
        }

        // if col of startPos > homePos
        for(int i = startPos[1]; i > homePos[1]; ) {
            res += colCosts[--i];
        }
        
        return res;
    }
};