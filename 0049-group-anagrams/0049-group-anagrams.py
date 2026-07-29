class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Initialize hash table to store key-value pair of (sorted_string -> list of anagrams)
        ht = {}
        
        # Iterate over each word in the input list of strings
        for ele in strs:
            # Sort characters alphabetically and join to form a canonical key shared by all anagrams
            key = ''.join(sorted(ele))
            
            # If sorted key is not yet in hash table, create a new list for this key
            if key not in ht:
                ht[key] = []
                
            # Append current original word to its corresponding anagram key group list
            ht[key].append(ele)
            
        # Initialize list to hold all collected anagram groups
        ans = []
        
        # Collect each list of grouped anagrams from dictionary values
        for key in ht:
            ans.append(ht[key])
            
        # Return final list of grouped anagrams
        return ans