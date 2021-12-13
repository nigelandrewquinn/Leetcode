class Solution:
    
    def isConsistent(alllowed, word):
        for i in word:
            if i not in allowed:
                return False
        return True
    
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for word in words:
            flag = True
            for i in word:
                if i not in allowed:
                    flag = False
                    break
            if flag:
                count += 1
        return count
