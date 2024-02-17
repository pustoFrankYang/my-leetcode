class Solution {
public:
    bool rotateString(string s, string goal) {
        // 噢对了。。。长度不一致的要排除
        // 比如 "aa" "a"
        if (s.size() != goal.size()) return false;
        
        // 好像以前见过
        // 一个规律，就是可以把原字符串自我复制到后面，称为s2吧
        // 然后看goal是否是个子串
        // 因为这样的话以s的任意字符为首的shifted串
        // 都回出现在s2里了
        string s2 = s + s;
        return (s2.find(goal) != string::npos);
    }
};