from Graph import Node, Graph

def minimax(node, maxmizingPlayer):
    if len(node.children)==0:
        return node
    if maxmizingPlayer:
        node.value = -100000
        for child in node.children:
            temp = minimax(child,False)
            node.value = max(temp.value,node.value)
        return node
    else:
        node.value = 100000
        for child in node.children:
            temp = minimax(child,True)
            node.value = min(temp.value,node.value)
        return node


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
    minimax(g.nodes[0], True)
    print(g.nodes[0].value)
