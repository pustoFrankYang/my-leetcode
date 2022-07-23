func shortestSequence(rolls []int, k int) int {
    var m = map[int]bool{}
    var curr, cntCollection int = 0, 0
    for _, n := range rolls {
        if !m[n] {
            curr ++
            m[n] = true
        }
        // when we've collected all k nums, ++
        if curr == k {
            cntCollection ++
            curr = 0
            m = map[int]bool{}
        }
    }
    return cntCollection + 1
}