/**
 * @param {string} s
 * @return {string}
 */
var minRemoveToMakeValid = function(s) {
    // when there is ), stack should have (, or delete incomer.
    // when reached the end, stack should be empty, or delete remainer.
    let stk = [], ans = [];
    for (let i = 0; i < s.length; i ++) {
        let ch = s[i];
        if (ch == "(")
            stk.push(i);
        else if (ch == ")") {
            // delete the incomer
            if (!stk.length) ans.push(i);
            // the previous paren made valid
            else stk.pop();
        }
    }
    // delete the remainers
    ans = stk.concat(ans);
    ans.sort((a, b) => b - a);
    for (i of ans) {
        s = s.slice(0, i) + s.slice(i + 1);
    }
    return s;
};