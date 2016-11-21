from algorithms.bst.avl_tree import BinaryNode
from algorithms.bst.avl_tree import BinaryTree


class TestAvlTree:
    def test_can_create_empty_tree_height_is_minus_one(self):
        tree = BinaryTree()

        assert tree.height == -1

    def test_can_create_nodes(self):
        assert BinaryNode('A')

    def test_can_add_sub_node(self):
        root = BinaryNode('A')
        left = BinaryNode('B')
        right = BinaryNode('C')

        root.add(left)
        root.add(right)

        pass
