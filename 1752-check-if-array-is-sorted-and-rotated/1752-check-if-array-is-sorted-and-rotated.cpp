class Solution {
public:
    bool check(vector<int>& nums) {
        bool flag = false;
        for(int i =0 ; i<nums.size()-1;i++){
            if(nums[i]>nums[i+1]){
                if(flag){
                    return false;
                }
                flag = true;
            }
        }
        if(flag){
            return nums.front()>=nums.back();
        }
        return true;
    }

};