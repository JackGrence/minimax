# version 1.0
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


def get_tree_info():
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
