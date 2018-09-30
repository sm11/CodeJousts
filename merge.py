def merge(arr1, arr2):
    arr3 = []
    c1 = 0
    c2 = 0

    while c1 < len(arr1) and c2 < len(arr2):
        if arr1[c1] < arr2[c2]:
            arr3.append(arr1[c1])
            c1 += 1
        else:
            arr3.append(arr2[c2])
            c2 += 1
        
    if c1 < len(arr1):
        arr3.extend(arr1[c1:])
    else:
        arr3.extend(arr2[c2:])

    return arr3


def merge_in(a1, a2):
    a3 = a1 + a2
    count = 0
    print (a3)
    for idx in range(len(a1), len(a3)):
        val = a3[idx]
        pos = idx

        while a3[pos-1] > val:
            a3[pos] = a3[pos-1]
            pos -= 1
        a3[pos] = val
    return a3
    



if __name__ == "__main__":
    arr1 = [1, 3, 4, 5]
    arr2 = [2, 4, 6, 8]

    print (merge_in(arr1, arr2))



    # for el1 in arr1:
    #     for el2 in arr2:
    #         if el1 < el2:
    #             arr3.append()

