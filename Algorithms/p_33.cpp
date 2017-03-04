// Search in Rotated Sorted Array
// 先找到翻转pivot，再二分
class Solution {
private:
    int find_special_index(const vector<int>& nums){
        int len = nums.size();
        int last_value = nums[len-1];
        if(nums[0]<=last_value){
            return 0;
        }
        int left = 0;
        int right = len - 2;
        while(left<right){
            int mid = (left+right)/2;
            if(nums[mid]<last_value){
                right = mid - 1;
            }else{
                if(mid == left){
                    if(nums[right]>last_value){
                        return right + 1;
                    }else{
                        return left + 1;
                    }
                }else{
                    left = mid;
                }
            }
        }
        return left + 1;
    }
    int binary_search(const vector<int>& nums, int left, int right, int target){
        if(left+1>=right){
            if(nums[left]==target){
                return left;
            }else if(nums[right]==target){
                return right;
            }else{
                return -1;
            }
        }
        int mid = (left+right)/2;
        if(nums[mid]<target){
            left = mid + 1;
        }else if(nums[mid]==target){
            return mid;
        }else{
            right = mid - 1;
        }
        return binary_search(nums, left, right, target);
    }
public:
    int search(vector<int>& nums, int target) {
        int len = nums.size();
        if(len==0){
            return -1;
        }
        int last_value = nums[len-1];
        if(target==last_value){
            return len - 1;
        }
        if(len==1){
            return -1;
        }
        int spe_index = find_special_index(nums);
        if(target<last_value){
            return binary_search(nums, spe_index, len-2, target);
        }else{
            return binary_search(nums, 0, spe_index-1>=0?spe_index-1:0, target);
        }
    }
};