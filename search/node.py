class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __str__(self):
        return self._str_indented()

    def _str_indented(self, indent_level=0):
        indentation = '  ' * indent_level
        parent_indented = self.parent._str_indented(indent_level + 1) if self.parent is not None else '    --None--'
        return '{0}--Node {1}--\n{0}  Parent:{{\n{0}{2}\n{0}  }}\n{0}  Action: {3}\n{0}  Cost: {4}' \
                .format(indentation, self.state, parent_indented, self.action, self.cost)
    
    def path(self):
        n = self
        solution_reversed = []
        while n.parent is not None:
            solution_reversed.append(n.action)
            n = n.parent
        solution_reversed.reverse()
        return solution_reversed

if __name__ == '__main__':
    n1 = Node('n1', None, 'South')
    n2 = Node('n2', n1, 'West')
    print n2.path()
    
