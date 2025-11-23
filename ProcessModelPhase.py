# This class represents a Phase in a Process Model for Software Development
class ProcessModelPhase:
    # Initialize the Phase with default values
    def __init__(self, name, description):
        self.__name = name
        self.__description = description
        # Initialize an empty list of tasks for the phase
        # Tasks is expected to be a list of Phase_Task instances
        self.__tastks = []

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

    # Property getter and setter for tasks
    @property
    def tasks(self):
        return self.__tastks
    @tasks.setter
    def tasks(self, tasks):
        self.__tastks = tasks

    # Get total number of tasks in the phase
    def get_total_tasks(self):
        return len(self.__tastks)

    # Method to add a task to the phase
    # task is expected to be an instance of PhaseTask
    def add_task(self, task):
        self.__tastks.append(task)

    # Print details of the Phase
    def __str__(self):
        return f"Phase: {self.name}\nDescription: {self.description}"