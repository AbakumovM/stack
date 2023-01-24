class Stack:

    def __init__(self):
         self.items = []

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        return False

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def brackets_balance(text):
    s = text
    stack = Stack()
    for i in s:
        if i in '({[':
            stack.push(i)
        elif i in ')}]':
            if stack.size() == 0:
                return 'Несбалансированно'
            if (stack.peek() == '('  and i == ')') or (stack.peek() == '{'  and i == '}') or (stack.peek() == '['  and i == ']'):
                stack.pop()
            else:    
                return 'Несбалансированно'
    if stack.size() == 0:
        return 'Сбалансированно'
    return 'Несбалансированно'


def test_1():

    list_input_true = [
        '(((([{}]))))',
        '[([])((([[[]]])))]{()}',
        '[([])((([[[]]])))]{()}',
    ]
    
    list_input_false = [
       '}{}',
       '{{[(])]}}',
       '[[{())}]'
    ]
    for i in list_input_false:
        assert brackets_balance(i) == 'Несбалансированно'

    for j in list_input_true:
        assert brackets_balance(j) == 'Сбалансированно'


if __name__ == '__main__':
    test_1()