class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        count = 0
        select = ''
        if ruleKey == 'type':
            select = 0
        elif ruleKey == 'color':
            select = 1
        else:
            select = 2
        
        for item in items:
            if item[select] == ruleValue:
                count+=1
        return count
            