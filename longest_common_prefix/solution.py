#reference:https://github.com/RealHacker/leetcode-solutions/blob/master/014_longest_common_prefix/longest_common_prefix.py
class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        else:
           sort_strs=sorted(strs)
           prefix=sort_strs[0]
           for i in sort_strs[1:]:
                while not i.startswith(prefix):
                    prefix=prefix[:-1]
                if not prefix:
                    break
        return prefix
