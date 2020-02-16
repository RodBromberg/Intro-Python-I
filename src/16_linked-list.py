class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


a = ListNode(5)
a.next = ListNode(10)
a.next.next = ListNode(15)

b = ListNode(8)
b.next = ListNode(10)
b.next.next = ListNode(12)


def search_list(L, key):
    while L and L.val != key:
        L = L.next
    return L


def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


def delete_after(node):
    node.next = node.next.next


# delete_after(a)

# print(a.next.val)
# print(search_list(a, 10))

def mergeTwoLists(l1, l2):
    dummyHead = ListNode(-1)
    head = dummyHead

    while l1 and l2:
        if l1.val <= l2.val:
            dummyHead.next = l1
            l1 = l1.next
        else:
            dummyHead.next = l2
            l2 = l2.next
        dummyHead = dummyHead.next

        if l1:
            dummyHead.next = l1

        if l2:
            dummyHead.next = l2

    return head.next
