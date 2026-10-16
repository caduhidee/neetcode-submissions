class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}
        for num in range(0, len(nums)):
            difference = target - nums[num]
            if difference in numMap:
                return [numMap[difference], num]
            numMap[nums[num]] = num