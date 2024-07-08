#!/usr/bin/env python3
'''Module define solution to merging k sorted linkedlist'''
from typing import List, Optional


class ListNode:
    '''Definition for singly-linked list.'''
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    '''Solution class'''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''merge k sorted linkedlist and reurn the head.
        all linked list will be joint in one singly-linkedlist
        '''
        flatten_list = []


        for node in lists:
            # flattening the list
            while node:
                flatten_list.append(node)
                node = node.next

        if len(flatten_list) == 0:
            return None
        size = len(flatten_list)
        i = size // 2 - 1

        while i >= 0:
            # build our max-heap
            self.heapify(flatten_list, i, size)
            i -= 1

        i = size - 1

        while i >= 0:
            # sorting our heap
            flatten_list[0], flatten_list[i] = flatten_list[i], flatten_list[0]
            self.heapify(flatten_list, 0, i)
            i -= 1


        tmp = flatten_list[0]
        for i in range(1, size):
            # adusting the links
            tmp.next = flatten_list[i]
            tmp = tmp.next
        tmp.next = None
        return flatten_list[0]


    def heapify(self, iterable, i, size):
        '''heapify max heap and siftdown.
        So basically heapify is a side_effect which change
        maintain my heap property by swapping nodes if necessary.
        '''
        i_large = i
        i_left = 2 * i + 1
        i_right = 2 * i + 2

        if i_left < size and iterable[i_left].val > iterable[i_large].val:
            i_large = i_left
        if i_right < size and iterable[i_right].val > iterable[i_large].val:
            i_large = i_right

        if i != i_large:
            # swap
            iterable[i].val, iterable[i_large].val = iterable[i_large].val, iterable[i].val
            self.heapify(iterable, i_large, size)

