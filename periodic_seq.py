# A periodic sequence s is defined as follows:

# s[0], a, b and m are all given positive integers;
# s[i] for i > 0 is equal to (a * s[i - 1] + b) mod m.
# Find the period of s, i.e. the smallest integer T such that for each i > k (for some integer k): s[i] = s[i + T].

# Example

# For s0 = 11, a = 2, b = 6, and m = 12, the output should be
# periodicSequence(s0, a, b, m) = 2.

# The sequence would look like this: 11, 4, 2, 10, 2, 10, 2, 10, 2, 10....

# For s0 = 1, a = 2, b = 3, and m = 5, the output should be
# periodicSequence(s0, a, b, m) = 4.

# The sequence would look like this: 1, 0, 3, 4, 1, 0, 3, 4, 1, 0, 3, 4....

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] integer s0

# a positive integer representing s[0].

# Guaranteed constraints:
# 1 ≤ s0 ≤ 100,
# s0 < m.

# [input] integer a

# Guaranteed constraints:
# 2 ≤ a ≤ 100.

# [input] integer b

# Guaranteed constraints:
# 2 ≤ b ≤ 100.

# [input] integer m

# Guaranteed constraints:
# 5 ≤ m ≤ 100.

# [output] integer

# The sequence period.

from collections import defaultdict

def periodicSequence(s0, a, b, m):
    #seq = {s0: 0}
    seq = defaultdict(int)
    seq.setdefault(s0,1)
    seq_l = [s0]
    # m = 100
    
    for i in range (1, m*5):
        res = (a * seq_l[i-1] + b )% m
        seq_l.append(res)
        seq[res] += 1
    
    rev_seq = seq_l[::-1]
    not_found = True
    count  = 0
    seen = 0
    period = 0
    # print (rev_seq)
    while not_found and period < m:
        period += 1        
        for count in range(6):
            if rev_seq[count] == rev_seq[count + period]:
                # print (rev_seq[count], rev_seq[count + period])
                seen += 1
                # print ('this', period)
            if seen == 6:
                not_found = False
                # period = period
                break
    print ('p', period)




    # print (seq)
    print (rev_seq)
    return period

def principal_period(modlist):
    a = ''.join(str(m) for m in modlist)
    i = (a+a).find(a,1, -1)
    return None if i == -1 else a[:i]

if __name__ == "__main__":
    s0 = 11
    a = 2
    b = 6
    m = 12
    # (a * s[i - 1] + b) mod m

   
    # for i in range(1, 14):
    periodicSequence(s0, a, b, m)
    # print ('seq', seq)

    s0 = 1
    a = 2
    b = 3
    m = 5
    print ('_'*30)
    print()
    
    # for i in range(1, 14):
    periodicSequence(s0, a, b, m)
    
    # periodicSequence(s0, a, b, m) = 4.
    # a = [ 2, 10, 2, 10, 2, 10, 2, 10, 2, 10, 2, 10, 2, 10]
    # seq = principal_period(a)
    # print ('seq', seq)

   