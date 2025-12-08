# This class represents a Developer in the Software Engineering context
# A Developer has a name and an experience level, and developer traits
import Trait as trait

class Developer:
    def __init__(self):
        self.__name = None
        self.__experience_level = None
        self.__trait_responsibility = None
        self.__trait_awareness = None
        self.__trait_honesty = None
        self.__trait_resiliency = None
        self.__trait_fairness = None
        self.__trait_attention_to_detail = None
        self.__trait_pragmatism = None
        self.__number_of_traits = 0

    # Getter and Setter for Developer Name
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, value):
        self.__name = value
    
    # Getter for Number of Traits
    @property
    def number_of_traits(self):
        return self.__number_of_traits

    # Getter and Setter for Experience Level
    @property
    def experience_level(self):
        return self.__experience_level
    @experience_level.setter
    def experience_level(self, value):
        self.__experience_level = value

    # Getters and Setters for the Responsibility Trait
    @property
    def trait_responsibility(self) -> trait.Trait:
        return self.__trait_responsibility
    @trait_responsibility.setter
    def trait_responsibility(self, value: trait.Trait):
        self.__trait_responsibility = value
        self.__number_of_traits += 1

    # Getters and Setters for the Responsibility Trait
    @property
    def trait_awareness(self) -> trait.Trait:
        return self.__trait_awareness
    @trait_awareness.setter
    def trait_awareness(self, value: trait.Trait):
        self.__trait_awareness = value
        self.__number_of_traits += 1

    # Getters and Setters for the Honesty Trait
    @property
    def trait_honesty(self) -> trait.Trait:
        return self.__trait_honesty
    @trait_honesty.setter
    def trait_honesty(self, value: trait.Trait):
        self.__trait_honesty = value
        self.__number_of_traits += 1

    # Getters and Setters for the Resiliency Trait
    @property
    def trait_resiliency(self) -> trait.Trait:
        return self.__trait_resiliency
    @trait_resiliency.setter
    def trait_resiliency(self, value: trait.Trait):
        self.__trait_resiliency = value
        self.__number_of_traits += 1

    # Getters and Setters for the Fairness Trait
    @property
    def trait_fairness(self) -> trait.Trait:
        return self.__trait_fairness
    @trait_fairness.setter
    def trait_fairness(self, value: trait.Trait):
        self.__trait_fairness = value
        self.__number_of_traits += 1

    # Getters and Setters for the Attention to Detail Trait
    @property
    def trait_attention_to_detail(self) -> trait.Trait:
        return self.__trait_attention_to_detail
    @trait_attention_to_detail.setter
    def trait_attention_to_detail(self, value: trait.Trait):
        self.__trait_attention_to_detail = value
        self.__number_of_traits += 1

    # Getters and Setters for the Being Pragmatic Trait
    @property
    def trait_pragmatism(self) -> trait.Trait:
        return self.__trait_pragmatism
    @trait_pragmatism.setter
    def trait_pragmatism(self, value: trait.Trait):
        self.__trait_pragmatism = value
        self.__number_of_traits += 1
