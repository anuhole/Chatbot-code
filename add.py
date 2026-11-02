print("Home Automation Bot")
name = input("Enter your name: ").strip()
role = input("Enter your role (user/admin): ").strip().lower()

# A dictionary allows the admin to dynamically add new devices
devices = {
    "Lights": False,
    "Fan": False,
    "AC": False,
    "TV": False,
    "Door": True  # True = Locked
}
temp = 25

while True:
    print(f"\n--- Hello, {name} ({role.upper()})! ---")
    
    # 1. Dynamically generate the menu based on current devices
    device_names = list(devices.keys())
    menu_counter = 1
    
    for i, device in enumerate(device_names, start=1):
        action = "lock/unlock" if device == "Door" else "switch on/off"
        print(f"Press {i} to {action} the {device}")
        menu_counter += 1
        
    temp_option = str(menu_counter)
    print(f"Press {temp_option} to set AC temperature")
    
    exit_option = str(menu_counter + 1)
    print(f"Press {exit_option} to exit")
    
    # 2. Show admin-only system commands
    admin_add_option = str(menu_counter + 2)
    if role == "admin":
        print("\n--- System Commands (Admin Only) ---")
        print(f"Press {admin_add_option} to add a new device")

    choice = input("\nEnter your choice: ").strip()

    # 3. Handle dynamic device selection (Options 1 through number of devices)
    if choice.isdigit() and 1 <= int(choice) <= len(device_names):
        selected_device = device_names[int(choice) - 1]
        
        # Toggle the boolean state in the dictionary
        devices[selected_device] = not devices[selected_device]
        
        if selected_device == "Door":
            state = "Locked" if devices[selected_device] else "Unlocked"
        else:
            state = "ON" if devices[selected_device] else "OFF"
            
        print(f"-> {selected_device} is now {state}.")
        
    # 4. Handle Temperature
    elif choice == temp_option:
        new_temp = input(f"Enter new temperature (Current: {temp}°C): ").strip()
        if not new_temp:
            print("Error: Input cannot be empty. Please enter a valid temperature.")
        else:
            try:
                temp_val = int(new_temp)
                if temp_val < 5 or temp_val > 32:
                    print(f"Warning: {temp_val}°C is out of range! Please enter a value between 5 and 32.")
                else:
                    temp = temp_val
                    print(f"-> Temperature successfully set to {temp}°C.")
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
                
    # 5. Handle Exit
    elif choice == exit_option:
        print(f"Goodbye {name}!")
        break
        
    # 6. Handle Admin Command: Add new device
    elif role == "admin" and choice == admin_add_option:
        new_device = input("Enter the name of the new device to add (e.g., Heater, Camera): ").strip().capitalize()
        
        if not new_device:
            print("Error: Device name cannot be empty.")
        elif new_device in devices:
            print(f"Error: '{new_device}' already exists on the network.")
        else:
            # Add the new device to the dictionary with a default state of False (OFF)
            devices[new_device] = False
            print(f"-> Success: System command executed. '{new_device}' added to the network.")
            
    # 7. Exception handling for invalid options
    else:
        print(f"Option '{choice}' doesn't exist or you don't have permission. Please choose again.")