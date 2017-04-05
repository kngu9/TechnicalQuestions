# Given a linked list, reverse the linked list in O(n) times.
# Time Complexity O(n)
# Space Complexity O(1)

from LinkedList import Node

def printLinkedList(head):
    print(head.val)

    if(head.next):
        printLinkedList(head.next)

# The idea around this is, say given a linked list: 1 -> 2 -> 3 -> 4
# We are going to save the previous node, and the next node.
# Then we are going to point the next of the current node to the previous node.
# Then we are going to set the current node to the next node, that we saved.
# So it'll look like this for the linked list node: 2
# Prev = 1
# Next = 3
# 1 <- 2 3 -> 4
def reverse(head):
    cur = head
    prev = None

    while cur:
        nxt = cur.next

        cur.next = prev
        prev = cur

        cur = nxt

    return newHead

if __name__ == '__main__':
    # Create the node
    head = Node(1)
    cur = head

    for i in range(1, 11):
        temp = Node(i)

        cur.next = temp
        cur = temp

    printLinkedList(head)

    h = reverse(head)
    
    printLinkedList(h)
