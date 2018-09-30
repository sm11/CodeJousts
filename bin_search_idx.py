def binary_search_rec(a, key, start, end):
  #TODO: Write - Your - Code
  if len(a):
    start = start
    end = end
    mid = (start + end)//2

    if key == a[mid]:
        return mid
    if key < a[mid]:
        return binary_search(a, key, start, mid-1)
    if key > a[mid]:
        return binary_search(a, key, mid+1, end)
  
  return -1

def binary_search_it(a, key):
    # TODO: Write - Your - Code
    
    start = 0
    end = len(a) - 1

    while start <= end:
        mid = (start + end)//2
        if a[mid] == key:
            return mid
        if key < a[mid]:
            end = mid-1
        else:
            start = mid+1

    return -1
   


if __name__ == "__main__":
  arr = [5, 3, 2, 9, 7]
  arr = [2,3,4,4,4,4,4,4,5,6,7,7,7,7,9]
  print (binary_search(arr, 5, 0, len(arr)-1))
#   binary_search(arr, 15)