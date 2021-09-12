class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        import math
        return 4**round(math.log(n,4)) == n