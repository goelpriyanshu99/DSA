class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        unordered_map<string,int> umap;
        for(auto &it: words1) {
            umap[it]++;
        }
        for(auto &it:words2) {
            if(umap[it] > 1) umap[it] = 0;
            umap[it]--;
        }
        
        int res = 0;
        for(auto i: umap) {
            if(i.second == 0) res++;
        }
        
        return res;
    }
};