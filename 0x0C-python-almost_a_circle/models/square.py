#!/usr/bin/python3
"""Gives a class to represent a square
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Representation of a rectangle
    """
    HEADERS = ('id', 'size', 'x', 'y')

    def __init__(self, size, x=0, y=0, id=None):
        """Initiate a rectangle
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Get a string output of a square
        """
        return "[{type}] ({id}) {x}/{y} - {size}".format(
            type=self.__class__.__name__,
            id=self.id,
            size=self.size,
            x=self.x,
            y=self.y
        )

    @property
    def size(self):
        """Get a private instance attribute 'width'
        """
        return self.width

    @size.setter
    def size(self, size):
        """Set a private instance attributes 'width' and 'height'
        """
        self.width = size
        self.height = size

    def to_dictionary(self):
        """Get dictionary representation of a square
        """
        return {key: getattr(self, key) for key in self.__class__.HEADERS}

    def update(self, *args, **kwargs):
        """Update attributes of a  object
        """
        if args:
            for pair in zip(self.HEADERS, args):
                setattr(self, *pair)
        else:
            for key in kwargs:
                if key in self.HEADERS:
                    setattr(self, key, kwargs[key])
