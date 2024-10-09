import tkinter as tk

def reverse_text():
    input_text = entry.get()
    reversed_text = input_text[::-1]
    result_label.config(text=reversed_text)

    root = tk.Tk()
    root.title("Text Reverser")

    entry = tk.Entry(root, width=50)
    entry.pack(pady=10)
    reverse_button = tk.Button(root, text="Reverse Text", command=reverse_text)
    reverse_button.pack(pady=10)
    result_label = tk.Label(root, text="", font=("Helvetica", 14))
    result_label.pack(pady=10)

    root.mainloop()