public class Solution {

	// O(n)
    public void moveZeroes(int[] nums) {
        int count = 0;
        for(int i: nums){
            if(i != 0) nums[count ++] = i;
        }
        while(count < nums.length){
            nums[count ++] = 0;
        }
    }
}