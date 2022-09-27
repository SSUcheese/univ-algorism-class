class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def add(self):
        node = head
        while node.next:
            node = node.next
        node.next = ListNode(self)


node1 = ListNode(1)
head = node1
ListNode.add(3)

node = head

while node.next:
    print(node.data)
    node = node.next
print(node.data)
