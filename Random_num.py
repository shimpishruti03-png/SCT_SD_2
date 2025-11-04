import tkinter as tk
from tkinter import messagebox
import random

# Create main window
root = tk.Tk()
root.title(" Number Guessing Game")
root.geometry("420x350")
root.config(bg="#f0f8ff")

# Generate a random number between 1 and 100
secret_number = random.randint(1, 100)

# Function to check user's guess
def check_guess():
    try:
        user_guess = int(entry_guess.get())

        if user_guess < 1 or user_guess > 100:
            messagebox.showwarning("Invalid", "Please enter a number between 1 and 100.")
            return

        if user_guess == secret_number:
            label_result.config(
                text=f" Correct! The number was {secret_number} ",
                fg="#2e7d32"
            )
            messagebox.showinfo("Congratulations!", "You guessed it right!")
            reset_game()
        else:
            label_result.config(text="❌ Try Again!", fg="#d62828")
            label_number.config(text=f"💡 The number was: {secret_number}", fg="#6a1b9a")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

# Function to reset the game
def reset_game():
    global secret_number
    secret_number = random.randint(1, 100)
    entry_guess.delete(0, tk.END)
    label_result.config(text="New game started! Guess the number ", fg="#000000")
    label_number.config(text="")

# Title label
label_title = tk.Label(
    root,
    text=" Guess The Number Game ",
    font=("Comic Sans MS", 18, "bold"),
    bg="#f0f8ff",
    fg="#1b4965"
)
label_title.pack(pady=15)

# Instructions label
label_instruction = tk.Label(
    root,
    text="I'm thinking of a number between 1 and 100.\nCan you guess it?",
    font=("Arial", 12),
    bg="#f0f8ff",
    fg="#023047"
)
label_instruction.pack(pady=10)

# Entry for user input
entry_guess = tk.Entry(
    root,
    font=("Arial", 14),
    width=10,
    justify="center",
    bg="#e3f2fd",
    relief="solid",
    bd=1
)
entry_guess.pack(pady=10)

# Buttons Frame
frame_buttons = tk.Frame(root, bg="#f0f8ff")
frame_buttons.pack(pady=5)

# Check guess button
btn_check = tk.Button(
    frame_buttons,
    text="Check Guess",
    font=("Arial", 12, "bold"),
    bg="#64b5f6",
    fg="white",
    activebackground="#42a5f5",
    activeforeground="white",
    padx=10,
    pady=5,
    relief="raised",
    command=check_guess
)
btn_check.grid(row=0, column=0, padx=10)

# Reset button
btn_reset = tk.Button(
    frame_buttons,
    text="Reset Game",
    font=("Arial", 12, "bold"),
    bg="#81c784",
    fg="white",
    activebackground="#66bb6a",
    activeforeground="white",
    padx=10,
    pady=5,
    relief="raised",
    command=reset_game
)
btn_reset.grid(row=0, column=1, padx=10)

# Result label
label_result = tk.Label(
    root,
    text="Start guessing! ",
    font=("Arial", 13, "italic"),
    bg="#f0f8ff",
    fg="#000000"
)
label_result.pack(pady=15)

# Label to show the generated number after guess
label_number = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#f0f8ff",
    fg="#6a1b9a"
)
label_number.pack(pady=5)




root.mainloop()

