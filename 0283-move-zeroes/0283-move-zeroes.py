class Solution:
    def moveZeroes(self, arr: List[int]) -> None:
        # Initialize write pointer 'j' to track position for next non-zero element
        j = 0
        
        # Iterate reader pointer 'i' across array
        for i in range(len(arr)):
            # If current element is non-zero
            if arr[i] != 0: 
                # Swap non-zero element at i with element at write pointer j
                arr[j], arr[i] = arr[i], arr[j]
                # Increment write pointer j
                j += 1
                
        # Optional print output for visual confirmation
        print(arr)