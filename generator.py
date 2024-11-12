from copy import deepcopy

from classes.node import NumNode
from classes.storage import NodeStorage


def main():
    first_node = NumNode(1)

    node_storage: NodeStorage = NodeStorage("graph")
    node_storage.add_node(first_node)

    working_list: list[NumNode] = [first_node]

    while True:
        next_list: list[NumNode] = []

        for node in working_list:
            created_nodes: list[NumNode] = []

            created_nodes.append(NumNode(node.value * 2))

            if (node.value - 1) % 3 == 0 and node.value - 1 != 0:
                created_nodes.append(NumNode((node.value - 1) // 3))

            for c_node in created_nodes:
                if node_storage.check(c_node):
                    temp_node = node_storage.get(c_node)
                    temp_node.add_from(node.value)
                    node_storage.add_node(temp_node)
                else:
                    c_node.add_from(node.value)
                    node_storage.add_node(c_node)
                    next_list.append(c_node)

        working_list = deepcopy(next_list)


if __name__ == '__main__':
    main()
