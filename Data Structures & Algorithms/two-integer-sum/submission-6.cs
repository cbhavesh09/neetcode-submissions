public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        var dict = new Dictionary<int,int>();
        int i = 0;
        foreach(int num in nums)
        {
            int diff = target-num;
            if(dict.ContainsKey(diff))
            {
                return [dict[diff],i];
            }
            dict.Add(num,i);
            i++;
        }
        return [0];

    }
}
