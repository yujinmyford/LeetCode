# Hashmap
# Runtime: O(n)
# Space: O(n)

class Solution:
    def romanToInt(self, s: str) -> int:
        # Initialize and add the roman to integer conversions
        conversion = {}
        conversion["I"] = 1
        conversion["V"] = 5
        conversion["X"] = 10
        conversion["L"] = 50
        conversion["C"] = 100
        conversion["D"] = 500
        conversion["M"] = 1000

        # Instantiate converted, which will hold the converted integer value from the roman numeral
        converted = 0

        # Start for loop through s
        for i in range(len(s)):
            # If the current character is less than the next one, we would subtract current and then add next
            if i < len(s) and conversion[s[i]] < conversion[s[i+1]]:
                converted -= conversion[s[i]]
            # If not, we would just add the current integer
            else:
                converted += conversion[s[i]]
        return converted

