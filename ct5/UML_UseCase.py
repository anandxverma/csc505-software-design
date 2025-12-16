# This class represents a use case in the UML Framework

import UML_UseCase_Function as ucf

class UML_UseCase:
    # Initialize the class with default values
    def __init__(self, name, desc):
        self.__name = name
        self.__desc = desc
        self.__use_case_functions = []  # List of UseCaseFunction objects

    # Getter and setter for name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name):
        self.__name = name
    
    # Getter and setter for description
    @property
    def desc(self):
        return self.__desc
    @desc.setter
    def desc(self, desc):
        self.__desc = desc

    # Add use case function to the use case
    def add_use_case_function(self, use_case_function: ucf.UML_UseCase_Function):
        self.__use_case_functions.append(use_case_function)

    # Getter and setter for use case functions
    @property
    def use_case_functions(self) -> list[ucf.UML_UseCase_Function]:
        return self.__use_case_functions
    @use_case_functions.setter
    def use_case_functions(self, use_case_functions: list[ucf.UML_UseCase_Function]):
        self.__use_case_functions = use_case_functions