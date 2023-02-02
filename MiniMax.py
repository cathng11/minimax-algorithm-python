from Graph import Node, Graph
# import random as rd
def MaxValue(node):
    if len(node.children) == 0:
        return node
    node.value = -100000
    for child in node.children:
        temp = MinValue(child)
        print(temp)
        if temp.value > node.value:
            node.value = temp.value
            print(node.value)
    return node
def MinValue(node):
    if len(node.children) == 0:
        return node
    node.value = 100000
    for child in node.children:
        temp = MaxValue(child)
        if temp.value < node.value:
            node.value = temp.value
    return node
def Minimax_Search(state):
     MaxValue(state)
if __name__ == '__main__':
    g = Graph()
    g.add_node_from([
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N'
    ])
    g.add_edges_from(
        [('A', 'B'),
         ('A', 'C'),
         ('B', 'D'),
         ('B', 'E'),
         ('C', 'F'),
         ('C', 'G'),
         ('C', 'H'),
         ('F', 'I'),
         ('F', 'J'),
         ('G', 'K'),
         ('G', 'L'),
         ('I', 'M'),
         ('I', 'N')]
    )
    g.nodes[3].value = 3
    g.nodes[4].value = 5
    g.nodes[7].value = 4
    g.nodes[9].value = 5
    g.nodes[10].value = 7
    g.nodes[11].value = 8
    g.nodes[12].value = 0
    g.nodes[13].value = 7
    print("------------")
    Minimax_Search(g.nodes[0])
    print(g.nodes[0].value)