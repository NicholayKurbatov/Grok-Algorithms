from typing import List


class TreeNode():
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None

    # more on https://blog.boot.dev/computer-science/binary-search-tree-in-python/
    

def pre_order(value_order: List[int], node: TreeNode) -> List[int]:
    """Прямой обход бинарного дерева (мы посещаем родительские узлы до посещения узлов-потомков)
    Args:
        node (TreeNode): бинарное дерево
        value_order (List[int]): состояния обхода
    Returns:
        List[int]: обновленное состояние обхода
    """
    if node:
        value_order += [node.value]
        pre_order(value_order, node.left)
        pre_order(value_order, node.right)
    return value_order


def post_order(value_order: List[int], node: TreeNode) -> List[int]:
    """Обратный обход бинарного дерева (сначала посещаете узлы-потомки, а затем — их родительские узлы)
    Args:
        node (TreeNode): бинарное дерево
        value_order (List[int]): состояния обхода
    Returns:
        List[int]: обновленное состояние обхода
    """
    if node:
        post_order(value_order, node.left)
        post_order(value_order, node.right)
        value_order += [node.value]
    return value_order


def in_order(value_order: List[int], node: TreeNode) -> List[int]:
    """Симметричный обход бинарного дерева (левый потомок, корень, правый потомок)
    Args:
        node (TreeNode): бинарное дерево
        value_order (List[int]): состояния обхода
    Returns:
        List[int]: обновленное состояние обхода
    """
    if node:
        in_order(value_order, node.left)
        value_order += [node.value]
        in_order(value_order, node.right)
    return value_order


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.left.left = TreeNode(4)
    tree.left.right = TreeNode(5)

    print(pre_order([], tree))
    print(post_order([], tree))
    print(in_order([], tree))