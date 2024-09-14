class Solution:
    def expand(self, s: str) -> List[str]:
    
        
        ex = []
        
        res = []
        def dfs(i, curArr):
            if i >= len(s):
                cur = ""
                for char in curArr:
                    cur += char
                res.append(cur)
                return
            
            
            if s[i] == "{":
                i += 1
                options = []
                
                while s[i] != "}":
                    if s[i] != ",":
                        heapq.heappush(options, s[i])
                    i += 1
                
                while len(options) > 0:
                    copy = curArr.copy()
                    copy.append(heapq.heappop(options))
                    dfs(i + 1, copy)
                
            else:
                copy = curArr.copy()
                copy.append(s[i])
                dfs(i + 1, copy)
        
        dfs(0, [])
        return res

