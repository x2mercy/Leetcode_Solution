class Solution(object):
    def groupAnagrams(self,strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if len(strs)==0:
            return []
        words={}
        for i in range(len(strs)):
            k="".join(sorted(strs[i]))
            if not words.has_key(k):
                words[k]=[]
            words[k].append(strs[i])
        result=[]
        for i in words.keys():
            result.append(sorted(words[i]))
        return result
