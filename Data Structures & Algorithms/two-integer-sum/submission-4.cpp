class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int,int> sett;

        for (int i = 0 ;i < nums.size();i++){
            int complement = target - nums[i];
            if (sett.find(complement) != sett.end()){
                return {sett[complement],i};
            }
            sett[nums[i]] = i;
        }
        return {};

    }
};
