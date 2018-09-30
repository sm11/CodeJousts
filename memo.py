class Fib:
    def __init__(self):
        self.memo = {}


    def fib(self, num):
        if num in self.memo:
            return self.memo[num]
        if num in [0,1]:
            self.memo[num] = num
            return num
        val = self.fib(num-1) + self.fib(num-2)
        self.memo[num] = val
        return val
        
def fib(num):
    memo = {}
    memo[0] = 0
    memo[1] = 1

    for i in range (2, num+1):
        memo[i] = memo[i-1] + memo[i -2]    
    return memo[num]

if __name__ == "__main__":
    f = Fib()
    print (f.fib(0))
    print (f.fib(1))
    print (f.fib(2))
    print (f.fib(3))
    print (f.fib(4))
    print (fib(4))