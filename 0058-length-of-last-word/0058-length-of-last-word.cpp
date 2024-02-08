class Solution {
public:
    int lengthOfLastWord(string s) {
        stringstream ss(s);
        string word;
        // 我日，把循环写成空的之后编译器就知道怎么优化了。。。？
        while (ss >> word) { };
        return word.size();
    }
};