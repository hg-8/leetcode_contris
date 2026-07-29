class Solution:
    def majorityElement(self, arr: List[int]) -> int:
        # Boyer-Moore Voting Algorithm
        # Initialize majority candidate 'mc' with the first element
        mc = arr[0]
        
        # Initialize vote counter for current candidate
        c = 1
        
        # Iterate over remaining elements of array starting from index 1
        for i in range(1, len(arr)):
            # If current element matches candidate, increment vote counter
            if arr[i] == mc:
                c += 1
            # If current element differs from candidate, decrement vote counter
            else:
                c -= 1
                # If vote count reaches zero, reset candidate to current element and reset count to 1
                if c == 0:
                    mc = arr[i]
                    c = 1            
                    
        # Optional print statement for debugging/visualizing output candidate
        print(mc)
        
        # Return majority element candidate (guaranteed to be majority element per problem constraint)
        return mc