class Solution {
public:
    // 灵机一动竟然还真对了，不错不错
    int minFlips(string target) {
        int len = target.size();
        
        // a continuous sequence of the same digits can be flipped in one run
        // therefore we just count how many differernt such sequences there are
        int cnt_seq = 1;
        // if first digit is 0, it means the first sequence don't need to be flipped
        // so there is 1 less run
        if (target[0] == '0') cnt_seq = 0;
        
        for (int i = 0; i < len - 1; ++i) {
            if (target[i] != target[i + 1]) {
                ++cnt_seq;
            }
        }
        return cnt_seq;
    }
};