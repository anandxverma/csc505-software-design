# This class represents an Abstract Builder for defining the behavious of a DeveloperBuilder

from abc import ABC, abstractmethod
import Trait as trait
import Developer as developer

class DeveloperBuilderAbstract(ABC):

    # Abstract method to get the Developer object being built
    @abstractmethod
    def get_developer(self) -> developer.Developer:
        pass

    # Abstract method to set the name of the Developer
    @abstractmethod
    def set_name(self, name: str):
        pass

    # Abstract method to set the experience level of the Developer
    @abstractmethod
    def set_experience_level(self, experience_level: str):
        pass

    # Abstract methods to add each of the Developer Traits
    @abstractmethod
    def add_trait_responsibility(self, trait: trait.Trait):
        pass

    @abstractmethod
    def add_trait_awareness(self, trait: trait.Trait):
        pass

    @abstractmethod
    def add_trait_honesty(self, trait: trait.Trait):
        pass

    @abstractmethod
    def add_trait_resiliency(self, trait: trait.Trait):
        pass

    @abstractmethod
    def add_trait_fairness(self, trait: trait.Trait):
        pass

    @abstractmethod
    def add_trait_attention_to_detail(self, trait: trait.Trait):
        pass

    @abstractmethod
    def add_trait_pragmatism(self, trait: trait.Trait):
        pass