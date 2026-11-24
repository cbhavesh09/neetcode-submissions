public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var dict = new Dictionary<string,List<string>>();

        foreach(string word in strs)
        {
            List<int> iList = Enumerable.Repeat(0,26).ToList();
            foreach(char ch in word)
            {
                iList[(int)ch-(int)'a']+=1;

            }
            string key = string.Join(",",iList);
            if(!dict.ContainsKey(key))
            {
                dict[key] = new List<string>();
            }
            dict[key].Add(word);
        }
        return dict.Values.ToList();


        
    }
}
