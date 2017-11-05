class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s.strip():
            return 0
        else:
            words=s.split()
            last_word=words[len(words)-1]
            return len(last_word)
            
