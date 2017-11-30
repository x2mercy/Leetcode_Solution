#time limit exceed
class Solution(object):
    def groupAnagrams(self,strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        words={}
        for i in range(len(strs)):
        
            if str(sorted(strs[i])) in words.keys():
                words[str(sorted(strs[i]))].append(strs[i])
            else:
                words[str(sorted(strs[i]))]=[]
                words[str(sorted(strs[i]))].append(strs[i])
        result=[]
        for i in words.keys():
            result.append(words[i])
        return result
