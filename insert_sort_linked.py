def ins_sort(head ):
    sorted_list = None
    curr = head

    while curr:
        temp = curr.next
        sorted_list = insert(sorted_list, curr)
        curr = temp
return sorted_list

def insert(new_head, node):
    if not node:
        return new_head

    if not new_head or node.data <= new_head.data:
        node.next = new_head
        return node
    
    curr = new_head
    while curr.next and curr.next.data < node.data:
        curr = curr.next

    node.next = curr.next
    curr.next = node

    return new_head