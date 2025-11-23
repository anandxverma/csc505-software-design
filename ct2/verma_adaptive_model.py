import ProcessModel as model
import ProcessModelPhase as phase
import PhaseTask as task

# This program implements VermaAdaptive Model for Software Development
# Users can interact with this program to learn more about the VermaAdaptive Model
# User can learn the details of each phases in the VermaAdaptive Model and the overall process

# Create an instance of ProcessModel for VermaAdaptive Model
verma_adaptive_model = model.ProcessModel("Verma Adaptive Model", "The VermaAdaptive model is an iterative software development process that emphasizes flexibility, continuous improvement, and effective communication, enabling regular updates and enhancements. It has seven distinct phases.")

# Add phases to the VermaAdaptive Model
# Each item in the list is a tuple of (phase_name, phase_description, task1, task2, ...)
phases_info = [
    ("Communication", "Understanding the Problem Statement and Scope.", ("Indentiy Stakeholder", "Define Scope", "Gather Requirements")),
    
    ("Planning", "Translating the requirements into a project roadmap and assessing risks.", ("Requirements Analysis", "Refine Project Scope", "Technology Choice", "Create Work Breakdown Structure (WBS)", "Estimation & Scheduling", "Risk Assessment")),
    
    ("Modeling", "Creating a software blueprint including architecture designs, data models, UI designs, and technical documentation, and POC for technical feasibility.", ("High-level Design - Architecture, Technology, Systems, Integration", "Data Model Design", "User Interface Design", "Detailed Design", "Technical Documentation", "Technology Proof Of Concepts (POC)", "Define Coding Standards", "Define Reusables Components - Patterns, Logging, Error Handling", "Define Security Standards")),
    
    ("Construction", "Building the software through iterative development, coding, and testing.", ("Coding", "Testing", "Prototyping", "Technical Documentation", "CI/CD Automation")),
    
    ("Deployment", "Deploying and releasing the software to end users, providing training, and getting a formal sign-off.", ("Deployment Planning", "Final Build and Packaging", "Data Load and Migration", "User Acceptance Testing (UAT)", "Training", "User Acceptance and Sign-off")),
    
    ("Post Deployment", "Providing post-deployment support and monitoring software health.", ("Monitoring", "Support")),
    
    ("Umbrella Activities", "Providing a framework for activities applicable to multiple phases in the model.", ("Project Tracking & Management", "Risk Management", "Quality Assurance", "Enterprise Architecture Review", "Ensure efficient communication flow"))
]
for name, description, tasks in phases_info:
    verma_phase = phase.ProcessModelPhase(name, description)
    for task_name in tasks:
        verma_task = task.PhaseTask(task_name, "")
        verma_phase.add_task(verma_task)
    verma_adaptive_model.add_phase(verma_phase)

# Method to print interactive menu
def print_menu():
    print()
    print("="*40)
    print("Select an Action:")
    print("1 - View Process Model Summary")
    print("2 - View Process Model Details")
    print("3 - View Summary of a Phase")
    print("4 - View Details of a Phase")
    print("5 - Add a New Phase *")
    print("6 - Remove a Phase *")
    print("q - Quit")
    print("-"*40)
    print("* - Method not implemeneted yet")
    print()
    return input("Choose an action: ").lower()

# Menu Action 1: View Process Model Summary
def view_model_summary():
    print()
    print("."*60)
    print(f"Process Model: {verma_adaptive_model.name}")
    print(f"Description: {verma_adaptive_model.description}")
    print(f"Total Phases: {verma_adaptive_model.get_total_phases()}")
    print("."*60)

# Menu Action 2: View Process Model Details
def view_model_details():
    print()
    print("."*60)
    print("Process Model Details:")
    print("."*60)
    print(f"Name: {verma_adaptive_model.name}")
    print(f"Description: {verma_adaptive_model.description}")
    print("."*60)
    print("Phases:")
    print("."*60)
    for idx, phase_instance in enumerate(verma_adaptive_model.phases, start=1):
        print(f"{idx}. {phase_instance.name} - {phase_instance.description}")
    print("."*60)
    print(f"Total Phases: {verma_adaptive_model.get_total_phases()}")
    print("."*60)

#Menu Action 3: View Summary of a Phase
def view_phase_summary(phase_name):
    phase_instance = verma_adaptive_model.get_phase_by_name(phase_name)
    if phase_instance:
        print()
        print("."*60)
        print(f"Phase: {phase_instance.name}")
        print(f"Description - {phase_instance.description}")
        print("."*60)
    else:
        print("Phase not found in the VermaAdaptive Model.")

# Menu Action 4: View Details of a Phase
def view_phase_details(phase_name):
    phase_instance = verma_adaptive_model.get_phase_by_name(phase_name)
    if phase_instance:
        print()
        print("."*60)
        print(f"Phase: {phase_instance.name}")
        print(f"Description - {phase_instance.description}")
        print("."*60)
        print("Tasks:")
        print("."*60)
        for idx, task_instance in enumerate(phase_instance.tasks, start=1):
            print(f"{idx}. {task_instance.name}")
        print("."*60)
        print(f"Total Tasks: {phase_instance.get_total_tasks()}")
        print("."*60)
    else:
        print("Phase not found in the VermaAdaptive Model.")

# Interact with the Model
action = print_menu()
while action != "q":
    print()
    if action == "1":
        view_model_summary()
    elif action == "2":
        view_model_details()
    elif action == "3":
        phase_name = input("Enter the Phase Name: ").strip()
        phase_instance = verma_adaptive_model.get_phase_by_name(phase_name)
        if phase_instance:
            view_phase_summary(phase_name)
        else:
            print(f"Phase '{phase_name}' not found in the VermaAdaptive Model.")
    elif action == "4":
        phase_name = input("Enter the Phase Name: ").strip()
        phase_instance = verma_adaptive_model.get_phase_by_name(phase_name)
        if phase_instance:
            view_phase_details(phase_name)
        else:
            print(f"Phase '{phase_name}' not found in the VermaAdaptive Model.")
    elif action == "5":
        print("Add Phase functionality is not implemented yet.")
    elif action == "6":
        print("Remove Phase functionality is not implemented yet.")
    else:
        print("INVALID ACTION. Please try again.")
    action = print_menu()
