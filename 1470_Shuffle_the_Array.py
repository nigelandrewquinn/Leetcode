class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        new_ar = []
        for i in range(n):
            new_ar.append(nums[i])
            new_ar.append(nums[i+n])
        return new_ar
