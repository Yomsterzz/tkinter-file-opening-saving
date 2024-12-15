import tkinter as tk
from tkinter.filedialog import askopenfile, asksaveasfile

def open_file():
    filetoopen = askopenfile(mode="r", filetypes=[("python files", "*.py")])
    if filetoopen is not None:
        file_data = filetoopen.read()
        print(file_data)

def save_file():
    filetosave = asksaveasfile(filetypes=[("Text document", "*.txt"), ("All files", "*.*")], defaultextension=".txt")
    if filetosave is not None:
        for i in listbox.get(0, tk.END):
            print(i, file=filetosave)
            

window = tk.Tk()
window.geometry("800x600")
window.title("Save Machine")

list_data = ["hello", "goodbye"]

listbox = tk.Listbox(window, font=("Arial", 20))

for i in list_data:
    listbox.insert(tk.END, i)

listbox.pack(padx=10, pady=10)

open = tk.Button(window, text="Open", font=("Arial", 20), command=open_file)
open.pack(padx=10, pady=10)

save = tk.Button(window, text="Save", font=("Arial", 20), command=save_file)
save.pack(padx=10, pady=10)

window.mainloop()