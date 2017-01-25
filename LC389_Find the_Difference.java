public class Solution {
    public char findTheDifference(String s, String t) {
        String n = s + t;
        char [] n_c = n.toCharArray();
        char p = 0;
        for(int i = 0; i< n_c.length; i++){
            p ^= n_c[i];
        }
        return p;
    }
}