# Hashmap
# Runtime: O(n)
# Space: O(n)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        
        # Iterate through strs
        for string in strs:
            # Start by joining the string
            sorted_str = ''.join(sorted(string))

            # Check hashmap, if it is not in it add with the sorted string as the key and the original string as the value
            if sorted_str not in grouped:
                grouped[sorted_str] = []

            # If it exists in the hashmap already just append it
            grouped[sorted_str].append(string)

        # After iterating through strs we'll have the anagrams grouped into groups
        return grouped.values()
