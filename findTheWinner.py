#https://leetcode.com/problems/find-the-winner-of-the-circular-game/
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        
        def rec(index, k):
            if len(players) == 1:
                return
            index = (index + k) % len(players)
            players.pop(index)
            rec(index, k)
        rec(0, k-1)
        return players.pop()

                
