class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        n = len(nums)
        total = 0
        for i in range(n):
            total += nums[i]
            maxSum = max(maxSum, total)
            if total < 0:
                total = 0
        return maxSum

