from tree import tree
import random
import time
import sys


def main():
    branch, max_depth, leaf = get_tree_info()
    t = tree(branch, max_depth, leaf)
    print('--- result ---')
    print('root value:', t.root.value)
    pruning_leaf = t.get_pruning_leaf()
    print('pruning leaf len:', len(pruning_leaf))
    print('leaf:')
    print(pruning_leaf)


def build_tree():
    pass


def get_tree_info():
    # input('branch:')
    # branch = 3
    # leaf = [-7, -5, 0, 3, 9, -6, 1, 3, 2]
    # leaf_len = branch ** 13
    # leaf = []
    # for i in range(leaf_len):
    #     leaf.append(random.randrange(-10, 10))
    # leaf = [-6, 15, 14, 10, -17, 16, -10, -7, -5]
    # leaf = [-13, -5, 10, 1, -5, -16, -16, -11, 6, -1, 16, 12, 3, -5, 19, -16, 19, 11, 12, 14, -13, 1, -15, -16, 16, 12, 18, 17, 9, -6, 10, -19, -14, -4, -11, -11, -1, 4, 9, 1, -10, -10, 19, 15, 19, 15, -10, 2, 8, 7, -10, 0, 5, 12, -7, -12, 6, 9, 4, -13, 17, 3, 0, -4, -10, 19, 17, 5, -6, -7, 9, -10, 13, -14, 15, -19, 17, 20, -11, -7, -5]
    # leaf = [-5, -9, -8, -5, -4, -7, -16, -18, -13, 13, 13, 16, 11, -10, -7, -1, -15, 10, 16, -9, -9, -3, -11, 15, -15, -12, -16, -6, -17, -17, 15, 1, -4, 8, -6, -1, 2, -8, 18, 18, 18, 2, -12, -1, -8, 2, 18, -5, 18, 17, 7, 17, 2, -5, 13, 15, 14, 15, -7, 16, -13, -4, -14, 4, 8, -4, -3, -8, -12, 7, 2, 14, 12, -13, -9, -10, -11, 5, -8, -9, 11]
    # leaf = [-15, -1, 13, -13, 13, 16, -11, -17, -2, -2, -15, 10, -3, -18, 18, -9, -17, -5, 8, 7, -7, -1, -12, -13, 12, -1, -4]
    # leaf_len = len(leaf)
    # leaf = [13 for i in range(leaf_len)]
    # max_depth = 3 # exclude root
    assert len(sys.argv) >= 2, '\nusage: ./minimax.py input.txt'
    with open(sys.argv[1], 'r') as f:
        branch = int(f.readline())
        max_depth = int(f.readline())
        leaf = f.readline()
    leaf = [int(i) for i in leaf.split(', ')]
    return branch, max_depth, leaf


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
