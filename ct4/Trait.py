# This class represents a Developer Trait defined in the Software Engineering
# There are seven traits defined in the Software Engineering
class Trait:

    # Constant Values for the sevent Traits defined in the Software Engineering
    RESPONSIBILITY = "Individual Responsibility"
    AWARENESS = "Acute Awareness "
    HONESTY = "Brutal Honesty"
    RESILIENCY = "Resilience Under Pressure"
    FAIRNESS = "Sense of Fairness"
    ATTENTION_TO_DETAIL = "Attention to Detail"
    PRAGMATISM = "Being Prgmatic"

    # Constant Values for the sevent Traits defined in the Software Engineering
    RESPONSIBILITY_DESC = "A commitment to fulfill promises by doing whatever it takes to achieve success."
    AWARENESS_DESC = "Being empatheic to the needs of team members and stakeholders."
    HONESTY_DESC = "Providing constructive feedback in a respectful manner."
    RESILIENCY_DESC = "Managing pressure without impacting performance."
    FAIRNESS_DESC = "Shares credit with colleagues and avoid conflicts of interest."
    ATTENTION_TO_DETAIL_DESC = "Considering broader criteria in technical decisions."
    PRAGMATISM_DESC = "Recognizing the need to adapt to the circumstances at hand."


    # Initialize the Trait with a name and description
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
