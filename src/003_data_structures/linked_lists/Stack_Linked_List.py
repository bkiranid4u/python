#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 15:51:39 2020

@author: viper
"""

class Stack:
    
    def __init__(self):
        self._top = None
        self._size = 0
    
    def isEmpty(self):
        assert self._top() is None
        
    def __len__(self):
        return self._size
    
    def peek(self):
        assert not self.isEmpty(), 'Cannot peek empty list'
        return self._top.item
    
    def pop(self):
        assert not self.isEmpty(), 'Cannot pop empty list'
        node = self._top()
        self._top = self._top.next
        return node.item
        self._size = self._size -1
        
    def push(self, item):
        self._top = _StackNode(item, self._top)
        self._size +=1

class _StackNode:
    def __init__(self, link, item):
        self.item = item
        self.next = link
        