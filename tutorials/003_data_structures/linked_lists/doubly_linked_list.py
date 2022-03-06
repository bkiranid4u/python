""" Doubly Linked List """

class _Node:
    __slots__ = '_element', '_next', '_prev'

    def __init__(self, element,prev,next) -> None:
        self._element = element
        self._next = next
        self._prev = prev
    

class DoublyLinkedList:

    def __init__(self) -> None:
        self._header = _Node(None,None,None)
        self._trailer = _Node(None, None, None)
        self._header._next = self._trailer
        self._trailer = self._header
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0
    
    def insertNode(self,node,prvNode,nextNode):
        newNode = 
        prvNode._next = node
        nextNode._prev = node
        self._size += 1
    
