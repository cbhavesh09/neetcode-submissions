public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var dict = new Dictionary<int,int>();
        int i = 0;
        foreach(int num in nums)
        {
            int diff = target-num;
            if(dict.TryGetValue(diff,out int x))
            {
                return [x,i];
            }
            dict[num]= i;
            i++;
        }
        return [0];

    }
}
