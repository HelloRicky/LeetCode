public class Solution {
    public int[] constructRectangle(int area) {
        int [] result = new int [2];
        int side = (int) Math.sqrt(area);
        while(area % side > 0){
            side --;
        }
        result[0] = area / side;
        result[1] = side;
        return result;
    }
}