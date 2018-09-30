

# def largest_diff(arr):
#     small = arr[0]
#     large = arr[0]
#     s_ind = 0
#     l_ind = 0

#     for i, val in enumerate(arr[1:])
#         if small > val:
#             small = val 
#             s_ind = i
#         if large < val:
#             large = val
#             l_ind = i
#     if s_ind > l_ind:
#         s_ind, l_ind = l_ind, s_ind
#     return (s_ind, l_ind)
def get_max_diff(arr):
    # s_ind = 0
    # l_ind = 1
    # diff = arr[l_ind]-arr[s_ind]

    # for j, j_val in enumerate (arr):
    #     for i in range(j):
    #         this_diff = j_val-arr[i]
    #         print (this_diff, diff)
    #         if this_diff > diff:
    #             s_ind = i
    #             l_ind = j
    #             diff = this_diff

    # return diff, s_ind, l_ind
    mid = 0
    l_ind = 0
    s_ind = 0
    while j < len(arr):
        if arr[j] >arr[l_ind]:
            l_ind = j
            mid = j
        j += 1

    for i in range(mid):
        if arr[i] < arr[s_ind]:
            s_ind = i

    return (arr[l_ind]-arr[s_ind], s_ind, l_ind)
            


    # s_ind = 0
    # l_ind = 1
    # diff = arr[l_ind]-arr[s_ind]
    # print ("dif", diff)
    # i = 0
    # j = 1
    # while (j < len(arr)):
    #     if arr[j] < arr[l_ind]:
    #         j += 1
    #         continue
    #     print (j)
    #     i = s_ind
    #     while i < j:
    #         this_diff = arr[j]-arr[i]
    #         print (this_diff, diff)
    #         if this_diff > diff:
    #             s_ind = i
    #             l_ind = j
    #             diff = this_diff
    #         i += 1
    #     j += 1

    # min_s = min(arr)
    # ind_s = arr.index(min_s)
    # max_s = max(arr[ind_s:])
    # ind_sl = arr.index(max_s, ind_s)
    # diff1 = max_s-min_s

    # max_2 = max(arr)
    # ind_2 = arr.index(max_2)
    # min_2=min(arr[:max_2])
    # ind_ss = arr.index(min_2)
    # diff2 = max_2 - min_2

    # print (diff1, diff2)
    # if diff1 > diff2:
    #     return diff1, ind_s, ind_sl
    # return diff2, ind_ss, ind_2

    # for j, j_val in enumerate (arr):
    #     if arr[l_ind]>= j_val:
    #         j += 1
    #     else:
    #         for i in range(j):
    #             if arr[i] >= arr[s_ind]:
    #                 i += 1
    #             else:
    #                 this_diff = arr[j]-arr[i]
    #                 print (this_diff, diff)
    #                 if this_diff > diff:
    #                     s_ind = i
    #                     l_ind = j
    #                     diff = this_diff

    # return diff, s_ind, l_ind


if __name__ == "__main__":
    # arr = [-2,-1,-3,-4]
    arr = [-2,-1,-3,-4]
    print (get_max_diff(arr))



    # for j, j_val in enumerate (arr):
    #     if arr[j]<= j_val:
    #         continue
    #     else:
    #         for i in range(j):
    #             if arr[i] >= arr[s_ind]:
    #                 continue
    #             else:
    #                 this_diff = j_val-arr[i]
    #                 print (this_diff, diff)
    #                 if this_diff > diff:
    #                     s_ind = i
    #                     l_ind = j
    #                     diff = this_diff
    
    
    
    
    # for j, j_val in enumerate (arr):
    #     for i in range(j):
    #         this_diff = j_val-arr[i]
    #         print (this_diff, diff)
    #         if this_diff > diff:
    #             s_ind = i
    #             l_ind = j
    #             diff = this_diff