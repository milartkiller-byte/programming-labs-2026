class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree:
    if node.right is not None:
        current = node.right
        while current.left is not None:
            current = current.left
        return current

    current = node
    while current.parent is not None and current.parent.right == current:
        current = current.parent

    return current.parent


if __name__ == "__main__":
    root = BinaryTree(10)
    root.left = BinaryTree(5, parent=root)
    root.right = BinaryTree(15, parent=root)

    root.left.left = BinaryTree(3, parent=root.left)
    root.left.right = BinaryTree(7, parent=root.left)

    root.right.right = BinaryTree(20, parent=root.right)
    root.right.right.left = BinaryTree(12, parent=root.right.right)

    node = root.left.right  
    successor = find_successor(root, node)

    if successor is not None:
        print("Наступник вузла", node.value, "->", successor.value)
    else:
        print("Наступника для вузла", node.value, "немає")