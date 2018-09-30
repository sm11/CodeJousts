# from collections import namedtuple

class ListNode(object):
    def __init__(self, value):
        self.data = value
        self.next = None

    def print_list(node):
        curr = node
        while curr.next:
            print (curr.data, end=' -> ')
            curr = curr.next
        print(curr.data)

def merge_sort_linked(head):
    if not head or not head.next:
        return head
    
    arr = []   # array of nodes
    result = head
    
    while result:
        temp = result.next
        result.next = None
        # if temp:
        #     print ('temp', end = " ")
        #     temp.print_list()
        if result:
            # print (type(result))
            print("res", end = " ")
            result.print_list()
        for idx, node in enumerate(arr):
            if node:
                print ('idx', idx)
                node.print_list()
                result = merge(node, result)
                print ('res2', end = " ")
                result.print_list()
                arr[idx] = None
        arr.append(result)
        
        print ('arr', [i.data if i else 'None' for i in arr])
        print ('__'*8)
        result = temp
    return arr[-1]


# def merge_sort_linked(head):
#     if not head or not head.next:
#         return head
#     arr = []
#     result = head
    
#     while result:
#         temp = result.next
#         result.next = None
#         # i = 0
#         for idx, node in enumerate(arr):
#             if node:
#                 result = merge(node, result)
#                 arr[idx] = None
#             # i += 1
#         # if i == len(arr):
#         #     i -= 1
#         arr.append(result)
#         result = temp
#     #result = None
#     #for node in arr:
#     #    result = merge(node, result)
#     return result
    
def merge(head1, head2): 
    if not head1:
        return head2
    if not head2:
        return head1
    
    head3 = None

    if head1.data < head2.data:
        head3 = head1
        head1 = head1.next
    else:
        head3 = head2
        head2 = head2.next

    curr = head3
    while head1 and head2:
    
        if head1.data < head2.data:
            curr.next = head1
            head1 = head1.next
        else:
            curr.next = head2
            head2 = head2.next
        curr = curr.next
    
    if head1:
        curr.next = head1
    elif head2:
        curr.next = head2

    return head3


if __name__ == "__main__":
    nodeA1 = ListNode(2)

    nodeA2 = ListNode(1)
    nodeA1.next = nodeA2

    nodeA3 = ListNode(9)
    nodeA2.next = nodeA3

    nodeA4 = ListNode(3)
    nodeA3.next = nodeA4

# Node C:
    nodeC1 = ListNode(5)
    nodeA4.next = nodeC1

    nodeC2 = ListNode(6)
    nodeC1.next = nodeC2

    

    nodeC3 = ListNode(4)
    nodeC2.next = nodeC3

    nodeC4 = ListNode(5)
    nodeC3.next = nodeC4

    nodeC5 = ListNode(-1)
    nodeC4.next = nodeC5

    nodeA1.print_list()

    s = (merge_sort_linked(nodeA1))
    s.print_list()


