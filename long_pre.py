def longestCommonPrefix1(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        shortest = min(strs,key=len)
        print (shortest)
        for i, ch in enumerate(shortest):
            print ('c', ch)
            for other in strs:
                if other[i] != ch:
                    print (other[i])
                    return shortest[:i]
        return shortest 



def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if not len(strs):
        return ''
    
    short = min(strs, key=len)
    print(strs, short)
    
    slen = len(short)
    let = ""
    
    for word in strs:
        if word[:slen] == short:
            continue
        else:
            for i, letter in enumerate(word):
                if letter == short[i]:
                    let += letter
                else:
                    break
            short = let
            slen = len(short)
            let = ""


    return short           
    
    # end_ = '*'
    # count = 0
    # trie = dict()

    # for word in strs:
    #     temp_trie = trie
    #     for letter in word:
    #         temp_trie = temp_trie.setdefault(letter, {})
    #     temp_trie[end_]=end_ 
    # print (trie)
    # short = ""
    # print (len(trie))
    # for k, v in trie.items():
    #     print (k)
    #     if len(k) == 1:
    #         short += k
    # print ('d', short)
    
    '''
    k = arr[0][0]
    
    while len(trie[k])== 1:
        short+= k
        k = trie[k].ke
        print (k)
                
        

    for word in strs:
        for idx, letter in enumerate(word):
            if trie[letter] = word[idx+1]:
                count += 1
            else:
                break
        if count == len(word)+1 and word != strs[-1]:
            count = 0
        if word == strs[-1]:
            print count
        else:
            print ("short", count)
    '''                    

if __name__ == "__main__":
    arr = ["flower","flow","flop", "flight"]
    #arr = ["aca","cba"]
    print (longestCommonPrefix(arr))
    
    # short = sorted(arr, key=lambda x:len(x))[0]
    # print(arr, short)
    
    # slen = len(short)
    # let = ""
    
    # for word in arr:
    #     if word[:slen] == short:
    #         continue
    #     else:
    #         for i, letter in enumerate(word[:slen]):
    #             if letter != short[i]:
    #                 print (i)
    #                 print (letter)
    #                 let += letter
    #             else:
    #                 break
    #         short = let
    #         slen = len(short)
                
                
    # print('s', short)
                 
                
            