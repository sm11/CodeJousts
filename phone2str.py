def phoneNumberToString_corr(digits, mapping):
    import itertools

    #
    # Write your code here.
    #  
    arr_ = [mapping[el] for el in digits]
    arr =  list(itertools.product(*arr_))
    return ["".join(w) for w in arr ]


def phoneNumberToString_bu(digits, mapping, sofar=''):
    #
    # Write your code here.
    #
 
    if len(digits) == 0:
        return [sofar]
    map_ = []
    for el in mapping[digits[0]]:
        map_.extend((phoneNumberToString_td(digits[1:], mapping, sofar+el)))
    #return (([item for sublist in map_ for item in sublist]))   # if append is used
    return (map_)

def phoneNumberToString_td(digits, mapping, sofar=''):
    #
    # Write your code here.
    #
 
    if len(digits) == 0:
        print (sofar)
    map_ = []
    for el in mapping[digits[0]]:
        phoneNumberToString_td(digits[1:], mapping, sofar+el)


def phoneNumberToString_bup(digits, mapping):
    #
    # Write your code here.
    #
 
    if len(digits) == 0:
        return [""]
    map_ = []
    for x in (phoneNumberToString_bu(digits[1:], mapping)):
        for el in mapping[digits[0]]:
            map_.append(el + x)
    
    return (map_)


def phoneNumberToString(digits, mapping):
    #
    # Write your code here.
    #
    map_ = [""]
    while len(digits):
        map_ = [(x+y) for x in map_ for y in mapping[digits[0]]]
        digits = digits[1:]
    return (map_)



def phone_permute_list_count(digits, mapping, count = 0):
    if len(digits) == count:
        return ['']
    else:
        result = []
        for x in phone_permute_list_count(digits, mapping, count + 1):
            print ("x", count, x)
            print (x=='')
            for y in mapping[digits[count]]:   #A B C
                result.append(y + x) #A B C
            print ("result", result)

    print ("l", len(['']))
    return result

d = {'1': ['A', 'B', 'C'], '2': ['D', 'E', 'F'], '3': ['G', 'H', 'I'], '4': ['J', 'K', 'L']}
print (phone_permute_list_count("12", d))

