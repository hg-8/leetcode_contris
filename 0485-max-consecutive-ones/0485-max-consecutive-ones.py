class Solution:
    def findMaxConsecutiveOnes(self, num: List[int]) -> int:
        # Variable to store global maximum consecutive 1s count
        ans = 0
        
        # Counter variable for current consecutive 1s streak
        count = 0
        
        # Iterate over each element in the input list
        for i in num:   
            # If current element is 0, reset current consecutive streak counter
            if i == 0:
                count = 0
            # If current element is 1, increment current consecutive streak counter
            else:
                count += 1
                
            # Update overall max consecutive 1s if current streak is larger
            if count > ans:
                ans = count
                
        # Return maximum consecutive 1s count
        return ans