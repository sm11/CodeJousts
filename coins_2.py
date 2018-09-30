import unittest
  

def add_denom(amount, denom, sofar=[], count=0):

    # Calculate the number of ways to make change
    if len(denom) == 0:
        #print ("here", count)
        return count
   
    highest = denom[-1]
    #print (sofar, count)
    if highest+sum(sofar) > amount:
        #print (denom[:-1])
        return add_denom(amount, denom[:-1], sofar, count)
    else:
        sofar.append(highest)
        #print (sofar)
        if sum(sofar) == amount:
            print (sofar)
            count += 1
            return add_denom(amount, denom[:-1], sofar=sofar[:-1], count=count)
        elif sum(sofar) < amount:
            return add_denom(amount, denom, sofar, count)
    
    #return count

def change_possibilities(amount, denominations):
    tot = 0
    denom = sorted (denominations)
    while len(denom):
        tot += add_denom(amount, denom, sofar=[], count=0)
        denom = denom[:-1]
    return tot


    

if __name__ == "__main__":
    print (change_possibilities(6, (1, 2,3)))
















# # Tests

# class Test(unittest.TestCase):

#     def test_sample_input(self):
#         actual = change_possibilities(4, (1, 2, 3))
#         expected = 4
#         self.assertEqual(actual, expected)

#     def test_one_way_to_make_zero_cents(self):
#         actual = change_possibilities(0, (1, 2))
#         expected = 1
#         self.assertEqual(actual, expected)

#     def test_no_ways_if_no_coins(self):
#         actual = change_possibilities(1, ())
#         expected = 0
#         self.assertEqual(actual, expected)

#     def test_big_coin_value(self):
#         actual = change_possibilities(5, (25, 50))
#         expected = 0
#         self.assertEqual(actual, expected)

#     def test_big_target_amount(self):
#         actual = change_possibilities(50, (5, 10))
#         expected = 6
#         self.assertEqual(actual, expected)

#     def test_change_for_one_dollar(self):
#         actual = change_possibilities(100, (1, 5, 10, 25, 50))
#         expected = 292
#         self.assertEqual(actual, expected)


# unittest.main(verbosity=2)import unittest

