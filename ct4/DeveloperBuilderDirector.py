# Main program logic for building Developer objects using the Builder Director Design Pattern
import DeveloperBuilder as developer_builder
import Developer as developer
import Trait as trait
import Experience_Levels as experience_levels

# Define all traits
trait_responsibility = trait.Trait(trait.Trait.RESPONSIBILITY, trait.Trait.RESPONSIBILITY_DESC)
trait_awareness = trait.Trait(trait.Trait.AWARENESS, trait.Trait.AWARENESS_DESC)
trait_honesty = trait.Trait(trait.Trait.HONESTY, trait.Trait.HONESTY_DESC)
trait_resiliency = trait.Trait(trait.Trait.RESILIENCY, trait.Trait.RESILIENCY_DESC)
trait_fairness = trait.Trait(trait.Trait.FAIRNESS, trait.Trait.FAIRNESS_DESC)
trait_attention_to_detail = trait.Trait(trait.Trait.ATTENTION_TO_DETAIL, trait.Trait.ATTENTION_TO_DETAIL_DESC)
trait_pragmatism = trait.Trait(trait.Trait.PRAGMATISM, trait.Trait.PRAGMATISM_DESC)

def print_developer_info(developer: developer.Developer):
    print(f"Developer Name: {developer.name}")
    print(f"Experience Level: {developer.experience_level}")
    print("Traits:")
    if developer.trait_responsibility:
        print(f" - {developer.trait_responsibility.name}: {developer.trait_responsibility.description}")
    if developer.trait_awareness:
        print(f" - {developer.trait_awareness.name}: {developer.trait_awareness.description}")
    if developer.trait_honesty:
        print(f" - {developer.trait_honesty.name}: {developer.trait_honesty.description}")
    if developer.trait_resiliency:
        print(f" - {developer.trait_resiliency.name}: {developer.trait_resiliency.description}")
    if developer.trait_fairness:
        print(f" - {developer.trait_fairness.name}: {developer.trait_fairness.description}")
    if developer.trait_attention_to_detail:
        print(f" - {developer.trait_attention_to_detail.name}: {developer.trait_attention_to_detail.description}")
    if developer.trait_pragmatism:
        print(f" - {developer.trait_pragmatism.name}: {developer.trait_pragmatism.description}")
    print("\n")

print("-"*40)
print()

# Build a Developer named "Alice"
builder = developer_builder.DeveloperBuilder()
builder.set_name("Alice") \
    .set_experience_level(experience_levels.SENIOR) \
    .add_trait_responsibility(trait_responsibility) \
    .add_trait_awareness(trait_awareness) \
    .add_trait_honesty(trait_honesty)

print_developer_info(builder.get_developer())

# Build a Developer named "John"
builder = developer_builder.DeveloperBuilder()
builder.set_name("John") \
    .set_experience_level(experience_levels.PRINCIPAL) \
    .add_trait_resiliency(trait_resiliency) \
    .add_trait_fairness(trait_fairness) \
    .add_trait_attention_to_detail(trait_attention_to_detail) \
    .add_trait_pragmatism(trait_pragmatism)

print_developer_info(builder.get_developer())

# Build a Developer named "Eve"
builder = developer_builder.DeveloperBuilder()
builder.set_name("Eve") \
    .set_experience_level(experience_levels.DISTINGUISHED) \
    .add_trait_responsibility(trait_responsibility) \
    .add_trait_pragmatism(trait_pragmatism) \
    .add_trait_honesty(trait_honesty) \
    .add_trait_attention_to_detail(trait_attention_to_detail)

print_developer_info(builder.get_developer())
print("-"*40)
print()