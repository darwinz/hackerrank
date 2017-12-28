"""
You're given the pointer to the head nodes of two linked lists. Compare the data in the nodes of the linked lists to check if they are equal. The lists are equal only if they have the same number of nodes and corresponding nodes contain the same data. Either head pointer given may be null meaning that the corresponding list is empty.

Input Format
You have to complete the int CompareLists(Node* headA, Node* headB) method which takes two arguments - the heads of the two linked lists to compare. You should NOT read any input from stdin/console.

Output Format
Compare the two linked lists and return 1 if the lists are equal. Otherwise, return 0. Do NOT print anything to stdout/console.

Sample Input

NULL, 1 --> NULL
1 --> 2 --> NULL, 1 --> 2 --> NULL

Sample Output

0
1
Explanation
1. We compare an empty list with a list containing 1. They don't match, hence return 0.
2. We have 2 similar lists. Hence return 1.
"""


def compare_lists(head_a, head_b):
    if not head_a and not head_b:
        return 1
    elif not head_a or not head_b:
        return 0

    return int(head_a.data == head_b.data and compare_lists(head_a.next, head_b.next))
