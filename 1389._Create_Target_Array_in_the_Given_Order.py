class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        ans = []
        for i, n in zip(index, nums):
            ans = ans[:i] + [n] + ans[i:]
        return ans
