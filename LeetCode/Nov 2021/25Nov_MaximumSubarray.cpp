class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int x = 0, res = 0, maxNeg = -INT_MAX;
        for(int i = 0; i < nums.size(); i++) {
            x += nums[i];
            if(nums[i] <=0) maxNeg = max(maxNeg,nums[i]);
            res = max(res,x);
            if(x < 0) x = 0;
        }
        
        if(res == 0) return maxNeg;
        
        return res;
    }
};