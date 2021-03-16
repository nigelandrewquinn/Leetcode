class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        most_candies = max(candies)
        for candy in candies:
            if (candy + extraCandies) >= most_candies:
                answer.append(True)
            else:
                answer.append(False)      
        return answer
