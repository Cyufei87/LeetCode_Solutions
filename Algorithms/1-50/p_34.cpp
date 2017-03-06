// Search for a Range
class Solution {
private:
    int searchValue(vector<int>& nums, int from, int end, int target, int left){
        if(from==end){
            if(nums[from]==target){
                return from;
            }else{
                return -1;
            }
        }else if(from+1==end){
            if(nums[from]==target){
                if(left==1||nums[end]>nums[from]){
                    return from;
                }else{
                    return end;
                }
            }else if(nums[end]==target){
                return end;
            }else{
                return -1;
            }
        }
        int mid = (from+end)/2;
        if(nums[mid]==target){
            if(left==1){
                if(nums[mid-1]==target){
                    return searchValue(nums, from, mid-1, target, left);
                }else{
                    return mid;
                }
            }else{
                if(nums[mid+1]==target){
                    return searchValue(nums, mid+1, end, target, left);
                }else{
                    return mid;
                }
            }
        }else if(nums[mid]<target){
            return searchValue(nums, mid+1, end, target, left);
        }else{
            return searchValue(nums, from, mid-1, target, left);
        }
    }
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int> result;
        if(nums.size()>0){
            int left = searchValue(nums, 0, nums.size() - 1, target, 1);
            int right = -1;
            if(left!=-1){
                right = searchValue(nums, left, nums.size() - 1, target, 0);
            }
            result.push_back(left);
            result.push_back(right);
        }else{
            result.push_back(-1);
            result.push_back(-1);
        }
        return result;
    }
};