"""
Помимо того чтобы логи писать, нужно их ещё и уметь читать,
иначе мы будем как в известном анекдоте, писателями, а не читателями.

Для вас мы написали простую функцию обхода binary tree по уровням.
Также в репозитории есть файл с логами, написанными этой программой.

Напишите функцию restore_tree, которая принимает на вход 
путь до файла с логами и восстанавливать исходное BinaryTree.

Функция должна возвращать корень восстановленного дерева

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    pass

Примечание: гарантируется, что все значения, 
хранящиеся в бинарном дереве уникальны

"""


import itertools
import logging
import random
import os

from collections import deque
from dataclasses import dataclass
from typing import Optional, Dict


# текущая директория:
cur_dir = os.path.dirname(os.path.abspath(__file__))
logger = logging.getLogger("tree_walk")


@dataclass
class BinaryTreeNode:
    val: int    # значение узла
    left: Optional["BinaryTreeNode"] = None # левый потомок
    right: Optional["BinaryTreeNode"] = None # правый потомок

    def __repr__(self):
        return f"<BinaryTreeNode[{self.val}]>"


def walk(root: BinaryTreeNode):
    queue = deque([root])

    while queue:
        node = queue.popleft()

        logger.info(f"Visiting {node!r}")

        if node.left:
            logger.debug(
                f"{node!r} left is not empty. Adding {node.left!r} to the queue"
            )
            queue.append(node.left)

        if node.right:
            logger.debug(
                f"{node!r} right is not empty. Adding {node.right!r} to the queue"
            )
            queue.append(node.right)


counter = itertools.count(random.randint(1, 10 ** 6))


def get_tree(max_depth: int, level: int = 1) -> Optional[BinaryTreeNode]:
    if max_depth == 0:
        return None

    node_left = get_tree(max_depth - 1, level=level + 1)
    node_right = get_tree(max_depth - 1, level=level + 1)
    node = BinaryTreeNode(val=next(counter), left=node_left, right=node_right)

    return node

# ===================================================================
# поиск в глубину (DFS) - сначала идёт по одному пути 
# от корня до самого глубинного узла, а потом возвращается 
# и обходит другие пути

# поиск в ширину (BFS) - сначала берется родительский узел
# потом его потомки - сначала левый потомок, затем правый
# потомок добавляется в очередь для следующего посещения

# судя по логам используется BFS

def restore_tree(path_to_log_file: str) -> BinaryTreeNode:
    # словарь для хранения узлов по значению:
    nodes_dict: Dict[int, BinaryTreeNode] = {}
    # корень дерева:
    root = None

    # прочитать файл логов и извлечь информацию
    # посещение узла - INFO:Visiting
    # добавление в очередь - DEBUG
    with open(path_to_log_file, 'r') as file:
        for line in file:
            line = line.strip()

            # если посещение узла:___________________________________
            if line.startswith('INFO:Visiting'):
                # берем номер узла и ложим в словарь:
                # split[1] - INFO:Visiting <BinaryTreeNode "[" 396938]>
                # split[0] - 396938 "]" >
                node_value = int(line.split('[')[1].split(']')[0])

                if node_value not in nodes_dict:
                    nodes_dict[node_value] = BinaryTreeNode(node_value)
                
                # проверить корень дерева:
                if root is None:
                    root = nodes_dict[node_value]

            
            # если добавление в очередь:_____________________________
            elif line.startswith('DEBUG'):
                # разделим строку на части:
                line_parts = line.split()

                # нас интересуют:
                # DEBUG:<BinaryTreeNode[396981]> - [0]
                # right / left
                # <BinaryTreeNode[396980]> - [6]

                # из первой части получить родительский узел:
                value_parent = int(line_parts[0].split('[')[1].split(']')[0])
                # из шестой части получить дочерний узел:
                value_child = int(line_parts[6].split('[')[1].split(']')[0])

                # проверить дочернее значение в словаре и создать узел:
                if value_child not in nodes_dict:
                    nodes_dict[value_child] = BinaryTreeNode(value_child)

                # определить лево или право:
                if 'left' in line_parts:
                    nodes_dict[value_parent].left = nodes_dict[value_child]
                elif 'right' in line_parts:
                    nodes_dict[value_parent].right = nodes_dict[value_child]

    return root

# ===================================================================
# ===================================================================
# структура дерева:
def print_tree(node, level=0):
    if node is not None:
        left_val = node.left.val if node.left else 'None'
        right_val = node.right.val if node.right else 'None'

        

# ===================================================================
# ===================================================================
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(levelname)s:%(message)s",
        filename=os.path.join(cur_dir, "walk_log_4.txt"),
    )

    root = get_tree(7)
    walk(root)

    tree_root = restore_tree(os.path.join(cur_dir, "walk_log_4.txt"))
    print('КОРЕНЬ:', tree_root)

    print_tree(tree_root)

