class Solution {
public:
    int hammingDistance(int x, int y) {
        if(x == y) return 0;
        
        if(x%2 != y%2) return 1+hammingDistance(x/2,y/2);
        
        return hammingDistance(x/2, y/2);
    }
};
