"""
    Difficulty: [Easy]
    Tags: tree search

    DFS realization
    Speed: 
        all: O(n+e)
        where: n - nodes count
               e - edges count
    Memory:
        all: O(n)
"""

import queue


class Graph:
    def __init__(self):
        self.root_nodes = []
    

class Node:
    def __init__(self, data):
        self.data = data
        self.childs = []
        self.marked = False


def dfs_search(node, search_data):
    if visit(node, search_data) == True:
        return True
    node.marked = True
    for child in node.childs:
        if not child.marked:
            if dfs_search(child, search_data) == True:
                return True
    return False


def visit(node, search_data):
    print(node.data)
    return node.data == search_data


def create_graph():
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')
    nodeF = Node('F')
    nodeG = Node('G')

    nodeA.childs.append(nodeB)
    nodeA.childs.append(nodeC)
    nodeB.childs.append(nodeD)
    nodeC.childs.append(nodeD)
    nodeC.childs.append(nodeE)
    nodeD.childs.append(nodeG)
    nodeE.childs.append(nodeF)
    nodeG.childs.append(nodeF)

    graph = Graph()
    graph.root_nodes.append(nodeA)
    return graph


def main():
    graph = create_graph()
    root_node = graph.root_nodes[0]     # simple graph with one root
    search_data = 'F'
    result = dfs_search(root_node, search_data)
    print("Search data {} found: {}".format(search_data, result))


if __name__ == '__main__':
    main()