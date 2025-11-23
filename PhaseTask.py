# This class represents a Task in a Phase in a Process Model for Software Development
class PhaseTask:
    # Initialize the Task with default values
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
    
    # Property getter and setter for name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    # Property getter and setter for description
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description):
        self.__description = description