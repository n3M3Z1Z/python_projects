#!/ust/bin/env python3

# Import the fun stuff

import tkinter as tk
from tkinter import messagebox

# User inputs for numbers and operation
def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = entry_operation.get()

# Calculation based on the selected operation

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            # Checking for division by zero
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed. Get a coffee and refresh your math")
            result = num1 / num2
        else:
            raise ValueError("Invalid operation")
# Output the result
        messagebox.showinfo("Result", f"The result is: {result}. Next time your your head stupid")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers and operation.")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Division by zero is not allowed. Get a coffee and refresh your math")

def clear():
    entry_num1.delete(0, tk.END)
    entry_num2.delete(0, tk.END)
    entry_operation.delete(0, tk.END)


# Create main window
root = tk.Tk()
root.title("Brutal Calculator")

# Labels
tk.Label(root, text="First Number:").grid(row=0, column=0)
tk.Label(root, text="Second Number:").grid(row=1, column=0)
tk.Label(root, text="Operation (+, -, *, /):").grid(row=2, column=0)

# Entry widgets
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)
entry_operation = tk.Entry(root)
entry_operation.grid(row=2, column=1)

# Buttons
tk.Button(root, text="Calculate", command=calculate).grid(row=3, column=0, columnspan=2, pady=10)
tk.Button(root, text="Clear", command=clear).grid(row=4, column=0, columnspan=2)

# Run the main event loop
root.mainloop()
