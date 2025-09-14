import tkinter as tk

window = tk.Tk()
window.title("simple hello")
window.geometry("300x300")
window.configure(bg = "lightblue")

tapcount = 0
def tapUpdate():
    global tapcount
    tapcount = tapcount+1
    print(tapcount)
    label_count.configure(text= tapcount)

label_tap = tk.Label(window, text = "Tap Count", bg = "yellow")
label_tap.pack()

label_count = tk.Label(window,text ="0", bg ="grey")
label_count.pack()

label_click = tk.Button(window, text ="Click here!!!", bg = "blue", command = tapUpdate)
label_click.pack()

quit_label = tk.Button(window, text = "Quit", bg = "red", command = window.destroy)
quit_label.pack()

window.mainloop()


