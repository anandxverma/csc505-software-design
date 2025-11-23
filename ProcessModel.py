# This class represents a generic Process Model for Software Development
class ProcessModel:
    def __init__(self, name, description):
        #Initialize the Process Model with default values
        self.__name = name
        self.__description = description
        # Phases is expected to be an ordered list of phases in the process model
        self.__phases = []

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

    # Property getter and setter for Phases
    @property
    def phases(self):
        return self.__phases
    @phases.setter
    def phases(self, phases):
        self.__phases = phases

    # Method to add a phase to the process model
    # The phases are added in order
    # phase is expected to be an instance of ProcessModelPhase
    def add_phase(self, phase):
        # Check if the phase is already in the process model
        existing_phase = self.get_phase_by_name(phase.name)
        # If it does not exist, then add the new phase to the list
        if not existing_phase:
            self.__phases.append(phase)
        # If it exists, then replace the existing phase with the new phase
        else:
            index = self.__phases.index(existing_phase)
            self.__phases[index] = phase

    # Method to remove a phase from the process model by name
    def remove_phase_by_name(self, phase_name):
        self.__phases = [phase for phase in self.__phases if phase.name.upper() != phase_name.upper()]

    # Method to remove a phase from the process model by position
    def remove_phase_by_position(self, position):
        if 0 <= position < len(self.__phases):
            del self.__phases[position]
        else:
            raise Exception("Position out of range")

    # Method to look up a phase by name
    # This method returns an instance of ProcessModel_ModelPhase if found, else None
    def get_phase_by_name(self, phase_name):
        for phase in self.__phases:
            if phase.name.upper() == phase_name.upper():
                return phase
        return None
    
    # Method to look up a phase by position
    def get_phase_by_position(self, position):
        if 0 <= position < len(self.__phases):
            return self.__phases[position]
        else:
            raise Exception("Position out of range")
        
    # Method to get the total number of phases in the process model
    def get_total_phases(self):
        return len(self.__phases)
    
    # Method to get the position of a phase by name
    def get_phase_position_by_name(self, phase_name):
        for index, phase in enumerate(self.__phases):
            if phase.name.upper() == phase_name.upper():
                return index+1
        return -1

    # Print the details of the process model
    def __str__(self):
        details = f"Process Model: {self.name}\n"
        details += f"Description: {self.description}\nPhases:\n"
        for phase in self.phases:
            details += f"- {phase}\n"
        return details