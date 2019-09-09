class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def two_pointer():
    head = ListNode(-1)
    sp = head
    fp = head
    while sp and fp and fp.next:
        sp = sp.next
        fp = fp.next.next
        if sp == fp:
            return True
    return False
