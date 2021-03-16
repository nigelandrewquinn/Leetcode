class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = sum(accounts[0])
        for account in accounts:
            sum_account = sum(account)
            if sum_account > richest:
                richest = sum_account
        return richest
    
        
