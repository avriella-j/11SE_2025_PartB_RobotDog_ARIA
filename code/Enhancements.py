# Enhancements.py
# Robot Dog Dance Program (compatible with Control class)

import time
from Control import *

# Create Control object
control = Control()

# --- Dance Routines ---

def quick_dance():
    print("🎵 Starting Quick Dance (30 sec)...")
    for i in range(3):
        control.forWard()
        time.sleep(0.3)
        control.backWard()
        time.sleep(0.3)
    # Spin left
    for i in range(10, -10, -2):
        control.attitude(0, 0, i)
        time.sleep(0.05)
    # Spin right
    for i in range(-10, 10, 2):
        control.attitude(0, 0, i)
        time.sleep(0.05)
    control.stop()
    print("✅ Quick Dance Done!")

def full_dance():
    print("🎵 Starting Full Dance Routine (2-3 min)...")
    
    # Step forward
    for i in range(5):
        control.forWard()
    control.stop()
    
    # Wiggle left and right
    for i in range(10, -10, -1):
        control.attitude(0, 0, i)
        time.sleep(0.05)
    for i in range(-10, 10, 1):
        control.attitude(0, 0, i)
        time.sleep(0.05)
    
    # Step backward
    for i in range(5):
        control.backWard()
    control.stop()
    
    # Little "jump" effect by tilting up and down
    for i in range(5):
        control.attitude(5, 0, 0)
        time.sleep(0.1)
        control.attitude(-5, 0, 0)
        time.sleep(0.1)
    control.attitude(0, 0, 0)  # reset
    
    # Forward shuffle dance
    for i in range(3):
        control.forWard()
        time.sleep(0.2)
        control.backWard()
        time.sleep(0.2)
    
    control.stop()
    print("✅ Full Dance Done!")

def freestyle_dance():
    print("🎵 Starting Freestyle Dance...")
    
    moves = [
        lambda: control.forWard(),
        lambda: control.backWard(),
        lambda: control.attitude(0, 0, 15),
        lambda: control.attitude(0, 0, -15),
        lambda: control.attitude(10, 0, 0),
        lambda: control.attitude(-10, 0, 0),
    ]
    
    for i in range(10):
        move = moves[i % len(moves)]
        move()
        time.sleep(0.3)
    
    control.stop()
    print("✅ Freestyle Dance Done!")

# --- Menu ---
if __name__ == "__main__":
    print("Robot Dog Dance Options:")
    print("1. Full Dance Routine (2-3 minutes)")
    print("2. Quick Dance Test (30 seconds)")
    print("3. Freestyle Dance (random fun)")
    
    choice = input("Enter your choice (1/2/3): ")
    if choice == "1":
        full_dance()
    elif choice == "2":
        quick_dance()
    elif choice == "3":
        freestyle_dance()
    else:
        print("❌ Invalid choice, try again.")
