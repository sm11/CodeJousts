class Fib:
    def __init__(self):
        self.memo = {}

    def fibon(self,n):
        if n in [0,1]:
            return n
        if n in self.memo:
            return self.memo[n]
        res = self.fibon(n-1) + self.fibon(n-2)
        self.memo[n] = res
        return res


if __name__ == "__main__":
    fib = Fib()
    print (fib.fibon(6))