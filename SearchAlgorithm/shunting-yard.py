class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        popped = self.top.data
        self.top = self.top.next
        return popped

    def peek(self):
        return None if self.is_empty() else self.top.data

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    return 0

def infix_to_postfix(infix):
    stack = Stack()
    postfix_steps = []

    for char in infix:
        if char.isalnum():
            postfix_steps.append(char)
        elif char == '(':
            stack.push(char)
        elif char == ')':
            while not stack.is_empty() and stack.peek() != '(':
                postfix_steps.append(stack.pop())
            stack.pop()  # Pop the '('
        elif is_operator(char):
            while not stack.is_empty() and precedence(stack.peek()) >= precedence(char):
                postfix_steps.append(stack.pop())
            stack.push(char)

    while not stack.is_empty():
        postfix_steps.append(stack.pop())

    result = []
    current_expression = ""
    for step in postfix_steps:
        current_expression += step
        result.append(current_expression)
    return result


infix_expression = "A + B + C"
postfix_expressions = infix_to_postfix(infix_expression)

print("Input infix:", infix_expression)
print("Output postfix:")
for postfix in postfix_expressions:
    print(postfix)
