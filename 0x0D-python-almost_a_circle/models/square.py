#!/usr/bin/python3
"""Module for calss Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a class square"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)
    
    def __str__(self):
        """Return string representation of a square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter of size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size"""
        self.width = value
        self.height = value
        
    def update(self, *args, **kwargs):
        """Update method for Square"""

        if args:
            for i, element in enumerate(args):
                if i == 0:
                    self.id = element
                elif i == 1:
                    self.size = element
                elif i == 2:
                    self.x = element
                elif i == 3:
                    self.y = element
        else:
            for key, value in kwargs.items():
                if hasattr(self, key) is True:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        my_dict2 = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return my_dict2    
