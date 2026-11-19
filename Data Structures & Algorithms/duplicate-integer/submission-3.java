
class Solution {
    public boolean hasDuplicate(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        for (int num : nums) {
            numSet.add(num);
        }
        boolean containsDupe = (!(numSet.size() == nums.length));
        return containsDupe;
    }
}