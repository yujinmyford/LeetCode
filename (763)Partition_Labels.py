class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        result = []
        lastSeen = {}
        lastSeenMax = 0
        count = 0
        # char = key, i(index) = value
        for i, char in enumerate(s):
            lastSeen[char] = i
        for i, char in enumerate(s):
            lastSeenMax = max(lastSeenMax, lastSeen[char])
            count += 1
            if i == lastSeenMax:
                result.append(count)
                count = 0
        return result
