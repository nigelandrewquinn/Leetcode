class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int, str(n)))
        res = 1
        for x in n:
            res *= x
        return(res - sum(n))
        
