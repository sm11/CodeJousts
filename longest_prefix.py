class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        short = (sorted(strs, key =lambda x: len(x)))[0]
        slen = len(short)
        let = ""

        for word in strs:
            if word[:slen] == short:
                continue
            else:
                for i, letter in enumerate(word[:slen]):
                    if letter == short[i]:
                        let += letter
                    else:
                        break
                short = let
                slen = len(short)
                let = ""


        return (short)


 def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest 

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        prefix = []
        for chars in zip(*strs):
            charset = set(chars)
            if len(charset) == 1:
                prefix.append(charset.pop())
            else:
                break
            
        return "".join(prefix)
        
        
    class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
				
        if not strs:
            return ''
						
        prefix = ''
        min_len = len(min(strs, key=len))
        if min_len == 0:
            return ''
	
        n = 0
        nth_chars = set([a[0] for a in strs])
        while len(nth_chars) == 1 and n <= min_len:
            prefix += strs[0][n]
            n += 1
            if n == min_len:
                break
            nth_chars = set([a[n] for a in strs])
        return prefix