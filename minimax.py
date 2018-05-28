from tree import tree
import random
import time


def main():
    branch, leaf_len, leaf = get_tree_info()
    t = tree(branch, leaf_len, leaf)
    print(t._tree__max_depth)
    print(t.root.value)
    t.print(t.root)
    print('--- pruning ---')
    for i in t.pruning_node:
        t.print(i)


def build_tree():
    pass


def get_tree_info():
    # input('branch:')
    branch = 3
    leaf_len = 9
    leaf = [-7, -5, 0, 3, 9, -6, 1, 3, 2]
    leaf_len = 3 ** 3
    leaf = []
    for i in range(leaf_len):
        leaf.append(random.randrange(-10, 10))
    leaf = [-7, 15, 6, 3, -11, 15, 5, -18, 2, -4, 7, 8, -17, -2, 5, 11, -15, 9, -15, 6, 17, -16, -5, 3, -13, -1, -5]
    return branch, leaf_len, leaf


if __name__ == '__main__':
    start_time = time.time()
    main()
    print('--- {0} seconds ---'.format(time.time() - start_time))

'''
6 |
-3 | 2 | 6 |
2 | -3 | 5 | 8 | 9 | 2 | 8 | 8 | 6 |
1 | 2 | -1 | -3 | -8 | -6 | 5 | 0 | 2 | -4 | 8 | 4 | 9 | -9 | 1 | 2 | -1 | -10 | -2 | 8 | -3 | -5 | 8 | -3 | 4 | 5 | 6 |
'''
