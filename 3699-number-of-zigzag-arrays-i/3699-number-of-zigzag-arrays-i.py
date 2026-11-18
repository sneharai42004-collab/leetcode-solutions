
class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        # Arrays of length 2
        up = [0] * m
        down = [0] * m

        for v in range(m):
            up[v] = v
            down[v] = m - 1 - v

        # Build arrays of length 3 to n
        for i in range(3, n + 1):
            new_up = [0] * m
            new_down = [0] * m

            # Prefix sum for increasing transitions
            total = 0
            for v in range(m):
                new_up[v] = total
                total = (total + down[v]) % MOD

            # Suffix sum for decreasing transitions
            total = 0
            for v in range(m - 1, -1, -1):
                new_down[v] = total
                total = (total + up[v]) % MOD

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD
