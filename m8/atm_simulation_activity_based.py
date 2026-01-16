def atm_simulation():
    print("--- ATM Transaction Start ---")
    
    # Step 1: Accept Debit Card Details
    print("\n[Step] Accepting Debit Card Details...")
    
    # Step 2: Validate Card Details
    print("[Step] Validating Card Details...")
    is_card_valid = input("Decision: Is the card valid? (y/n): ").strip().lower()
    
    if is_card_valid != 'y':
        print("[End] Invalid Card. Ejecting card.")
        return

    # Step 3: PIN Validation Loop
    # "Set Valid PIN Counter to 1"
    pin_counter = 1
    max_tries = 3
    pin_verified = False

    while not pin_verified:
        # "Prompt for Pin and accept input"
        print(f"\n[Step] Please enter your PIN (Attempt {pin_counter}/{max_tries}).")
        _ = input("Input: Enter 4-digit PIN: ") # Variable nt used, just simulating input
        
        # "Validate Pin"
        print("[Step] Validating PIN...")
        is_pin_valid = input("Decision: Is the PIN correct? (y/n): ").strip().lower()
        
        if is_pin_valid == 'y':
            pin_verified = True
            print("[Info] PIN Accepted.")
        else:
            # "Reached Max Tries?"
            if pin_counter >= max_tries:
                print("\n[End] Max PIN attempts reached. Card locked/ejected.")
                return
            else:
                # "Increment Pin Counter by 1"
                print("[Info] Incorrect PIN. Please try again.")
                pin_counter += 1

    # Main Transaction Loop
    while True:
        # Step 4: Action Selection
        # "Prompt Actions List and accept chosen Action"
        print("\n[Step] Displaying Action List:")
        print("1. Withdrawal")
        print("2. Check Balance (Other Action)")
        
        action = input("Input: Choose an action (1 or 2): ").strip()
        
        # "Withdrawal Action chosen?"
        if action == '1':
            print("\n--- Withdrawal Flow ---")
            
            # "Retrieve & show Accounts List"
            print("[Step] Retrieving and showing Accounts List...")
            print(" - Checking")
            print(" - Savings")
            
            # "Prompt to choose Account and accept input"
            _ = input("Input: Choose Account (e.g., Checking): ")
            
            # "Prompt to enter Amount and accept input"
            _ = input("Input: Enter Amount to withdraw: ")
            
            # "Check Account Balance"
            print("[Step] Checking Account Balance...")
            
            # "Acc has enugh funds?"
            has_funds = input("Decision: Does account have enugh funds? (y/n): ").strip().lower()
            
            if has_funds == 'y':
                # "Dispense Amount & update Account Balance"
                print("[Step] Dispensing Amount...")
                print("[Step] Updating Account Balance...")
                print("[Info] Please take your cash.")
            else:
                print("[Info] Insufficient funds. Transaction cancelled.")
        
        else:
            # Path for "n" on "Withdrawal Action chosen?"
            # (The diagram implies other actions exist, though only Withdrawal is detailed)
            print("\n[Step] Performing selected nn-withdrawal action...")
            print("[Info] Action completed.")

        # Step 5: Session Continuation
        # "Prompt for anther Transaction or end the session"
        print("\n[Step] Transaction complete.")
        
        # "Anther Transaction?"
        retry = input("Decision: Perform anther transaction? (y/n): ").strip().lower()
        
        if retry != 'y':
            # "End the session & logout"
            print("\n[End] Ending session...")
            print("[End] Logging out. Please take your card.")
            break
        
        print("\n[Info] Returning to Action List...")

atm_simulation()