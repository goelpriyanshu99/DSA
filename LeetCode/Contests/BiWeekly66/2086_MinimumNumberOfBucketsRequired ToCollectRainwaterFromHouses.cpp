class Solution {
public:
    int minimumBuckets(string street) {
        int cur = -2,res = 0;
        int n = street.length();
        
        for(int i = 0; i < n; i++) {
            if(street[i] == 'H') {
                // if there is a dot after H then fill that first and update cur pointer
                if(i < n-1 && street[i+1] == '.') {
                    if(cur != i-1) {
                        cur = i+1;
                        res++;
                    }
                }
                // if their exist . previously then this res++ will be executed
                else if(i>=1 && street[i-1] == '.') {
                    if(cur != i-1) {
                        res++;
                    }
                }
                // if there exists an H whose both sides have H only
                else {
                    return -1;
                }
            } 
        }
        
        return res;
    }
};