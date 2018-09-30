class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        def myp(x,n):
            # print(n)
            k=n
            if n==0:
                return 1
            if n==1:
                return x
            if n%2==0:
                res=myp(x,n/2)
                # print('returning',res*res)
                return res*res
            else:
                res=myp(x,(n-1)/2)
                # print('ret',res*x)
                return res*res*x
        if n>0:
            return myp(x,n)
        else:
            return 1/myp(x,-n)


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1
        sign = -1 if n < 0 else 1
        n = abs(n)
        res = 1
        while n:
            if n%2 == 0:
                x = x*x
                n/= 2
            else:
                res*= x
                n-= 1
        return res if sign > 0 else 1/res


    class Solution:
    def myPow(self, x, n):

        """
        :type x: float
        :type n: int
        :rtype: float
        """
        
        if not n:
            return 1.0
        
        inv = False if n > 0 else True
        if inv:
            n = -n
        
        res = 1
        while n:
            if not n%5:
                x = x*x*x*x*x
                n //= 5
            if not n%4:
                x = x*x*x*x
                n //= 4
            if not n%3:
                x = x*x*x
                n //= 3
            if not n%2:
                x = x*x
                n //= 2
            else:
                res *= x
                n -= 1

        return res if not inv else 1/res
            
