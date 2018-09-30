import re
num = 0
def shoppingList(items):
    num = re.findall(r"[-+]?\d*\.\d+|\d+", items)
    num = [float(n) for n in num]
    print (num)
    return sum(num)

