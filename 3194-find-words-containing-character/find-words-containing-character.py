class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        
        word_dict = [set(word) for word in words]
        ans = [i for i, word in enumerate(word_dict) if x in word]
        return ans
