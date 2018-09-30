#!/bin/python

import sys
import unittest
from collections import defaultdict
from copy import deepcopy

# Complete the function below.

word_dic = defaultdict(list)

def setup(words):
    # preprocessing
    # dict(key=len, val = [list of words of len])
    global word_dic
    
    for el in words:
        word_dic[len(el)].append(el)

def isMember(w):
    global word_dic
    # words is accessible here
  
    indices = [idx for idx, val in enumerate(w) if val == '.']
    wordList = deepcopy(word_dic[len(w)])   #Prevent changes to actual entries in global dictionary
    w = "".join(x for x in w if x != '.')
    for idx, el in enumerate(wordList):
       wordList[idx] = "".join(x for ind,x in enumerate(el) if ind not in indices)
    return w in set(wordList)
   
class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(isMember('f.o.d'), False)   
        self.assertEqual(isMember('f.o'), True)  
        self.assertEqual(isMember('..'), False)
        self.assertEqual(isMember('hello'), False)  
        self.assertEqual(isMember('foo'), True)

if __name__ == "__main__":
    setup(["foo", "bar", "baz", "food"])
    # print (isMember('f.o.d'))
    # print (isMember("f.o"))
    # print (isMember(".."))
    # print (isMember("foo")) # true
    # print (isMember("hello")) # false
    # isMember("f.o") # true matches foo
    # isMember("..") # false because no two character words
    # test = Test()
    # test.test()
    unittest.main()
    
        
        
 #word_dic = {len(el): word_dic[len(el)].append(el) if len(el) in word_dic else [el] for el in words}
            
                
            
            
        

    
   
    




