import tkinter as tk
import random

# window setup
root = tk.Tk()
root.title("Calculator Game 🎮")
root.geometry("400x500")
root.configure(bg="black")

score = 0
question_count = 0

# question generator
def new_question():
    global num1, num2, op, answer

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        answer = num1 + num2
    elif op == "-":
        answer = num1 - num2
    else:
        answer = num1 * num2

    question_label.config(text=f"{num1} {op} {num2} = ?")

# check answer
def check_answer():
    global score, question_count

    try:
        user = int(entry.get())
        if user == answer:
            result_label.config(text="✅ Correct!", fg="green")
            score += 1
        else:
            result_label.config(text=f"❌ Wrong! Ans: {answer}", fg="red")

        question_count += 1
        score_label.config(text=f"Score: {score}")

        entry.delete(0, tk.END)

        if question_count < 5:
            root.after(1000, new_question)
        else:
            question_label.config(text="Game Over 🎯")
            result_label.config(text=f"Final Score: {score}/5", fg="yellow")

    except:
        result_label.config(text="⚠️ Enter number only", fg="orange")

# UI elements
title = tk.Label(root, text="Calculator Game 🎮", font=("Arial", 18, "bold"), bg="black", fg="white")
title.pack(pady=20)

question_label = tk.Label(root, text="", font=("Arial", 22), bg="black", fg="cyan")
question_label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 18), justify="center")
entry.pack(pady=10)

submit_btn = tk.Button(root, text="Submit", font=("Arial", 14), command=check_answer, bg="blue", fg="white")
submit_btn.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 14), bg="black")
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score: 0", font=("Arial", 14), bg="black", fg="white")
score_label.pack(pady=10)

# start game
new_question()

root.mainloop()
