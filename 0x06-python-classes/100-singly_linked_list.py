#!/usr/bin/python3
"""Square module."""

class Node:
"""Define Square"""
    def __init__(self, data, next_node=None):
        """initialize square.
        Args:
            data
            next_node
        """
        self.data = data
    
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
    def __init__(self):
        self.head = None

        


