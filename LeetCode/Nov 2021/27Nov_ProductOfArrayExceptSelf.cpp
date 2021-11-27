class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int idx = -1, mul = 1, n = nums.size();
        vector<int> res(n,0);
        for(int i = 0; i < n; i++) {
            if(nums[i] == 0) {
                if(idx != -1) {
                    idx = -2;
                    break;
                }
                else 
                    idx = i;
                continue;
            }
            
            mul *= nums[i];
        }
        
        if(idx == -2) {
            return res;
        }
        else if(idx != -1) {
            res[idx] = mul;
            return res;
        }
        
        for(int i = 0; i < n; i++) {
            int sign = ((mul < 0) ^ (nums[i] < 0)) ? -1 : 1;
 
            long long di = abs(mul);
            long long dvs = abs(nums[i]);

            long long quotient = 0, temp = 0;

            for (int i = 31; i >= 0; --i) {

                if (temp + (dvs << i) <= di) {
                  temp += dvs << i;
                  quotient |= 1LL << i;
                }
              }
            
            if(sign==-1) quotient=-quotient;
            res[i] = quotient;
        }
        
        return res;
        
    }
};
