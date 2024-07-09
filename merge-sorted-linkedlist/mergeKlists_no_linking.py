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
        '''merge k sorted linkedlist and return the head.
        all linked-list elements will be joined in one singly-linkedlist
        only the values are swapped so no need for relinking at the end
        a teeny tiny bit faster (not sure if it's allowed tho)
        '''
        flatten_list = []

        # flattening the list
        for node in lists:
            # linking the lists inside the flattened list
            if flatten_list:
                flatten_list[-1].next = node
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

        i = size - 1
        while i >= 0:
            # sorting our heap
            flatten_list[0].val, flatten_list[i].val = flatten_list[i].val, flatten_list[0].val
            self.heapify(flatten_list, 0, i)
            i -= 1

        return flatten_list[0]

    def heapify(self, iterable, i, size):
        '''heapify max heap and siftdown. (should theoretically work with both min and max heaps)
        So basically heapify is a side_effect which changes the iterable in place and
        maintains my heap property by swapping nodes if necessary.
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
            iterable[i].val, iterable[i_large].val =\
                    iterable[i_large].val, iterable[i].val
            self.heapify(iterable, i_large, size)