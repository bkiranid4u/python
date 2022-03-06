#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Implementation of stack using a list
class Node:
    __slots__ = '_element', '_next'
    def __init__(self, data):
        self._element = data
        self._next = None

class LinkedList:

    def __init__(self):
        self._head = None
        self._size = 0
    
    def is_empty(self):
        return self._size == 0

    def push(self,data):
        node = Node(data)
        node._next = self._head
        self._head = node
        self._size +=1
    
    def top(self):
        # Check if the stack is empty
        assert not self.is_empty(), 'Stack is empty'
        return self._head._element
    
    def pop(self):
        # Check if the stack is empty
        assert not self.is_empty(), 'Stack is empty'
        answer = self._head._element
        self._head = self._head._next
        self._size -=1
        return answer

        
