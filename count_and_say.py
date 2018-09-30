class Solution:
    def __init__(self):
        self.memo = dict()
        self.memo[1] = '1'
        
    def count(self, strn):
        count = 1
        output = ""
        for i, v in enumerate(strn[:-1]):
            if v == strn[i+1]:
                count += 1
            else:
                output += str(count)+v
                count = 1
        output += str(count) + strn[-1]
        return output       
    
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """

        for i in range(1, n+1):
            check = self.memo[i]
            self.memo[i+1] = self.count(check)
        return self.memo[n]