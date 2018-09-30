def detectLoop(arr):
    isLoop = False
    lena = len(arr)
    slow = 0
    fast = 1

    while slow:
        pass

    return isLoop



# 2 3 4 2 5 6


def hasCycle(head):
    if head.next == None:
        return False

    slow = head
    fast = head.next

    while (slow != fast):
        if fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    
    return True