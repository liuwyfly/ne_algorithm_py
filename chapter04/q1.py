# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-09-01 22:04:38
# @Last Modified by:   Anderson
# @Last Modified time: 2019-03-10 23:46:10
class Node:
    def __init__(self, data, par=None):
        # print ("Node __init__: " + str(data))
        self.data = list([data])
        self.parent = par
        self.child = list()

    def __str__(self):
        if self.parent:
            return str(self.parent.data) + ' : ' + str(self.data)
        return 'Root : ' + str(self.data)

    def __lt__(self, node):
        return self.data[0] < node.data[0]

    def _isLeaf(self):
        return len(self.child) == 0

    # merge new_node sub-tree into self node
    def _add(self, new_node):
        for data in new_node.data:
            if data in self.data:
                return False
        for child in new_node.child:
            child.parent = self
        self.data.extend(new_node.data)
        self.data.sort()
        self.child.extend(new_node.child)
        if len(self.child) > 1:
            self.child.sort()
        if len(self.data) > 2:
            self._split()

        return True

    # find correct node to insert new node into tree
    def _insert(self, new_node):
        # print ('Node _insert: ' + str(new_node.data) + ' into ' + str(self.data))
        insert_done = False
        # leaf node - add data to leaf and rebalance tree
        if self._isLeaf():
            insert_done = self._add(new_node)

        # not leaf - find correct child to descend, and do recursive insert
        elif new_node.data[0] > self.data[-1]:
            insert_done = self.child[-1]._insert(new_node)
        else:
            for i in range(0, len(self.data)):
                if new_node.data[0] == self.data[i]:
                    break
                if new_node.data[0] < self.data[i]:
                    insert_done = self.child[i]._insert(new_node)
                    break

        return insert_done

    # 3 items in node, split into new sub-tree and add to parent
    def _split(self):
        # print("Node _split: " + str(self.data))
        left_child = Node(self.data[0], self)
        right_child = Node(self.data[2], self)
        if self.child:
            self.child[0].parent = left_child
            self.child[1].parent = left_child
            self.child[2].parent = right_child
            self.child[3].parent = right_child
            left_child.child = [self.child[0], self.child[1]]
            right_child.child = [self.child[2], self.child[3]]

        self.child = [left_child]
        self.child.append(right_child)
        self.data = [self.data[1]]

        # now have new sub-tree, self. need to add self to its parent node
        if self.parent:
            if self in self.parent.child:
                self.parent.child.remove(self)
            self.parent._add(self)
        else:
            left_child.parent = self
            right_child.parent = self

    # find an item in the tree; return item, or False if not found
    def _find(self, item):
        # print ("Find " + str(item))
        if item in self.data:
            return item
        elif self._isLeaf():
            return False
        elif item > self.data[-1]:
            return self.child[-1]._find(item)
        else:
            for i in range(len(self.data)):
                if item < self.data[i]:
                    return self.child[i]._find(item)

    def _remove(self, item):
        pass

    # print preorder traversal
    def _preorder(self):
        print(self)
        for child in self.child:
            child._preorder()


class Tree:
    def __init__(self):
        # print("Tree __init__")
        self.root = None

    def insert(self, item):
        insert_done = True
        if self.root is None:
            self.root = Node(item)
        else:
            insert_done = self.root._insert(Node(item))
            while self.root.parent:
                self.root = self.root.parent
        return insert_done

    def find(self, item):
        return self.root._find(item)

    def remove(self, item):
        self.root.remove(item)

    def printTop2Tiers(self):
        print('----Top 2 Tiers----')
        print(str(self.root.data))
        for child in self.root.child:
            print(str(child.data), end=' ')
        print(' ')

    def preorder(self):
        print('----Preorder----')
        self.root._preorder()


s = input()
s_list = s.split(' ')
# s_list = [1,4,2,5,4,3,2,2,6,2]
tree = Tree()
count = 0
for item in s_list:
    if tree.insert(int(item)):
        count += 1
print(count)
