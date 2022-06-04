#: part of oop
class box() :
    def __init__(self):
        self.__length = 0.0
        self.__width = 0.0
        self.__height = 0.0

    def setlength (self , l):
        self.__length = l

    def setwidth (self , w):
        self.__width = w

    def setheight ( self , h):
        self.__height = h

    def getlength (self):
        return self.__length

    def getwidth (self) :
        return self.__width

    def getheight (self):
        return self.__height

    def getvolume (self):
        vol = self.__width * self.__height * self.__length
        return vol

box1 = box()
box1.setheight(2.0)
box1.setlength(3.0)
box1.setwidth(9.0)
print ("volume of box imputed is:" , box1.getvolume())