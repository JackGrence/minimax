import queue


class tree:
    def __init__(self, branch, max_depth, leaf):
        self.__branch = branch
        self.__leaf_len = branch ** max_depth
        self.__leaf = leaf[:]
        self.__max = leaf[0]
        self.__min = leaf[0]
        for i in leaf[1:]:
            if self.__max < i:
                self.__max = i
            if self.__min > i:
                self.__min = i
        self.__max += 1
        self.__min -= 1
        self.__max_depth = max_depth
        self.__cur_index = 0
        self.pruning_node = []
        self.root = self.node(self.__min, 0, None, self.__branch)
        self.build_tree(self.root, 0, False)
        self.alpha_beta_pruning(self.root, 0, True, self.__min, self.__max)
        #self.minimax(self.root, 0, True)
        # catch leaf_len < 1 or leaf is empty

    def get_pruning_leaf(self):
        leaf = []
        for i in self.pruning_node:
            self.get_leaf(i, leaf)
        return leaf

    def get_leaf(self, cur_node, leaf):
        if cur_node.depth == self.__max_depth:
            leaf.append(cur_node.value)
            return
        for i in cur_node.child:
            self.get_leaf(i, leaf)

    def print(self, print_node):
        last_node_depth = -1
        q = queue.Queue()
        q.put(print_node)
        while not q.empty():
            cur_node = q.get()
            if last_node_depth != cur_node.depth:
                print('')
            print(cur_node.value, end=' | ')
            for i in cur_node.child:
                q.put(i)
            last_node_depth = cur_node.depth
        print('')

    def build_tree(self, cur_node, depth, is_max):
        for i in range(self.__branch):
            value = self.__min if is_max else self.__max
            new_node = self.node(value, depth + 1, cur_node, self.__branch)
            cur_node.child.append(new_node)
            if depth + 1 == self.__max_depth:
                new_node.value = self.__leaf[self.__cur_index]
                self.__cur_index += 1
            else:
                self.build_tree(new_node, depth + 1, not is_max)

    def minimax(self, cur_node, depth, is_max):
        if depth >= self.__max_depth:
            return cur_node.value
        child_index = 0
        for i in cur_node.child:
            value = self.minimax(i, depth + 1, not is_max)
            if is_max:
                cur_node.value = value if value > cur_node.value else cur_node.value
            else:
                cur_node.value = value if value < cur_node.value else cur_node.value
            child_index += 1
        return cur_node.value

    def alpha_beta_pruning(self, cur_node, depth, is_max, alpha, beta):
        if depth >= self.__max_depth:
            return cur_node.value
        child_index = 0
        for i in cur_node.child:
            value = self.alpha_beta_pruning(i, depth + 1, not is_max, alpha, beta)
            if is_max:
                # get maximizing of child
                cur_node.value = value if value > cur_node.value else cur_node.value
                # update alpha
                alpha = cur_node.value if cur_node.value > alpha else alpha
            else:
                # get minimizing of child
                cur_node.value = value if value < cur_node.value else cur_node.value
                # update beta
                beta = cur_node.value if cur_node.value < beta else beta
            # record pruning index
            child_index += 1

            # alpha-beta pruning
            if alpha >= beta:
                self.pruning_node.extend(cur_node.child[child_index:])
                break
        return cur_node.value

    class node:
        def __init__(self, value, depth, parent, max_child_len):
            self.value = value
            self.depth = depth
            self.parent = parent
            self.child = []
            self.max_child_len = max_child_len
