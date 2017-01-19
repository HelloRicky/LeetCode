public class Solution {
    public boolean canWinNim(int n) {
        int net = n % 4;
        if(net > 0){
            return true;
        }
        return false;
    }
}