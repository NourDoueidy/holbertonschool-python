#!/usr/bin/python3
"""Module for class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Defines a class Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constuctor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)        
