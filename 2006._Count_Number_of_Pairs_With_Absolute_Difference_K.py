class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        dic = dict()
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1

        count = 0
        for key, value in dic.items():
            if abs(k-key) in dic:
                count += value * dic[abs(k-key)]
            if abs(k+key) in dic:
                count += value * dic[abs(k+key)]

        return int(count/2)
