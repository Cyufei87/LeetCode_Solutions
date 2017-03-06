// Search Insert Position
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int len = nums.size();
        if(len==0){
            return 0;
        }
        int left = 0;
        int right = len - 1;
        while(left<right){
            int mid = (left+right)/2;
            int mid_value = nums[mid];
            if(mid_value<target){
                left = mid + 1;
            }else if(mid_value==target){
                return mid;
            }else{
                right = mid - 1;
            }
        }
        int left_value = nums[left];
        if(left_value>=target){
            return left;
        }else{
            return left + 1;
        }
    }
};