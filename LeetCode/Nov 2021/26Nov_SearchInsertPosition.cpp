class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        if(target <= nums[0]) return 0;
        int s = 0, e = nums.size()-1,m;
        while(s<=e) {
            m = s + (e-s)/2;
            if(nums[m] == target || (m>0 && nums[m-1] < target && nums[m] > target)) return m;
            else if(nums[m] < target) s = m+1;
            else e = m-1;
        }
        return nums.size();
    }
};
