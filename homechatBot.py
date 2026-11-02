print("Home Automation Bot")
name = input("Enter your name: ")

lightOn = False
fanOn = False
acOn = False
tvOn = False
doorLock = True
temp = 25

while True:
    print(f"\nHello, {name}! Please choose an option:")
    print("Press 1 to switch on/off the lights")
    print("Press 2 to switch on/off the fan")
    print("Press 3 to switch on/off the AC")
    print("Press 4 to switch on/off the TV")
    print("Press 5 to lock/unlock the door")
    print("Press 6 to set AC temperature")
    print("Press 7 to exit")

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        lightOn = not lightOn
        state = "ON" if lightOn else "OFF"
        print(f"Lights are now {state}.")
        
    elif choice == "2":
        fanOn = not fanOn
        state = "ON" if fanOn else "OFF"
        print(f"Fan is now {state}.")
        
    elif choice == "3":
        acOn = not acOn
        state = "ON" if acOn else "OFF"
        print(f"AC is now {state}.")
        
    elif choice == "4":
        tvOn = not tvOn
        state = "ON" if tvOn else "OFF"
        print(f"TV is now {state}.")
        
    elif choice == "5":
        doorLock = not doorLock
        state = "Locked" if doorLock else "Unlocked"
        print(f"Door is now {state}.")
        
    elif choice == "6":
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
                    print(f"Temperature successfully set to {temp}°C.")
            except ValueError:
                print("Error: Invalid input. Please enter a number.")
                
    elif choice == "7":
        print(f"Goodbye {name}!")
        break
        
    else:
        print(f"Option '{choice}' doesn't exist. Please choose again.")