class Solution:
    def countSubarrays(self, nums, k):
        n = len(nums)

        # Find position of k
        pos = nums.index(k)

        # Store prefix balances on the left side
        count = {0: 1}
        balance = 0

        for i in range(pos - 1, -1, -1):
            if nums[i] > k:
                balance += 1
            else:
                balance -= 1

            count[balance] = count.get(balance, 0) + 1

        # Start with k itself
        ans = 0
        balance = 0

        # Move from k towards the right
        for i in range(pos, n):
            if nums[i] > k:
                balance += 1
            elif nums[i] < k:
                balance -= 1

           
            ans += count.get(-balance, 0)
            ans += count.get(1 - balance, 0)

        return ans