
def perms(rem, cases, seen):
    if rem == "":
        cases.add(seen)
    for i, v in enumerate(rem):
        perms(rem[:i]+rem[i+1:], cases, seen+v)


def all_perms(string):
    cases = set()
    perms(string, cases, seen="")
    return cases



# def all_perms(string):
#     if len(string) < 2:
#         return set([string])
#     # seen.add(string[-1]+all_perms(string[:-1], seen))
#     # seen.add(all_perms(string[:-1], seen)+string[-1])
#     seen = set()
#     for word in all_perms(string[:-1]):
#         for i, _ in enumerate(string): 
#             seen.add(word[:i]+string[-1]+word[i:])
#     return seen
  

    
if __name__ == "__main__":
    print (all_perms('abcd'))