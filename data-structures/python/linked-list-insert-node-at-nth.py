"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.

 This is a "method-only" submission.
 You only need to complete this method.
"""

import Node


def InsertNth(head, data, position):
    if position == 0:
        return Node(data, head)

    current = head
    prev = Node()
    p = Node(data, None)
    pos = 0
    while current:
        pos += 1
        prev = current
        current = current.next
        if pos == int(position):
            prev.next = p
            p.next = current
            return head
