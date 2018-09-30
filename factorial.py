class Factorial:
    def __init__(self):
        self.fact_dict = {0:1}
    
    def fact(self, n):
        if n in self.fact_dict:
            return self.fact_dict[n]
        self.fact_dict[n] = n * self.fact(n-1) % (10**9 + 7)
        return self.fact_dict[n]
    
if __name__ == "__main__":
    f = Factorial()
    print (f.fact(4))



def fact(n):
    global factors

    if len(factors) <= n:
        factors.extend(-1 for i in range(n-len(factors)+1))
    if factors[n] != -1:
        return factors[n]       
    factors[n] = n * fact(n-1) % (10**9 + 7)
    return factors[n] 


    
if __name__ == "__main__":
    #f = Factorial()
    # create(n)

    factors = [1]
    n = 10
    # create()
    print (fact(n))
    print (fact(5))
    print (fact(15))
        
        
    
        
        