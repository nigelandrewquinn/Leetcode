class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        import math
        return 2**int(math.log(n,2)) == n