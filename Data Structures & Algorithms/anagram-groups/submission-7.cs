public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var dict = new Dictionary<string,List<string>>();

        foreach(string word in strs)
        {
            int[] iList = new int[26];
            foreach(char ch in word)
            {
                iList[ch-'a']++;

            }
            string key = string.Join(",",iList);
            if(!dict.TryGetValue(key,out var list))
            {
                    list = new List<string>();
    dict[key] = list;
            }
            dict[key].Add(word);
        }
        return dict.Values.ToList();


        
    }
}
