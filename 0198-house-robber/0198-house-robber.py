class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        for n in range (1, len(nums)):
            dp[n] = max(nums[n]+dp[n-2], dp[n-1])
        return dp[-1]
        