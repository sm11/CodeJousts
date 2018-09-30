from collections import namedtuple

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
    
    pointers = namedtuple('pointer', '')
    split_list(head, pointers)
    pointers.head = merge_sort_linked(pointers.head)
    pointers.mid = merge_sort_linked(pointers.mid)

    return merge(pointers.head, pointers.mid)


def split_list(head, point):
    if not head or not head.next:
        point.head = head
        point.mid = None
    else:
        slow = head
        fast = head.next

        while fast:
            fast = fast.next

            if fast:
                slow = slow.next
                fast = fast.next
        
        point.head = head
        point.mid = slow.next
        slow.next = None
        
"""
Alternative without named tuples
"""

# def merge_sort(head):
#     if not head or not head.next:
#       return head
    
#     beg, mid = split_list(head)
#     first_half = merge_sort(beg)
#     second_half = merge_sort(mid)
    
#     return merge(first_half, second_half)


# def split_list(head):
#     if not head or not head.next:
#         return (head, None)
    
#     slow = head
#     fast = head.next

#     while fast:
#         fast = fast.next

#         if fast:
#             slow = slow.next
#             fast = fast.next
            
#     mid = slow.next
#     slow.next = None
    
#     return (head, mid)
            
    
    
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

    nodeA1.print_list()

    s = (merge_sort_linked(nodeA1))
    s.print_list()


