class Solution {
public:
    int minFlips(string target) {
        int len = target.size();
        char prev = ' ';
        // a continuous sequence of the same digits can be flipped in one run
        // therefore we just count how many differernt such sequences there are
        int cnt_continuous_digits = 0;
        for (int i = len - 1; i >= 0; --i) {
            if (target[i] != prev) {
                ++cnt_continuous_digits;
                prev = target[i];
            }
        }
        // if first digit is 0, it means the first sequence don't need to be flipped
        // so there is 1 less run
        return target[0] == '0'? cnt_continuous_digits - 1 : cnt_continuous_digits;
    }
};