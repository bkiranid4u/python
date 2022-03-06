#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Implementation of stack using a queue

class Node:
    __slots__ = '_element', '_next'

    def __init__(self, data):
        self._element = data
        self._next = None

class LinkListQueue:

    def __init__(self) -> None:
        self._head = None
        self._tail = None   
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        return self._head._element
    
    def enqueue(self, item):
        node = Node(item)
        # If the queue is empty add the element to head and tail as well 
        if self.is_empty():
            self._head = node
        else:
            # Assigning the refrence of the new node to the current tail node 
            self._tail.next = node
        # Assign the new node as the tail node
        self._tail = node
        self._size +=1
    
    def dequeue(self):
        
        assert not self.is_empty(), 'Queue is empty'

        answer = self._head._element
        self._head = self._head._next
        self._size -=1
        if self.is_empty():
            self._tail = None
        return answer


