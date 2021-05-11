#!/usr/bin/python3
"""Square module."""

class Node:
"""Define Square"""
    def __init__(self, data, next_node=None):
        """initialize square.
        Args:
            data (int)
            next_node (Node)
        """
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """Get/set data"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self)
        """Get/set next_node"""
        return self.__next_data

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) != Node:
            raise TypeError("next_node must be a Node object")
        self.next_node = value


class SinglyLinkedList:
    """Define a singly linked list"""

    
    def __init__(self):
        """initiate a new Singley linked list.
        """
        self.head = None
        
    def sorted_insert(self, value):
        """insert a new Node 
        Args:
            value
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
