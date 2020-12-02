#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 09:43:19 2020

@author: viper

Single Linked List 
"""

class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None 

class LinkedList:
    
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def push(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAfter(self,after,data):
        
        if after is None:
            print("The given previous node must not be none and should exist in Linked List")
        if self.head == None:
            self.head = Node(data)
            return
        
    
        pnode = self.head
        while(pnode is not None and pnode.data != after):
            pnode = pnode.next
        
        new_node = Node(data)
        new_node.next = pnode.next
        pnode.next = new_node
        return 
    
    def append(self, data):
        if self.head == None: 
            self.head = Node(data)
            return
        last = self.head
        while(last.next):
            last = last.next
        last.next = Node(data)
    
    def delete(self,data):
        
        if self.head == None:
            print('Link List is empty')
            return 
        predNode = None
        curNode = self.head
        while curNode is not None and curNode.data != data :
          predNode = curNode
          curNode = curNode.next
        if curNode is not None:
            if curNode is self.head :
                self.head = curNode.next 
            else :
                predNode.next = curNode.next
            
            
            
        
if __name__ == '__main__':
    slist = LinkedList()
    slist.head = Node(1)
    second = Node(2)    
    third = Node(3)
    slist.head.next = second
    second.next = third
    slist.push(4)
    
    slist.insertAfter(2,5)
    slist.delete(1)
    slist.delete(2)
    slist.delete(4)
    slist.delete(5)
    slist.printList()
    slist.delete(3)
    slist.printList()
    slist.delete(3)
    