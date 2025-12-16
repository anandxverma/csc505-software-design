import Actor as actor
import UMLConstants as constants
import UseCaseFunction as ucf
import UseCase as uc

# Function to print the summary of a use case
def print_use_case_summary(use_case: uc.UseCase):
    print(f"Use Case: {use_case.name}")
    print(f"Description: {use_case.desc}")
    print("Use Case Functions:")
    for f in use_case.use_case_functions:
        print(f"  - Function: {f.name}")
        print(f"    Description: {f.desc}")
        print("    Actors:")
        for a in f.actors:
            print(f"      * Type: {a.type}, Description: {a.desc}")
    print("\n")

# Define actors for the Citizen use case
actor_citizen = actor.Actor(constants.ACTOR_TYPE_USER, "Citizen")
actor_pothole_damage_report = actor.Actor(constants.ACTOR_TYPE_ENTITY, "Pothole Damage Report")
actor_property_damage_claim = actor.Actor(constants.ACTOR_TYPE_ENTITY, "Property Damage Claim")

# Define use case functions for the Citizen use case
# use Case Function = Report Pothole Damage
ucf_citizen_1 = ucf.UseCaseFunction("Report Pothole Damage", "Report Pothole Damage to the city authorities.")
ucf_citizen_1.add_actor(actor_citizen)
ucf_citizen_1.add_actor(actor_pothole_damage_report)

# use Case Function = Track Pothole Repair Status
ucf_citizen_2 = ucf.UseCaseFunction("Track Pothole Repair Status", "Track Pothole Repair Status reported via the PHTRS")
ucf_citizen_2.add_actor(actor_citizen)
ucf_citizen_2.add_actor(actor_pothole_damage_report)

# use Case Function = Submit Property Damage Claim
ucf_citizen_3 = ucf.UseCaseFunction("Submit Property Damage Claim", "Submit Property Damage Claim for damages caused by potholes.")
ucf_citizen_3.add_actor(actor_citizen)
ucf_citizen_3.add_actor(actor_property_damage_claim)

# use Case Function = Track Property Damage Claim Status
ucf_citizen_4 = ucf.UseCaseFunction("Track Property Damage Claim Status", "Track Property Damage Claim Status submitted for pothole-related damages.")
ucf_citizen_4.add_actor(actor_citizen)
ucf_citizen_4.add_actor(actor_property_damage_claim)

# Define the Citizen use case
uc_citizen = uc.UseCase("Citizen Specific Use Cases", "These use cases represent the actions taken by the Citizen and features available for them.")
uc_citizen.add_use_case_function(ucf_citizen_1)
uc_citizen.add_use_case_function(ucf_citizen_2)
uc_citizen.add_use_case_function(ucf_citizen_3)
uc_citizen.add_use_case_function(ucf_citizen_4)

# Print the summary of the Citizen use case
print_use_case_summary(uc_citizen)

# Define actors for the Admin use case
actor_admin = actor.Actor(constants.ACTOR_TYPE_USER, "Public Works Admin")
actor_work_order = actor.Actor(constants.ACTOR_TYPE_ENTITY, "Work Order")
actor_sys_config = actor.Actor(constants.ACTOR_TYPE_ENTITY, "System Configuration")
actor_pothole = actor.Actor(constants.ACTOR_TYPE_ENTITY, "Pothole")
actor_report = actor.Actor(constants.ACTOR_TYPE_ENTITY, "Report")
actor_repair_crew = actor.Actor(constants.ACTOR_TYPE_USER, "Repair Crew")

# Define use case functions for the Admin use case
# use Case Function = System Configuration
ucf_admin_1 = ucf.UseCaseFunction("Configure System", "Configure System (Manage Potholes Database, Set Up System Security etc)")
ucf_admin_1.add_actor(actor_admin)
ucf_admin_1.add_actor(actor_sys_config)

# use Case Function = Create Work Order
ucf_admin_2 = ucf.UseCaseFunction("Create Work Order", "Create Work Order (Assign Pothole, Crew, Equipment etc))")
ucf_admin_2.add_actor(actor_admin)
ucf_admin_2.add_actor(actor_work_order)

# use Case Function = Update Work Order
ucf_admin_3 = ucf.UseCaseFunction("Update Work Order", "Update Work Order (Change Details)")
ucf_admin_3.add_actor(actor_admin)
ucf_admin_3.add_actor(actor_work_order)

# use Case Function = Manage Potholes Database
ucf_admin_4 = ucf.UseCaseFunction("Manage Potholes Database", "Manage Potholes Database (Add, Update, Delete Pothole Records)")
ucf_admin_4.add_actor(actor_admin)
ucf_admin_4.add_actor(actor_pothole)

# use Case Function = View Reports
ucf_admin_5 = ucf.UseCaseFunction("View Reports", "View Reports (Pothole Repair Status, Work Order Status etc)")
ucf_admin_5.add_actor(actor_admin)
ucf_admin_5.add_actor(actor_report)

# use Case Function = Notifications
ucf_admin_6 = ucf.UseCaseFunction("Notifications", "Send Notifications (Alert Citizens and Repair Crews about Status Changes and Pending Work Orders etc)")
ucf_admin_6.add_actor(actor_admin)
ucf_admin_6.add_actor(actor_citizen)
ucf_admin_6.add_actor(actor_repair_crew)

# Define the Admin use case
uc_admin = uc.UseCase("Administrator Specific Use Cases", "These use cases represent the actions taken by the Public Works Admin and features available for them.")
uc_admin.add_use_case_function(ucf_admin_1)
uc_admin.add_use_case_function(ucf_admin_2)
uc_admin.add_use_case_function(ucf_admin_3)
uc_admin.add_use_case_function(ucf_admin_4)
uc_admin.add_use_case_function(ucf_admin_5)
uc_admin.add_use_case_function(ucf_admin_6)

# Print the summary of the Citizen use case
print_use_case_summary(uc_admin)

# Define use case functions for the Repair use case
# use Case Function = Update Work Order
ucf_repair_crew_1 = ucf.UseCaseFunction("Update Work Order", "Update Work Order (Update Status, Notes etc)")
ucf_repair_crew_1.add_actor(actor_repair_crew)
ucf_repair_crew_1.add_actor(actor_work_order)

# use Case Function = Notifications
ucf_repair_crew_2 = ucf.UseCaseFunction("Notifications", "Send Notifications (Alert Citizens and Admin about Status Changes)")
ucf_repair_crew_2.add_actor(actor_admin)
ucf_repair_crew_2.add_actor(actor_citizen)

# Define the Admin use case
uc_repair_crew = uc.UseCase("Repair Crew Specific Use Cases", "These use cases represent the actions taken by the Repair Crew and features available for them.")
uc_repair_crew.add_use_case_function(ucf_repair_crew_1)
uc_repair_crew.add_use_case_function(ucf_repair_crew_2)

# Print the summary of the Citizen use case
print_use_case_summary(uc_repair_crew)