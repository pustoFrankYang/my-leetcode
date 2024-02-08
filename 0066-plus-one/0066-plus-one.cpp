class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        bool higher1 = true;
        int len = digits.size();
        for (int i = len - 1; i >= 0; --i) {
            if (higher1) {
                if (digits[i] == 9) {
                    digits[i] = 0;
                } else {
                    ++digits[i];
                    higher1 = false;
                }
            }
        }
        if (higher1) {
            digits.insert(digits.begin(), 1);
        }
        return digits;
    }
};