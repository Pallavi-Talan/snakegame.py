import random
import tkinter as tk
from tkinter import messagebox

# Main window
root = tk.Tk()
root.title("🎮 Guess The Game Hub")
root.geometry("400x400")

# ------------------ NUMBER GUESS GAME ------------------ #
def start_guess_game():
    game_window = tk.Toplevel(root)
    game_window.title("Guess The Number")
    game_window.geometry("350x350")

    number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7

    def check_guess():
        nonlocal attempts
        try:
            guess = int(entry.get())
            attempts += 1

            if guess > number:
                result_label.config(text="⬇️ Lower number please")
            elif guess < number:
                result_label.config(text="⬆️ Higher number please")
            else:
                messagebox.showinfo("🎉 जीत गए!", f"Correct! {attempts} tries me guess kiya 😎")
                game_window.destroy()

            if attempts >= max_attempts and guess != number:
                messagebox.showinfo("❌ Game Over", f"Number was {number}")
                game_window.destroy()

        except:
            result_label.config(text="⚠️ Enter valid number")

    tk.Label(game_window, text="Guess number (1-100)", font=("Arial", 14)).pack(pady=10)

    entry = tk.Entry(game_window)
    entry.pack(pady=5)

    tk.Button(game_window, text="Guess", command=check_guess).pack(pady=5)

    result_label = tk.Label(game_window, text="")
    result_label.pack(pady=10)

# ------------------ ROCK PAPER SCISSORS ------------------ #
def start_rps():
    game_window = tk.Toplevel(root)
    game_window.title("Rock Paper Scissors")
    game_window.geometry("350x300")

    choices = ["Rock", "Paper", "Scissors"]

    def play(user_choice):
        comp_choice = random.choice(choices)

        if user_choice == comp_choice:
            result = "😐 Draw"
        elif (user_choice == "Rock" and comp_choice == "Scissors") or \
             (user_choice == "Paper" and comp_choice == "Rock") or \
             (user_choice == "Scissors" and comp_choice == "Paper"):
            result = "🎉 You Win!"
        else:
            result = "😢 You Lose!"

        result_label.config(text=f"You: {user_choice}\nComputer: {comp_choice}\n{result}")

    tk.Label(game_window, text="Choose:", font=("Arial", 14)).pack(pady=10)

    for choice in choices:
        tk.Button(game_window, text=choice, command=lambda c=choice: play(c)).pack(pady=5)

    result_label = tk.Label(game_window, text="")
    result_label.pack(pady=10)

# ------------------ MAIN MENU ------------------ #
tk.Label(root, text="🎮 GUESS THE GAME HUB", font=("Arial", 16, "bold")).pack(pady=20)

tk.Button(root, text="🎯 Number Guess Game", width=20, command=start_guess_game).pack(pady=10)
tk.Button(root, text="✊ Rock Paper Scissors", width=20, command=start_rps).pack(pady=10)

tk.Label(root, text="More games coming soon 😎").pack(pady=20)

# Run app
root.mainloop()
