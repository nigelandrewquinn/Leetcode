class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        for i in range(len(word)):
            if word[i] == ch:
                segment = word[:i+1]
                segment = segment[::-1]
                word = segment + word[i+1:]
                return word
        return word
