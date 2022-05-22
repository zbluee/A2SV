#question = > https://leetcode.com/problems/maximum-number-of-coins-you-can-get/
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_coins = []
        triplets = len(piles) / 3
        coin_index = 1
        while(triplets > 0):
            # -2 * coin_index gives the second max coin from each triplets
            max_coins.append(piles[-2 * coin_index])
            coin_index += 1
            triplets -= 1
            
        return sum(max_coins)
