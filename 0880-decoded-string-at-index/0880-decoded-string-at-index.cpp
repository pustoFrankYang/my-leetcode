// ¡¡¡gesah poorla backward formation
class Solution {
public:
    string decodeAtIndex(string s, int k) {
        long long currsum = 0;
        int n = s.size();
        // get total sum
        for (char ch : s) {
            if (isdigit(ch)) {
                currsum *= (ch - '0');
            } else {
                currsum ++;
            }
        }
        // backward
        // if digit, divide currsum daby
        //   - and k modulo
        //   - NO!!! k should modulo everywhen. 
        // if alpha, minus 1
        // and when currsum == k, getted
        // 唉，到底怎麼思考呢件事？還是用currsum變化嘅各種情況啩
        // 總長度currsum一開始總是大於k嘛
        // 其中（isalpha）稍-1都係大於
        // 減到等於呢，k=0啦，同時也揾都位置啦
        // 其中（isdigit）currsum遇到除以
        // 除完仲大於k，則冇關係，淨係無關嘅大數
        // 而除至小於k時，此小currsum當以modulo，以揾k喺新小範圍嘅位置
        for (int i = n - 1; i > -1; i --) {
            k %= currsum;
            if (isdigit(s[i])) {
                currsum /= (s[i] - '0');
            } else {
                // ja only possible to return when alpha
                if (0 == k) return (string)"" + s[i];
                currsum --;
            }
        }
        return string();
    }
};