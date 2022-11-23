import tkinter as tk

screen = tk.Tk()
screen.title("Calculator")
screen.configure(bg="light green")
screen.minsize(width=140, height=250)

expression = ""



entry_bar = tk.Entry(screen, width=25,borderwidth=3)
entry_bar.grid(row=0, column=0 ,columnspan=4,pady=1,padx=1)


def delete():
    value = entry_bar.get()
    entry_bar.delete(first=len(value) - 1, last="end")

def equals_to():
    if entry_bar.get() == "":
        pass
    elif entry_bar.get()[0] == "0":
        entry_bar.delete(0,"end")
    else:
        c_res = entry_bar.get()
        c_res = eval(c_res)
        clear()
        entry_bar.insert("end",c_res)

def clear():
    entry_bar.delete(0,"end")

#def tobetsa(num):

delete_button = tk.Button(screen, text="Del", fg="black", bg="pink", height=1, width=1, command=delete , pady=10,padx=15)
delete_button.grid(row=5, column=0)



button1 = tk.Button(screen, text="1", fg="black", bg="light blue" , height=1, width=1, command=lambda : entry_bar.insert("end","1"),pady=10,padx=15)
button1.grid(row=1, column=0)

button2 = tk.Button(screen, text="2", fg="black", bg="light blue", height=1, width=1,command=lambda : entry_bar.insert("end","2") ,pady=10, padx=15)
button2.grid(row=1, column=1,columnspan=1, pady=1, padx=0.1)

button3 = tk.Button(screen, text="3", fg="black", bg="light blue", height=1, width=1, command=lambda : entry_bar.insert("end","3"),pady=10, padx=15)
button3.grid(row=1, column=2)

button4 = tk.Button(screen, text="4", fg="black", bg="light blue", height=1, width=1, command=lambda : entry_bar.insert("end","4"),pady=10, padx=15)
button4.grid(row=2, column=0)

button5 = tk.Button(screen, text="5", fg="black", bg="light blue", height=1, width=1, command=lambda : entry_bar.insert("end","5"),pady=10, padx=15)
button5.grid(row=2, column=1)

button6 = tk.Button(screen, text="6", fg="black", bg="light blue", height=1, width=1,command=lambda : entry_bar.insert("end","6"), pady=10, padx=15)
button6.grid(row=2, column=2)

button7 = tk.Button(screen, text="7", fg="black", bg="light blue", height=1, width=1, command=lambda : entry_bar.insert("end","7"), pady=10, padx=15)
button7.grid(row=3, column=0)

button8 = tk.Button(screen, text="8", fg="black", bg="light blue", height=1, width=1,command=lambda : entry_bar.insert("end","8") ,pady=10, padx=15)
button8.grid(row=3, column=1)

button9 = tk.Button(screen, text="9", fg="black", bg="light blue", height=1, width=1,command=lambda : entry_bar.insert("end","9") ,pady=10, padx=15)
button9.grid(row=3, column=2)

button0 = tk.Button(screen, text="0", fg="black", bg="light blue", height=1, width=1,command=lambda : entry_bar.insert("end","0") ,pady=10, padx=15)
button0.grid(row=4, column=1)

button_plus = tk.Button(screen, text="+", fg="black", command=lambda : entry_bar.insert("end","+"),bg="pink", height=1, width=1,pady=10, padx=15)
button_plus.grid(row=1, column=3)

button_minus = tk.Button(screen, text="-", fg="black",command=lambda : entry_bar.insert("end","-"), bg="pink", height=1, width=1, pady=10, padx=15)
button_minus.grid(row=2, column=3)

button_multi = tk.Button(screen, text="x", fg="black", command=lambda : entry_bar.insert("end","x"),bg="pink", height=1, width=1, pady=10, padx=15)
button_multi.grid(row=3, column=3)

button_div = tk.Button(screen, text="/", fg="black", command=lambda : entry_bar.insert("end","/"),bg="pink", height=1, width=1, pady=10, padx=15)
button_div.grid(row=4, column=3)

button_cancel = tk.Button(screen, text="C", fg="black", bg="light blue", width=1,command=clear, height=1, pady=10, padx=15)
button_cancel.grid(row=4, column=0)

button_decimal = tk.Button(screen, text="0,0", fg="black",command=lambda : entry_bar.insert("end",","), bg="light blue", width=1, height=1, pady=10,padx=15)
button_decimal.grid(row=4, column=2)

button_equals = tk.Button(screen, text="=", fg="black",command=equals_to, bg="pink", width=1, height=1, pady=10, padx=15)
button_equals.grid(row=5, column=1)










screen.mainloop()
