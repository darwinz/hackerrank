"""
 Insert Node at the end of a linked list
 head pointer input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method
"""

import Node


def insert(head, data):
    if head is None:
        head = Node(data)
    else:
        current = head
        while current.next is not None:
            current = current.next
        current.next = Node(data)
    return head
