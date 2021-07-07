#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def push(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    

        
