# This class represents an actor in the UML Framework

class Actor:
    # Initialize the class with default values
    def __init__(self, type, desc):
        self.__type = type
        self.__desc = desc

    # Getter and setter for type
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type):
        self.__type = type
    
    # Getter and setter for description
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, desc):
        self.__desc = desc