#Question -> https://leetcode.com/problems/plus-one/
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, digit in reversed(list(enumerate(digits))):
            if digit == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0, 1)
            else:
                digits[i] += 1
                break
        return digits
                

                                    
                                    
                                    
                                    
                                    
                                    
        
