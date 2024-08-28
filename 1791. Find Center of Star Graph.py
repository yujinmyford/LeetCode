class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        hashmap = {}

        for pair in edges:
            if pair[0] not in hashmap:
                hashmap[pair[0]] = 1
            elif pair[0] in hashmap:
                hashmap[pair[0]] += 1
            if pair[1] not in hashmap:
                hashmap[pair[1]] = 1
            elif pair[1] in hashmap:
                hashmap[pair[1]] += 1

        for key in hashmap:
            if hashmap[key] == len(edges):
                return key
