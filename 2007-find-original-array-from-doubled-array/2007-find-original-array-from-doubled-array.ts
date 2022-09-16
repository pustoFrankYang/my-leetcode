// Q2007m, runtime 88.89%, TS
function findOriginalArray(changed: number[]): number[] {
    let ans: number[] = []; // soll init
    let cnt = new Map();
    // js sort() is really problematic
    changed.sort((a, b) => a - b);
    for (let n of changed) { // gramma here is of
        if (cnt.has(n))
            cnt.set(n, cnt.get(n) + 1);
        else
            cnt.set(n, 1);
    }
    for (let n of changed) {
        if (cnt.get(n) == 0)
            continue;
        if (!cnt.has(n * 2))
            return [] as number[];
        if (n == 0 && cnt.get(n) <= 1 || n >= 1 && cnt.get(n) <= 0)
            return [] as number[];
        cnt.set(n, cnt.get(n) - 1);
        cnt.set(n * 2, cnt.get(n * 2) - 1);
        ans.push(n);
    }
    return ans;
};