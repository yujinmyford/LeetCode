class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.maxSuf = 0
        for word in words:
            self.maxSuf = max(self.maxSuf, len(word))
        self.stream = ""
        

    def query(self, letter: str) -> bool:
        self.stream += letter
        
        if len(self.stream) > self.maxSuf:
            self.stream = self.stream[1:]
        
        for word in self.words:
            wordLen = len(self.stream) - len(word)
            suf = self.stream[wordLen:]
            if word == suf:
                return True
        
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
