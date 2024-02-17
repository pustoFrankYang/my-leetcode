// ！只是把几年前的答案重新提交一遍观察
class Solution {
public:
    int reverse(int x) {
        stringstream ss;
        string s;
        ss << x;
        ss >> s;
        ss.clear();
        if (s[0]!='-') std::reverse(s.begin(), s.end());
        else std::reverse(s.begin()+1, s.end());
        double a;
        ss << s;
        ss >> a;
        if(a<-pow(2,31)||a>pow(2,31)-1) return 0;
        else return a;
    }
};