import Actor as actor

# This class represents a use case function in the UML Framework

class UseCaseFunction:
    # Initialize the class with default values
    def __init__(self, name, desc):
        self.__name = name
        self.__desc = desc
        self.__actors = []  # List of Actor objects

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

    # Add actor to the use case function
    def add_actor(self, actor: actor.Actor):
        self.__actors.append(actor)

    # Getter and setter for actors
    @property
    def actors(self) -> list[actor.Actor]:
        return self.__actors
    @actors.setter
    def actors(self, actors: list[actor.Actor]):
        self.__actors = actors