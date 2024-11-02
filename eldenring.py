import random
import time
from tkinter import messagebox, simpledialog, Tk

# Function to print with colors
def print_color(color, text):
    colors = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
    }
    end_color = "\033[0m"
    print(colors.get(color, ""), text, end_color)

# Function for battles
def battle(beast_range):
    beast = random.randint(beast_range[0], beast_range[1])

    # Simulate GUI battle animation
    messagebox.showinfo("Battle", "Get ready to battle! Beast is attacking!")

    # Simulate GUI waiting animation
    time.sleep(1)

    tarnished = simpledialog.askstring("Battle", f"Pick a number between {beast_range[0]}-{beast_range[1]}.")
    if tarnished.isdigit() and beast_range[0] <= int(tarnished) <= beast_range[1]:
        tarnished = int(tarnished)
        if beast == tarnished:
            print_color("green", "Beast VANQUISHED! Congrats fellow tarnished.")
        else:
            print_color("red", "You Died!")
            exit(1)
    elif tarnished.lower() == "coffee":
        print_color("green", "Cheat code activated! Beast defeated with coffee.")
    else:
        print_color("red", f"Invalid input! You must pick a number between {beast_range[0]}-{beast_range[1]} or enter 'coffee'.")
        exit(1)

    # Simulate GUI waiting animation
    time.sleep(2)


# Welcome Message
print_color("blue", "Welcome")
time.sleep(1)

# Choose if you're up to the task
root = Tk()
root.withdraw()
ready = simpledialog.askstring("Ready?", "Are you ready? (y/n)")
if ready.lower() == "y":
    print_color("green", "You're awesome")
else:
    print_color("red", "Leave right now! - Bye!")
    exit(0)

time.sleep(1)

# First beast battle
battle([0, 1])

# Second beast battle (easier)
battle([0, 5])

# More difficult fights
for i in range(3, 11):
    beast_range = [0, 10 + i]
    print_color("yellow", f"Fight {i-1}! Get ready! Pick a number between {beast_range[0]}-{beast_range[1]}.")
    battle(beast_range)

print_color("green", "Congratulations on your victories!")
