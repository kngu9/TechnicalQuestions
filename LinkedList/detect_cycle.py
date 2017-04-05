# Given a linked list, determine if there's a cycle
# Time Complexity: O(n)
# Space Complexity: O(1)

from LinkedList import Node

# 1 -> 2 -> 3 -> 4 -> 2
def createLinkedList():
    head = Node(1)
    n2 = Node(2)

    head.next = n2

    n3 = Node(3)
    n2.next = n3

    n4 = Node(4)
    n3.next = n4

    n4.next = n2

    return head

def detectCycle(head):
    s = head
    f = head.next

    while f:
        if s.val == f.val:
            return True

        f = f.next.next
        s = s.next

    return False

if __name__ == '__main__':
    head = createLinkedList()

    isCycle = detectCycle(head)

    print(isCycle)
