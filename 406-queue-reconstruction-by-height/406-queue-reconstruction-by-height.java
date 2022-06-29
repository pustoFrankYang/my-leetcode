class Solution {
    public int[][] reconstructQueue(int[][] people) {
        // sort by 1. height (higher first) 2. k (lower first)
        // I don't know how to use Comparator.comparing() to array
        Arrays.sort(people, 
                    (a, b) -> a[0] == b[0]? a[1] - b[1] : b[0] - a[0]
        );
        
        List<int[]> ans = new LinkedList<>();
        // then k value is the position whither we insert
        for (var p : people) {
            ans.add(p[1], p);
        }
        
        // change type to array
        int n = people.length;
        return ans.toArray(new int[n][2]);
    }
}