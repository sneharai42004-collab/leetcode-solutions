
from collections import defaultdict

class Solution:
    def maxSelectedElements(self, nums: List[int]) -> int:
        nums.sort()

        dp = defaultdict(int)
        ans = 0

        for x in nums:
            prev = dp[x]

            # Use current element without increasing it
            dp[x] = max(dp[x], dp[x - 1] + 1)

            # Increase current element by 1
            dp[x + 1] = max(dp[x + 1], prev + 1)

            ans = max(ans, dp[x], dp[x + 1])

        return ans
