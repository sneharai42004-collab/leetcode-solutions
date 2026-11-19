
from collections import Counter

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        freq = Counter(nums)
        ans = 1

        for x in freq:

            if x == 1:
                count = freq[1]
                ans = max(ans, count if count % 2 == 1 else count - 1)
                continue

            length = 0
            curr = x

            
            while freq[curr] >= 2:
                length += 2
                curr = curr * curr

            
            if freq[curr] >= 1:
                length += 1
            else:
                length -= 1

            ans = max(ans, length)

        return ans
