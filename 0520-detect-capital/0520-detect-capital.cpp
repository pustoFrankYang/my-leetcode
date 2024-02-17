class Solution {
public:
    bool detectCapitalUse(string word) {
        if (word.size() <= 1) return true;
        bool is_first_upper = word[0] >= 'A' && word[0] <= 'Z';
        bool is_second_upper = word[1] >= 'A' && word[1] <= 'Z';
        if (!is_first_upper && is_second_upper) {
            return false;
        }
        for (int i = 2; i < word.size(); i++) {
            if (is_first_upper && is_second_upper 
                && word[i] >= 'a' && word[i] <= 'z') {
                return false;
            }
            if (is_first_upper && !is_second_upper 
                && word[i] >= 'A' && word[i] <= 'Z') {
                return false;
            }
            if (!is_first_upper && !is_second_upper
               && word[i] >= 'A' && word[i] <= 'Z'
               )  {
                return false;
            }
            
        }
        
        return true;
    }
};