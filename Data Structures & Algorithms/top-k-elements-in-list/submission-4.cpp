class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map <int,int> hashmap;
        for( int num : nums){
            hashmap[num]++;
        }

        priority_queue<pair<int,int>> heap;

        for (auto & pair : hashmap){
            heap.push({pair.second,pair.first});
        }

        vector<int> result;
        for (int i = 0; i <k; i++){
            result.push_back(heap.top().second);
            heap.pop();
        }
        return result;
    }
};
