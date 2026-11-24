public class Solution {
    public bool IsPalindrome(string s) {
        int l =0;
        int r = s.Length-1;
        while(l<r)
        {
            while(!char.IsLetterOrDigit(s[l]) && l<r)
            {
                l++;
            }

            while(!char.IsLetterOrDigit(s[r]) && l<r)
            {
                r--;
            }

            if(char.ToLowerInvariant(s[l])!=char.ToLowerInvariant(s[r]))
            {
                return false;
            }
            l++;
            r--;
        }
        return true;       
    }

    
}
