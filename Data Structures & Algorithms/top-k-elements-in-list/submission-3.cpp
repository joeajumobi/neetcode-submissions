class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> count;
        // key, values of number, frequency
        for(int num : nums){
            count[num]++;
        }

        vector<pair<int, int>> arr;
        //order pairs of frequency then number
        for (const auto& pair : count){
            arr.push_back({pair.second, pair.first});
        }
        //highest frequency pairs are first
        sort(arr.rbegin(), arr.rend());

        vector<int> res;
        for (int i = 0; i < k; ++i){
            res.push_back(arr[i].second);
        }
        return res;

        
    }
};
