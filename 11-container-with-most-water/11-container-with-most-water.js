/**
 * @param {number[]} height
 * @return {number}
 */
/*
WA:
[1,2,1]
*/
// ¡¡¡¡gesah,
// cuz I-got-it-ve a fickende false one
var maxArea = function(height) {
    let L = 0, R = height.length - 1;
    let tl = L, tr = R;
    let ans = (R - L) * Math.min(height[L], height[R]);
    while (true) {
        // goto next state
        // first, it is obvious that we only want to find a line that is higher than now.
        // but which one should we move, L or R?
        //   say, the lower is L, and higher is R
        //   and there are L, newL, newR, R,
        //   we are not interested in the pair (L, newR), 
        //      because it can only be shorter than (L, R) but with same height
        //   but we don't know pairs (newL, R) and (newL, newR), so we must calc in following steps
        //   that's why it is only reasonable to move L to newL, say, L is lower
        if (height[L] < height[R]) {
            while (tl < tr && height[tl] <= height[L])
                tl ++;
        } else {
            while (tl < tr && height[tr] <= height[R])
                tr --;
        }
        if (tl < tr) {
            L = tl, R = tr;
            ans = Math.max(ans, (R - L) * Math.min(height[L], height[R]));
        } else break;
    }
    return ans;
};