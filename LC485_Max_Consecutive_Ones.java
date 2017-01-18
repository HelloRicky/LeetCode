public class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int result = 0;
        int count = 0;
        for(int i = 0; i< nums.length; i++){
            if(nums[i] == 1){
                count ++;
            }else{
                if(count > result){
                    result = count;
                    
                }
                count = 0;
            }
        }
        if(count > result){
            result = count;
        }
        return result;
    }
}