# -*- coding: utf-8 -*-
# @Author: Anderson
# @Date:   2018-10-05 01:44:18
# @Last Modified by:   biying
# @Last Modified time: 2018-10-10 13:39:11
class Heap(object):
    """docstring for Heap"""
    def __init__(self):
        self.__keys = [None]
        self.__size = 0

    def add(self, x):
        self.__keys.append(x)
        self.__size += 1
        self.__swim_up(self.__size)

    def get_smallest(self):
        return self.__keys[1]

    def remove_smallest(self):
        self.__keys[1] = self.__keys.pop()
        self.__size -= 1
        self.__swim_down(1)

    def size(self):
        return self.__size

    def __swim_up(self, index):
        if index == 1:
            return

        parent_index = index // 2
        if self.__keys[parent_index] > self.__keys[index]:
            self.__swap(index, parent_index)
            self.__swim_up(parent_index)

    def __swim_down(self, index):
        left_child_index = index * 2
        right_child_index = index * 2 + 1
        swim_down_index = index

        # ÅÐ¶ÏÓÐÃ»ÓÐ×ó×Ó½Úµã
        if left_child_index <= self.__size:
            if self.__keys[index] > self.__keys[left_child_index]:
                swim_down_index = left_child_index

        if right_child_index <= self.__size:
            if self.__keys[index] > self.__keys[right_child_index]:

                if self.__keys[left_child_index] > self.__keys[right_child_index]:
                    swim_down_index = right_child_index

        if swim_down_index != index:
            self.__swap(index, swim_down_index)
            self.__swim_down(swim_down_index)

    def __swap(self, a, b):
        self.__keys[a], self.__keys[b] = self.__keys[b], self.__keys[a]

    def print(self):
        print(self.__keys[1:])


heap = Heap()
s = input()
items = s.split(' ')
for item in items:
    heap.add(int(item))
num = int(input())
for _ in range(num):
    heap.remove_smallest()
print(heap.get_smallest())
