from timeit import timeit

def merge_sort(a_list):
    if len(a_list) > 1:
        # print ('Splitting', a_list)
        mid = len(a_list)//2
        left = a_list[:mid]
        right = a_list[mid:]

        merge_sort(left)
        merge_sort(right)
        merge(left, right, a_list)


def merge(left, right, a_list):
    # print("Merging {} and {}".format(left, right))
    i, j, k = 0, 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a_list[k] = left[i]
            i += 1
        else:
            a_list[k] = right[j]
            j+= 1
        k += 1

    while i < len(left):
        a_list[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        a_list [k] = right[j]
        j += 1
        k += 1
    

        # return j_list



def quick_sort(a):
  #TODO: Write - Your - Code
  qs_helper(a, 0, len(a)-1)
  return a

def qs_helper(a, start, end):
  if start < end:
    part = get_part(a, start, end)
    qs_helper(a, start, part-1)
    qs_helper(a, part+1, end)

def get_part(a, start, end):
  #if len(a) > 1:

    pivot = a[start]
    left = start+1
    right= end
    while left <= right:
      while(a[left] <= pivot) and (left <= right):
        left += 1
      while (a[right] > pivot): # and (left <= right):
        right -= 1
      if left < right:
        a[left],a[right] = a[right], a[left]
        left += 1
        right -= 1
        
    a[start], a[right] = a[right], a[start]
    return right
    




def quick_sort_median_three(a_list):
    quick_sort_helper(a_list, 0, len(a_list)-1)

def quick_sort_helper(a_list, start, end):
    #if len(a_list) > 1:
    print(a_list)
    if start < end:
        split_point = partition(a_list, start, end)

        quick_sort_helper(a_list, start, split_point-1)
        quick_sort_helper(a_list, split_point+1, end)

  
        
def get_pivot(a_list, start, end):
    mid = (start+end)//2
    beg = a_list[start]
    last = a_list[end]
    cent = a_list[mid]

    print (beg, cent, last)

    if cent <= beg <= last or cent >= beg >= last:
        return (beg, start)
    if beg <= cent <= last or beg >= cent >= last:
        return (cent, mid)
    if cent <= last <= beg or cent >= last >= beg:
        return (last, end)

def partition(a_list, start, end):  
    p_val, p_ind = get_pivot(a_list, start, end) 
    a_list[start], a_list[p_ind] = a_list[p_ind], a_list[start]
    p_val = a_list[start]
    print (p_val, p_ind, start, end)
    # p_val = a_list[start]
    left = start    # if p_ind == start else start
    right = end

    done = False

    while not done:
        while left <= right and a_list[left] <= p_val:
            left += 1
        while right >= left and a_list[right] >= p_val:
            right -= 1
        
        if left > right:
            done = True
        else:
            a_list[left], a_list[right] = a_list[right], a_list[left]
            left += 1
            right -= 1
    # if a_list[right] > a_list[p_ind]:
    a_list[start], a_list[right] = a_list[right], a_list[start]
    
    return right
    # quick_sort(a_list)
    # quick_sort(a_list, right, len(a_list)-1)









def insertion_sort(a_list):
    for idx in range(1, len(a_list)):
        curr = a_list[idx]
        pos = idx

        while pos > 0 and a_list[pos-1] > curr:
            a_list[pos] = a_list[pos-1]
            pos -= 1

        a_list[pos] = curr

    


if __name__ == "__main__":
    reps = 100
    a_list= [54,26,93,17,77,31,44,55,20]
    # merge_sort(a_list)
    insertion_sort(a_list)
    print (a_list)
    # print(timeit("quick_sort([54,26,93,17,77,31,44,55,20])", number=reps,
    #                     setup="from __main__ import quick_sort"))
    # print(timeit("merge_sort([54,26,93,17,77,31,44,55,20])", number=reps,
    #                     setup="from __main__ import merge_sort"))
    # print(timeit("insertion_sort([54,26,93,17,77,31,44,55,20])", number=reps,
    #                     setup="from __main__ import insertion_sort"))
    # print(timeit("bubble_sort([54,26,93,17,77,31,44,55,20])", number=reps,
    #                     setup="from __main__ import bubble_sort"))
