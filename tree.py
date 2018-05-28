import queue


class tree:
    def __init__(self, branch, leaf_len, leaf):
        self.__branch = branch
        self.__leaf_len = leaf_len
        self.__leaf = leaf[:leaf_len]
        self.__max = leaf[0]
        self.__min = leaf[0]
        for i in leaf[1:]:
            if self.__max < i:
                self.__max = i
            if self.__min > i:
                self.__min = i
        self.__max += 1
        self.__min -= 1
        self.__max_depth = 0
        self.__cur_index = 0
        self.pruning_node = []
        self.root = self.node(self.__min, 0, None, self.__branch)
        self.build_tree(self.root, 0, False, branch)
        self.minimax(self.root, 0, True)
        # catch leaf_len < 1 or leaf is empty

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

    def build_tree(self, cur_node, depth, is_max, node_len):
        if depth + 1 > self.__max_depth:
            self.__max_depth = depth + 1
        for i in range(self.__branch):
            value = self.__min if is_max else self.__max
            new_node = self.node(value, depth + 1, cur_node, self.__branch)
            cur_node.child.append(new_node)
            if node_len == self.__leaf_len:
                new_node.value = self.__leaf[self.__cur_index]
                self.__cur_index += 1
            else:
                self.build_tree(new_node, depth + 1, not is_max, node_len * self.__branch)

    def minimax(self, cur_node, depth, is_max):
        if depth >= self.__max_depth:
            return cur_node.value
        child_index = 0
        for i in cur_node.child:
            # alpha-beta pruning
            if depth >= 1:
                if is_max:
                    alpha = cur_node.value
                    beta = cur_node.parent.value
                else:
                    alpha = cur_node.parent.value
                    beta = cur_node.value
                if alpha >= beta:
                    self.pruning_node.extend(cur_node.child[child_index:])
                    break
            value = self.minimax(i, depth + 1, not is_max)
            if is_max:
                cur_node.value = value if value > cur_node.value else cur_node.value
            else:
                cur_node.value = value if value < cur_node.value else cur_node.value
            child_index += 1
        return cur_node.value

    class node:
        def __init__(self, value, depth, parent, max_child_len):
            self.value = value
            self.depth = depth
            self.parent = parent
            self.child = []
            self.max_child_len = max_child_len
