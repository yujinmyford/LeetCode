# Array
# Runtime: O(n log n)
# Space: O(n)

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals and instantiate merged
        intervals.sort()
        merged = []
 
        # Start a for loop for intervals
        for interval in intervals:
            # If merged is empty, just add the current one we're on
            if merged == []:
                merged.append(interval)
            # If not, check variables to see if intervals overlap
            else:
                # Get the variables for previous and current
                last_merged_high = merged[-1][1]
                current_low = interval[0]
                current_high = interval[1]

                # Check if it overlaps, merge if does
                if last_merged_high >= current_low:
                    merged[-1][1] = max(last_merged_high, current_high)
                # If it doesn't overlap, just add to merged
                else:
                    merged.append(interval)
        return merged

