class Solution:
    def minElement(self, nums: List[int]) -> int:
        def get_digit_sum(n: int) -> int:
            return sum(int(digit) for digit in str(n))
        
        # Replace each element with its digit sum and find the minimum
        return min(get_digit_sum(num) for num in nums)