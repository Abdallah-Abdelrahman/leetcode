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
    def mergeKLists(self,
                    lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''merge k sorted linkedlist and reurn the head.
        all linked-list elements will be joined in one singly-linkedlist
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

        for i in range(size // 2 - 1, -1, -1):
            # build our min-heap
            self.heapify(flatten_list, i, size)
            i -= 1

        head = flatten_list[0]
        tmp = head
        for i in range(size - 1, -1, -1):
            # extract heap root(minheap)
            flatten_list[0], flatten_list[i] = flatten_list[i], flatten_list[0]
            self.heapify(flatten_list, 0, i)
            tmp.next = flatten_list[0]
            tmp = tmp.next
            i -= 1
        tmp.next = None
        return head

    def heapify(self, iterable, i, size):
        '''build a heap from an array and holds min heap property.
        So basically heapify is a side_effect which maintains
        my heap property by swapping nodes if necessary.
        '''
        i_small = i
        i_left = 2 * i + 1
        i_right = 2 * i + 2

        if i_left < size and iterable[i_left].val < iterable[i_small].val:
            i_small = i_left
        if i_right < size and iterable[i_right].val < iterable[i_small].val:
            i_small = i_right

        if i != i_small:
            # swap
            iterable[i].val, iterable[i_small].val =\
                    iterable[i_small].val, iterable[i].val
            # sifting
            self.heapify(iterable, i_small, size)
