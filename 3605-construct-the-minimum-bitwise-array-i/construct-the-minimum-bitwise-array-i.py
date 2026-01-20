from typing import List

class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        ans = []
        for x in nums:
            # (a | (a+1)) is always odd, so even nums (only prime is 2) are impossible
            if x % 2 == 0:
                ans.append(-1)
                continue

            # k = number of trailing 1-bits in x
            k = 0
            t = x
            while t & 1:
                k += 1
                t >>= 1

            # minimal a is obtained by using the largest possible k (the trailing-ones count)
            a = x - (1 << (k - 1))
            ans.append(a)

        return ans
        