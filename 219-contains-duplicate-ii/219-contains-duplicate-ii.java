class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // sliding window of size k with hash map recording
        Map<Integer, Integer> m = new HashMap<>();
        int l = 0, r = 0;
        for (; r < nums.length && r < k + 1; r ++) {  // !!! k + 1
            if (m.getOrDefault(nums[r], 0) > 0)
                return true;
            m.put(nums[r], 1);
        }
        while (r < nums.length) {
            m.put(nums[l], 0);
            l ++;
            if (m.getOrDefault(nums[r], 0) > 0)
                return true;
            m.put(nums[r], 1);
            r ++;
        }
        return false;
    }
}