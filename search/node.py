class Node:
    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __str__(self):
        return '--Node {0}--\n\tParent: {1}\n\tAction: {2}\n\tCost: {3}' \
               .format(self.state, self.parent, self.action, self.cost)
    
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
    
