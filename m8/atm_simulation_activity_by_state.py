import time

def print_step(step_name):
    """Prints a state or action step."""
    print(f"[*] STEP: {step_name}")
    time.sleep(0.5)

def get_user_decision(question):
    """Helper to get a yes/no decision from the user."""
    while True:
        response = input(f"[?] DECISION: {question} (y/n): ").lower().strip()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("    Please enter 'y' for Yes or 'n' for No.")

def simulate_atm(debit_card_number):
    print("--- ATM TRANSACTION FLOW SIMULATION ---")
    
    # 1. Initiation
    print_step(f"New Session with Debit Card: {debit_card_number}")
    print_step("Validate Debit Card")

    # 2. Card Validation Decision
    is_card_valid = get_user_decision("Is the Debit Card valid?")
    
    if not is_card_valid:
        print_step("Card Invalid -> Session Ended")
        return # Exit simulation

    print_step("Debit Card Validated Successfully")

    # 3. PIN Entry Loop
    pin_counter = 1
    max_tries = 3
    pin_validated = False

    while not pin_validated:
        print(f"\n[Step] Please enter your PIN (Attempt {pin_counter}/{max_tries}).")
        _ = input("Input: Enter 4-digit PIN: ") # Variable nt used, just simulating input

        print_step("Validate ATM Pin")
        
        # In a real app, we'd compare numbers. Here we ask the user to simulate the backend check.
        print("[Step] Validating PIN...")
        is_pin_valid = input("Decision: Is the PIN correct? (y/n): ").strip().lower()

        if is_pin_valid == 'y':
            pin_validated = True
            print_step("ATM Pin Validated")
        else:
            print_step("ATM Pin Invalid")            
            if pin_counter >= max_tries:
                print_step("Reached Max Tries? -> YES")
                print_step("Session Ended")
                return # Exit simulation
            else:
                # "Increment Pin Counter by 1"
                print("[Info] Incorrect PIN. Please try again.")
                pin_counter += 1
    
    # 4. Main Transaction Loop
    session_active = True
    
    while session_active:
        print_step("List of Actions Displayed")
        print("1. Withdrawal")
        print("2. Check Balance (Other Action)")
        
        # Decision: Withdrawal or Other?
        # The diagram focuses on Withdrawal, so we ask specifically about that.
        is_withdrawal = get_user_decision("Did the user choose 'Withdrawal'?")
        
        if not is_withdrawal:
            print_step("Other Action Chosen")
            # The diagram implies we might loop back or end, 
            # but usually 'Other Action' executes and then we check for another transaction.
            print("    (Executing other action...)")
        else:
            # Withdrawal Flow
            print_step("Withdrawal Action Chosen")
            print_step("Retrieve Accounts List")
            
            # Withdrawal Amount Loop (Implicit in "Return to Accounts List" on failure)
            transaction_successful = False
            
            while not transaction_successful:
                print("\n[Step] Displaying Accounts List:")
                print("1. Checkings ending in 3456")
                print("2. Savings ending in 0987")

                _ = input("Input: Choose an Account to withdraw from (1 or 2): ").strip()

                # "Prompt to enter Amount and accept input"
                _ = input("Input: Enter Amount to withdraw: ")

                print_step("Check Account Balance")
                
                has_funds = get_user_decision("Are there enough funds in the account?")
                
                if has_funds:
                    print_step("Amount Dispensed & Account Balance Updated")
                    transaction_successful = True # Exit the withdrawal loop
                else:
                    print_step("Enough Funds? -> NO")
                    print("    (Looping back to Account List...)")
                    # Loops back to Accounts List Displayed
        
        # 5. Completion / New Transaction
        print_step("Check for Another Transaction")
        do_another = get_user_decision("Does the user want another transaction?")
        
        if do_another:
            print("    (Looping back to Action List...)")
            # Loops back to List of Actions Displayed
        else:
            session_active = False

    print_step("Session Ended")
    print("--- SIMULATION COMPLETE ---")

card_number = input("Enter Debit Card Number to start ATM simulation or press enter to choose 1111-2222-3333-4444: ").strip()
if not card_number:
    card_number = "1111-2222-3333-4444"
simulate_atm(card_number)