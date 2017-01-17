public class Solution {
	// Ricky Zheng
	/**
	Method: 1
	O(n)

	**/


	public static int[] twoSum_1(int[] nums, int target) {
		int [] result = new int[2];
		Map<Integer, Integer> map = new HashMap<Integer, Integer>();
		for(int i = 0; i < nums.length; i++){
			if(map.containsKey(target - nums[i])){
				result[0] = map.get(target - nums[i]);
				result[1] = i;
				return result;
			}

			map.put(nums[i], i);
		}

		return result;

	/**
	Method: 2
	O(nlogn)

	**/


	public static int[] twoSum_2(int[] nums, int target) {
		int i, j = 0;
		boolean flag = false;
		int [] result = new int[2];
		
		for(i = 0; i < nums.length; i++){
			if(flag){
				break;
			}
			if(nums[i] >= target){
				continue; 
			}
			int rest = target - nums[i];
			for(j = i + 1; j < nums.length; j ++){
				if(nums[j] == rest){
					flag = true;
					break;
				}
			}
			
		}
		result[0] = i - 1;
		result[1] = j;
		return result;
}