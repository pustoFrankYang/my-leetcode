/**
 * @param {number[]} height
 * @return {number}
 */
/*
WA
[2,3,10,5,7,8,9]
*/
var maxArea = function(h) {
    let L = 0, R = h.length - 1;
    let ans = (R - L) * Math.min(h[L], h[R]);
    while (L < R) {
        let nl = L, nr = R;
        if (h[L] < h[R]) {
            while (nl < R && h[nl] <= h[L])
            nl ++;
        L = nl;
        ans = Math.max(ans, (R - L) * Math.min(h[L], h[R]));
        } else {
            while (nr > L && h[nr] <= h[R])
            nr --;
        R = nr;
        ans = Math.max(ans, (R - L) * Math.min(h[L], h[R]));
        }
        
//         console.log(L, R)
        
//         // console.log(L, R)
    }
    return ans;
};