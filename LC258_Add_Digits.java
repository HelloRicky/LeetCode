public class Solution {
    public int addDigits(int num) {
        int result;
        result = (num > 0 & num % 9 == 0) ? 9 : num % 9;
        return result;
    }
}