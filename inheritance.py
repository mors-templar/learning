#: part of oop
class Rectangle ():
    def __init__(self):
        self.__length = 0.0
        self.__width = 0.0

    def set_length(self, length):
        (self.__length )= length

    def set_width(self, width):
        (self.__width) = width

    def get_length(self):
        return (self.__length)

    def get_width(self):
        return (self.__width)

    def get_area (self):
        area = self.__width * self.__length
        return area
class tabletop (Rectangle):
    pass
