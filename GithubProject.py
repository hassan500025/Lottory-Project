#   Lottory Project  :
#   Tkinter Package :
    
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import random


def select_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text Files", " *.txt")])
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, file_path)


def select_winners():
    file_path = file_entry.get()
    try:
        num = int(winners_entry.get())
        if num <= 0:
            messagebox.showwarning("WRONG NUMBER",
                                   "The entered number must be greater than zero.")
            return
    except ValueError:
        messagebox.showwarning("!!!WRONG!!!", "Please enter a number .")
        return
    #
    try:
        #  exist file?
        with open(file_path, "r") as file:
            name_list = file.read().splitlines()
            print(name_list)
            # number in list
            if len(name_list) < num:
                messagebox.showwarning("WRONGNUMBER",
                                       "The selected number is greater than the total number")
            winners_list=random.sample(name_list,num)
            top_window=tk.Toplevel()
            top_window.title("Winners list")
            top_window.geometry("400x600")
            top_window.configure(background="black")
            win_label = ttk.Label(top_window, text=" WINNERS", font=("Sanserif", 30),
                                      background="black", foreground="#239B56")
            win_label.pack(pady=15)
            winners_list=[f"{i+1}--{j} "for i,j in enumerate(winners_list)]
            winners="\n".join(winners_list)
            show_winners=ttk.Label(top_window, text=winners, font=("Sanserif", 25),
                                      background="black", foreground="#9FE2BF")
            show_winners.pack(pady=12)
            top_window.mainloop()
    except  FileNotFoundError:
        messagebox.showwarning("WRONG",
                               "The file is not found!!!")

    except  Exception  as e:
        messagebox.showwarning("ERROR",
                               str(e))


window = tk.Tk()
window.title("lottery program")
window.geometry("500x500")
window.configure(background="black")


Title_label = ttk.Label(window, text=" lottery program", font=("Sanserif", 40),background="black"
                          , foreground="#6C3483")
Title_label.pack(pady=2)

file_label = ttk.Label(window, text=" 1.Please select the participants file.", font=("Sanserif", 14),
                       background="black", foreground="gray")

file_label.pack(pady=20)

style = ttk.Style()
style.configure("TFrame", background="#D7BDE2")

file_frame = ttk.Frame(window, style="TFrame")
file_frame.pack()

file_entry = ttk.Entry(file_frame, font=("Sanserif", 14))
file_entry.grid(row=0, column=0, padx=3, pady=3)

file_button = ttk.Button(file_frame, text="choose a file", command=select_file)
file_button.grid(row=0, column=1, padx=3, pady=3)
#

winners_label = ttk.Label(window, text=" 2.Please Select the number of winners.",  font=("Sanserif", 14),
                       background="black", foreground="gray")
winners_label.pack(pady=20)

winners_entry = ttk.Entry(window, font=("Sanserif", 14))
winners_entry.pack()

select_button = ttk.Button(window, text="choose winners", command=select_winners)
select_button.pack(pady=5)

window.mainloop()
