class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        // sliding window of size k with hash set recording
        Set<Integer> s = new HashSet<>();
        for (int i = 0; i < nums.length; i ++) {
            if (s.contains(nums[i])) return true;
            s.add(nums[i]);
            if (s.size() > k)
                s.remove(nums[i - k]);  // cuz fixed len
        }
        return false;
    }
}