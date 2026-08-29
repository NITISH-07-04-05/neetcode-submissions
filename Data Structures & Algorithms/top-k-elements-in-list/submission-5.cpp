class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int,int> hashmap;
        vector<vector<int>> bucket (nums.size()+1);
        for (int num :nums){
            hashmap[num]++;
        }
        for (auto & pair : hashmap){
            bucket[pair.second].push_back(pair.first);
        }
        vector<int> result;
        for (int i = bucket.size()-1 ; i >= 0 ; i--){
            
            for (int x : bucket[i]){
                result.push_back(x);
                if (result.size() == k){
                    return result;
                }
            }
        }
        return result;
    }   
};
