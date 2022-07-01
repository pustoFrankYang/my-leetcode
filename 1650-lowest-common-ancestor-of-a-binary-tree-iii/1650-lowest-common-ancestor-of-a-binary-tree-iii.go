/**
 * Definition for Node.
 * type Node struct {
 *     Val int
 *     Left *Node
 *     Right *Node
 *     Parent *Node
 * }
 */
// Q1650m, runtime 86.73%
func lowestCommonAncestor(p *Node, q *Node) *Node {
    // cuz val unique
    got := make(map[int]bool)
    got[p.Val] = true
    got[q.Val] = true
    
    for p.Parent != nil || q.Parent != nil {
        if p.Parent != nil {
            p = p.Parent
            if got[p.Val] {
                return p
            } else {
                got[p.Val] = true
            }
        }
        if q.Parent != nil {
            q = q.Parent
            if got[q.Val] {
                return q
            } else {
                got[q.Val] = true
            }
        }
    }
    return nil
}