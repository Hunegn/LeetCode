class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        st1 = ''
        for word in word1:
            st1+=word
        st2 = ''
        for word in word2:
            st2+= word
        return st1== st2