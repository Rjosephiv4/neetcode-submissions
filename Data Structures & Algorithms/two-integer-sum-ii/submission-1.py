class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #numbers sorted in non decreasing (increasing + =) order
        #return the indicies of 1 indexed(stupid) such that they add up to a target adn index 1 < index 2
        # [x1, x2, x3]
        # x1 and x3 then if your value is greater then x3  is out of play so you go back
        
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right +1]
            elif total > target:
                right -= 1
            elif total < target:
                left +=1
        
        return []