class Solution {
public:
    // 灵机一动竟然还真对了，不错不错
    // 我在这里试验随机改程序某个地方，怎么能让程序运行更快。。。。好像是玄学？
    int minFlips(string target) {
        //int len = target.size();
        
        // a continuous sequence of the same digits can be flipped in one run
        // therefore we just count how many differernt such sequences there are
        int cntseq = 1;
        // if first digit is 0, it means the first sequence don't need to be flipped
        // so there is 1 less run
        if (target[0] == '0') cntseq = 0;
        
        for (int i = 0; i < target.size() - 1; i++) {
            if (target[i] != target[i + 1]) {
                ++cntseq;
            }
        }
        return cntseq;
    }
};