class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        listS = list(s)
        listT = list(t)
        if len(listS) != len(listT):
            return False

        for i, c in enumerate(listS):
            for j, ch in enumerate(listT):
                if c == ch:
                    del(listT[j])
                    break
        
        if len(listT) == 0:
            return True
        return False




# # 7/25
# # Hashmap
# # Runtime: O(n)
# # Space: O(s+t) = O(n)

# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:

#         s_hash = {}
#         t_hash = {}

#         for i in s:
#             if i in s_hash:
#                 s_hash[i] += 1
#             else:
#                 s_hash[i] = 1
        

#         for i in t:
#             if i in t_hash:
#                 t_hash[i] += 1
#             else:
#                 t_hash[i] = 1
        

#         return s_hash == t_hash
