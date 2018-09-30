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
    

if __name__ == "__main__":
    array=[33, 6, 21, 12, 19, 29, 38, 22, 14, 40]
    print (array)
    quick_sort(array)
    print(array)