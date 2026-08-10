class Stack:
    def __init__(self) -> None:
        self.stack: list = []

    # Exercise 1 - size(), pop(), push(), peek()
    # Exercise 2 - methods should work with the head of the list
    def size(self) -> int:
        # Method left as-is. No changes from the base template.
        return len(self.stack)

    # Exercise 4 - complexity measures
    # If the Python list is implemented as dynamic array then complexity
    # for the pop() and push() operations should be:
    # Space complexity: O(n)
    # Time complexity:  O(n)
    # Due to working with the head of the list instead of the tail
    # every pop() or push() requires copying all the elements of the array.
    def pop(self):
        if self.size() == 0:
            return None
        return self.stack.pop(0)

    def push(self, value) -> None:
        self.stack.insert(0, value)

    def peek(self):
        if self.size() == 0:
            return None
        return self.stack[0]

# Exercise 3
#
# while stack.size() > 0:
#    print(stack.pop())
#    print(stack.pop())
#
# If the initial size of the stack is even -- the cycle will print out the
# contents of the stack as usual.
# If the initial size is odd -- the cycle will print out the contents and
# an additional "None" at the end, as it will try to pop() the stack when
# it is empty.



