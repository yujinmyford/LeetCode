class Solution:
    def isPalindrome(self, s: str) -> bool:
        front = 0
        end = len(s) - 1

        # Convert s to lowercase letters and remove all non-alphanumeric characters
        s = s.lower()
        s_list = list(s)
        for i in range(len(s_list)):
            # If s[i] is not lower case letter
            if (ord(s_list[i]) < 97) or (ord(s_list[i]) > 122):
                s_list[i] = ""

        while front <= end:
            while (ord(s[front]) < 48 or 57 < ord(s[front]) < 97 or ord(s[front]) > 122) and front < end:
                front += 1
            
            while (ord(s[end]) < 48 or 57 < ord(s[end]) < 97 or ord(s[end]) > 122) and front < end:
                end -= 1
                
            if s[front] != s[end]:
                return False
            front += 1
            end -= 1
        
        return True




# # Neetcode

# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         l, r = 0, len(s) - 1
#         while l < r:
#             while l < r and not self.alphanum(s[l]):
#                 l += 1
#             while l < r and not self.alphanum(s[r]):
#                 r -= 1
#             if s[l].lower() != s[r].lower():
#                 return False
#             l += 1
#             r -= 1
#         return True

#     # Could write own alpha-numeric function
#     def alphanum(self, c):
#         return (
#             ord("A") <= ord(c) <= ord("Z")
#             or ord("a") <= ord(c) <= ord("z")
#             or ord("0") <= ord(c) <= ord("9")
#         )


# # 7/26:
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
        
#         stk = []


#         for char in s:
#             if char.isalnum():
#                 stk.append(char.lower())

#         for i in range(len(s) - 1):
#             if s[i].isalnum():
#                 if s[i].lower() != stk.pop():
#                     return False
        

#         return True
