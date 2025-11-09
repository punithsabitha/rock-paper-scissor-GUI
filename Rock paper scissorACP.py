import tkinter as tk, random

def play(user):
    comp = random.choice(["Rock", "Paper", "Scissor"])
    user_lbl.config(text=f"User: {user}")
    comp_lbl.config(text=f"Computer: {comp}")
    if user == comp: res = "It's a Tie!"
    elif (user, comp) in [("Rock","Scissor"),("Paper","Rock"),("Scissor","Paper")]:
        res = "You Win!"
    else: res = "Computer Wins!"
    result_lbl.config(text=res)

def reset():
    user_lbl.config(text="User:")
    comp_lbl.config(text="Computer:")
    result_lbl.config(text="Result:")

root = tk.Tk(); root.title("Rock Paper Scissor"); root.geometry("350x250")
tk.Label(root, text="Rock Paper Scissor", font=("Arial",16,"bold")).pack(pady=10)
f = tk.Frame(root); f.pack()
for ch in ["Rock","Paper","Scissor"]:
    tk.Button(f, text=ch, width=10, command=lambda c=ch: play(c)).pack(side="left", padx=5)
user_lbl = tk.Label(root, text="User:", font=("Arial",12)); user_lbl.pack()
comp_lbl = tk.Label(root, text="Computer:", font=("Arial",12)); comp_lbl.pack()
result_lbl = tk.Label(root, text="Result:", font=("Arial",14,"bold"), fg="blue"); result_lbl.pack(pady=10)
tk.Button(root, text="Reset Game", bg="orange", command=reset).pack(pady=5)
root.mainloop()

