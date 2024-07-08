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
        '''merge k sorted linkedlist and reurn the head'''
