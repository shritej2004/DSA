class Solution:
    def stoneGameII(self, piles: list[int]) -> int:
        n = len(piles)
        #Shritej
        # Calculate suffix sums so suffix_sum[i] stores the sum of piles[i:]
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + piles[i]
            
        memo = {}

        def dp(i: int, M: int) -> int:
            # Base case: if remaining piles can all be taken by the current player
            if i + 2 * M >= n:
                return suffix_sum[i]
            
            if (i, M) in memo:
                return memo[(i, M)]
            
            max_stones = 0
            # Try taking X piles where 1 <= X <= 2M
            for X in range(1, 2 * M + 1):
                next_M = max(M, X)
                # Current player gets (total remaining stones) - (best opponent score)
                stones = suffix_sum[i] - dp(i + X, next_M)
                max_stones = max(max_stones, stones)
                
            memo[(i, M)] = max_stones
            return max_stones

        # Alice starts at index 0 with M = 1
        return dp(0, 1)       