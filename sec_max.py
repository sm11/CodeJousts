# -*- coding: utf-8 -*-

def sec_max(arr):
    if len(arr) < 2:
        return None
    #fir = max(arr)
    #arr.remove(fir)
    #sec = max(arr)
    fir, sec = arr[0], None
    for a in arr[1:]:
        if a >= fir:
            sec, fir = fir, a 
        elif not sec:
            sec = a
        elif a > sec:
            sec = a

    return sec


if __name__ == "__main__":
   arr = [-2, -1]
   print (sec_max(arr))
   test(arr)



#    fir, sec = arr[1], None
#    for a in arr[1:]:
#        if a >= arr[1]:
#            sec, fir = fir, a 
#    return sec
