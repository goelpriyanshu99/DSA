class Solution {
public:
    int singleNonDuplicate(vector<int>& nums) {
        int n = nums.size();
        int s = 0, e = n-1;
        int m;
        while(s<=e) {
            m = s + (e-s)/2;
            if(m == 0 || (m < n && nums[m] != nums[m-1] && nums[m] != nums[m+1])) break;
            else if((nums[m] == nums[m-1] && (m+1)%2 == 0) || (nums[m] == nums[m+1] && (m+1)%2 == 1)) s = m+1;
            else e = m-1;
        }
        return nums[m];
    }
};
