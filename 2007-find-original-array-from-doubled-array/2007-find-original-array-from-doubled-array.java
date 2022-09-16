class Solution {
    public int[] findOriginalArray(int[] changed) {
        List<Integer> ans = new ArrayList<>();
        Map<Integer, Integer> cnt = new HashMap<>();
        // gramma
        List<Integer> nums = Arrays.stream(changed).boxed().collect(Collectors.toList());
        Collections.sort(nums); // gramma
        for (var num : nums) {
            cnt.put(num, cnt.getOrDefault(num, 0) + 1);
        }
        for (var num : nums) {
            if (cnt.get(num) == 0)
                continue;
            if (!cnt.containsKey(num * 2))
                return new int[]{};
            if (num == 0 && cnt.get(num * 2) <= 1 || num >= 1 && cnt.get(num * 2) <= 0)
                return new int[]{};
            cnt.put(num, cnt.get(num) - 1);
            cnt.put(num * 2, cnt.get(num * 2) - 1);
            ans.add(num);
        }
        // gramma
        return ans.stream().mapToInt(i->i).toArray();
    }
}