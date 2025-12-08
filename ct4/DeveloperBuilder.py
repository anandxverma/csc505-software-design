# This class represents an Developer Builder for creating Developer objects

import Trait as trait
import Developer as developer
from DeveloperBuilderAbstract import DeveloperBuilderAbstract

class DeveloperBuilder(DeveloperBuilderAbstract):

    def __init__(self):
        self.__developer = developer.Developer()

    def get_developer(self) -> developer.Developer:
        return self.__developer

    def set_name(self, name: str):
        self.__developer.name = name
        return self

    def set_experience_level(self, experience_level: str):
        self.__developer.experience_level = experience_level
        return self

    def add_trait_responsibility(self, trait: trait.Trait):
        self.__developer.trait_responsibility = trait
        return self

    def add_trait_awareness(self, trait: trait.Trait):
        self.__developer.trait_awareness = trait
        return self

    def add_trait_honesty(self, trait: trait.Trait):
        self.__developer.trait_honesty = trait
        return self

    def add_trait_resiliency(self, trait: trait.Trait):
        self.__developer.trait_resiliency = trait
        return self

    def add_trait_fairness(self, trait: trait.Trait):
        self.__developer.trait_fairness = trait
        return self

    def add_trait_attention_to_detail(self, trait: trait.Trait):
        self.__developer.trait_attention_to_detail = trait
        return self
    
    def add_trait_pragmatism(self, trait: trait.Trait):
        self.__developer.trait_pragmatism = trait
        return self
