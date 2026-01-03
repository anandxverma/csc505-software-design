# This class represents an Developer Builder for creating Developer objects

import Trait as trait
import Developer as developer
import Experience_Levels as exp
from DeveloperBuilderAbstract import DeveloperBuilderAbstract

class DeveloperBuilder(DeveloperBuilderAbstract):

    # Experience levels for Developers
    experience_levels = [exp.INTERN, exp.ASSOCIATE, exp.STAFF, exp.SENIOR, exp.PRINCIPAL, exp.DISTINGUISHED]

    def __init__(self):
        self.__developer = developer.Developer()

    def get_developer(self) -> developer.Developer:
        return self.__developer

    #def set_name(self, name: str):
    #    self.__developer.name = name
    #    return self

    #def set_experience_level(self, experience_level: str):
    #    self.__developer.experience_level = experience_level
    #    return self

    def add_trait_responsibility(self):
        self.__developer.trait_responsibility = trait.Trait(trait.Trait.RESPONSIBILITY, trait.Trait.RESPONSIBILITY_DESC)
        return self

    def add_trait_awareness(self):
        self.__developer.trait_awareness = trait.Trait(trait.Trait.AWARENESS, trait.Trait.AWARENESS_DESC)
        return self

    def add_trait_honesty(self):
        self.__developer.trait_honesty = trait.Trait(trait.Trait.HONESTY, trait.Trait.HONESTY_DESC)
        return self

    def add_trait_resiliency(self):
        self.__developer.trait_resiliency = trait.Trait(trait.Trait.RESILIENCY, trait.Trait.RESILIENCY_DESC)
        return self

    def add_trait_fairness(self):
        self.__developer.trait_fairness = trait.Trait(trait.Trait.FAIRNESS, trait.Trait.FAIRNESS_DESC)
        return self

    def add_trait_attention_to_detail(self):
        self.__developer.trait_attention_to_detail = trait.Trait(trait.Trait.ATTENTION_TO_DETAIL, trait.Trait.ATTENTION_TO_DETAIL_DESC)
        return self
    
    def add_trait_pragmatism(self):
        self.__developer.trait_pragmatism = trait.Trait(trait.Trait.PRAGMATISM, trait.Trait.PRAGMATISM_DESC)
        return self

    def build(self, name: str, experience_level: str):
        self.__developer = developer.Developer()
        # Validate name is not empty
        if not name or name.strip() == "":
            raise ValueError("Developer Name cannot be empty")
        # Validate Experience Level is valid
        if experience_level is None:
            raise ValueError("Developer Experience Level must be provided")
        # Check if experience level is valid
        if experience_level not in self.experience_levels:
            raise ValueError(f"{experience_level} is invalid. Developer Experience Level must be one of {self.experience_levels}")
        # Set values after validations pass
        self.__developer.name = name
        self.__developer.experience_level = experience_level
        return self