class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        pair = None
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if not pair:
                    pair = (s1[i], s2[i])
                elif pair == (s2[i], s1[i]):
                    pair = True
                else:
                    return False
        return (pair is None or pair is True)
