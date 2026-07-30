from task1 import Node, LinkedList


# Task 1 - exercise *1.8 - Sum of two linked lists of integers
# Space complexity: O(n)
# Time complexity: O(n)
def sum_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    result: LinkedList = LinkedList()
    length: int = list1.len()
    if length != list2.len():  # Sum only if lengths match
        return result
    node1: Node | None = list1.head
    node2: Node | None = list2.head
    for i in range(length):
        value: int = node1.value + node2.value
        result.add_in_tail(Node(value))
        node1 = node1.next
        node2 = node2.next
    return result



