def reverseNodesInKGroups(A, K):
    cur = A
    for _ in xrange(K):
        if not cur: return A
        cur = cur.next
    
    ans, cur = A, A.next
    for _ in xrange(K-1):
        cur.next, cur, ans = ans, cur.next, cur
    A.next = reverseNodesInKGroups(cur, K)
    return ans


    # Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#



def reverseNodesInKGroups(l, k):
    
    if not l:
        return l
    c = l
    n = k
    while c and n:
        c = c.next
        n -= 1
    if n:
        return l
    curr = l
    prev = None
    next = None
    n = k
    while curr and n:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        n -= 1
    if next:
        l.next = reverseNodesInKGroups(next, k)
    return prev


# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseList(head, tail):
    prev = None
    while prev != tail:
        prev, prev.next, head = head, prev, head.next
    return prev
    
def reverseNodesInKGroups(l, k):
    if k < 2:
        return l
    
    p = ListNode(-1)
    p.next = l
    ret = p
    while True:
        flag = True
        tmp = p
        for i in range(k):
            if tmp.next:
                tmp = tmp.next
            else:
                flag = False
                break
        
        if flag:
            q = tmp.next
            t = p.next
            reverseList(t, tmp)
            p.next = tmp
            t.next = q
            p = t
        else:
            break
    
    return ret.next


# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

def iter(pointer, stop):
    head = pointer
    temp = pointer
    pointer = pointer.next
    while pointer != stop:
        temp.next = pointer.next
        pointer.next = head
        head = pointer
        pointer = temp.next
    return(pointer, stop, temp, head)

 # Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#

# def iter(pointer, stop, temp, l):
#     while pointer != stop:
#         temp.next = pointer.next
#         pointer.next = l
#         l = pointer
#         pointer = temp.next
        

def reverseNodesInKGroups(l, k):
    if k < 2:
        return l
    
    pointer, stop = l, l
    end = 1
    first_k = True
    
    while stop:
        while end < k and stop:
            stop = stop.next
            end += 1
        if end == k:
            end = 1
            if first_k:
                first_k = False
                stop = stop.next
                temp = pointer
                pointer = pointer.next
                while pointer != stop:
                    temp.next = pointer.next
                    pointer.next = l
                    l = pointer
                    pointer = temp.next
                
                
            else:
                end_hold = temp
                new_head = pointer
                temp = pointer
                pointer = pointer.next
                while pointer != stop:
                    temp.next = pointer.next
                    pointer.next = new_head
                    new_head = pointer
                    pointer = temp.next
                end_hold.next = new_head
            if stop:
                stop = stop.next
    return l
            

       

def reverseNodesInKGroups(l, k):
    if k < 2:
        return l
    
    pointer, stop = l, l
    end = 1
    first_k = True
    
    while stop:
        while end < k and stop:
            stop = stop.next
            end += 1
        if end == k:
            end = 1
            if first_k:
                first_k = False
                stop = stop.next
                pointer, stop, temp, l = iter(pointer, stop)
            else:
                end_hold = temp
                pointer, stop, temp, new_head = iter(pointer, stop)
                end_hold.next = new_head
            if stop:
                stop = stop.next
    return l
            

