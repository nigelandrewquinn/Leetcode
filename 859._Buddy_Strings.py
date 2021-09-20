USED = True
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        elif s == goal:
                return len(s) > len(set(s))

        pair = None
        for i in range(len(s)):
            if s[i] != goal[i]:
                if not pair:
                    pair = (s[i], goal[i])
                elif pair == (goal[i], s[i]):
                    pair = True
                else:
                    return False

        return (pair is None or pair == True)
