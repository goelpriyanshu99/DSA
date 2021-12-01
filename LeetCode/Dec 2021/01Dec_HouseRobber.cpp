class Solution {
public:
    void maxMoney(vector<int>& num, int i, int* c, int* n, int* p) {
        if(i < 0) return;
        int temp = num[i] + max(*n,*p);
        *p = *n;
        *n = *c;
        *c = temp;
        
        maxMoney(num,i-1,c,n,p);
    }
    
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n == 1)
            return nums[0];
        
        int cur = nums[n-2], next = nums[n-1],p = 0;
        maxMoney(nums,n-3,&cur,&next,&p);
        return max(cur,next);
    }
};