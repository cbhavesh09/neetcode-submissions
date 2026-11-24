public class Solution {
    public bool IsAnagram(string s, string t) {
        if(s.Length != t.Length)
        {
            return false;
        }
        Dictionary<char,int> hset = new Dictionary<char,int>();
        int count = 0;
        foreach(char ch in s)
        {

                hset[ch]= hset.GetValueOrDefault(ch,0)+1;

        }

        foreach(char c in t)
        {
            if(!hset.ContainsKey(c)) return false;
            hset[c]--;
        }

        foreach(int i in hset.Values)
        {
            if(i != 0)
            {
                return false;
            }
        }

        return true;

    }
}
