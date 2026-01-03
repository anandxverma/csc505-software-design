# Main program logic for building Developer objects using the Builder Director Design Pattern
import DeveloperBuilder as developer_builder
import Developer as developer
import Experience_Levels as experience_levels

# Function to print Developer information
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
builder.build("Alice", experience_levels.SENIOR) \
    .add_trait_responsibility() \
    .add_trait_awareness() \
    .add_trait_honesty()

print_developer_info(builder.get_developer())

# Build a Developer named "John"
builder = developer_builder.DeveloperBuilder()
builder.build("John", experience_levels.PRINCIPAL) \
    .add_trait_resiliency() \
    .add_trait_fairness() \
    .add_trait_attention_to_detail() \
    .add_trait_pragmatism()

print_developer_info(builder.get_developer())

# Build a Developer named "Eve"
builder = developer_builder.DeveloperBuilder()
builder.build("Eve", experience_levels.DISTINGUISHED) \
    .add_trait_responsibility() \
    .add_trait_pragmatism() \
    .add_trait_honesty() \
    .add_trait_attention_to_detail()

print_developer_info(builder.get_developer())

# Simulate Error
builder = developer_builder.DeveloperBuilder()
builder.build("Mike", "Full Time") \
    .add_trait_responsibility() \
    .add_trait_pragmatism() \
    .add_trait_honesty() \
    .add_trait_attention_to_detail()

print_developer_info(builder.get_developer())
print("-"*40)
print()