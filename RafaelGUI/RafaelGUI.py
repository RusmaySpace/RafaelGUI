from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

clicks = 0

def satanaa():
    satana = PhotoImage(file="oh.png")
    label = ttk.Label(image=satana)
    label.pack(anchor=CENTER, ipady = 150)
    panel = Label(satanaa, image=satana)
    panel.pack(side="bottom", fill="both", expand="no")
    button = Button(satanaa, text='открыть окно', font='Times 12', command=satanaa)
    button.place(x=0, y=0)

def iff():
    if clicks >= 70:
        btn4["text"] = f"СЮДААА!!!!!!!!!!!!!!!!!! (x{clicks})"
    elif clicks >= 100:
        btn4["text"] = f"C:< (x{clicks})"
    elif clicks >= 300:
        btn4["text"] = f"C:<<<<< (x{clicks})"
    elif clicks == 666:
        btn4["text"] = f"ЧТО ТЫ НАДЕЛАЛ? (x{clicks})"
        satanaa()
    elif clicks >= 667:
        btn4["text"] = f"<: (x{clicks})"
    elif clicks >= 1000:
        btn4["text"] = f"0_0 (x{clicks})"
    elif clicks >= 1500:
        btn4["text"] = f"X_X (x{clicks})"
    else:
        btn4["text"] = f"ЕЩЁ (x{clicks})"

def click_button():
    global clicks
    clicks += 1
    if clicks <= 10:
        btn4["text"] = f"ЕЩЁ! (x{clicks})"
    elif clicks >= 10 and clicks < 20:
        btn4["text"] = f"ЕЩЁ!!! (x{clicks})"
    elif clicks >= 20 and clicks < 30:
        btn4["text"] = f"ЕЩЁ!!!!!! (x{clicks})"
    elif clicks >= 30 and clicks <= 69:
        btn4["text"] = f"СЮДААА!! (x{clicks})"
    else:
        iff()

def open_error(): 
    showerror(title="Отказано в доступе", message="Ты не можешь так со мной поступить.")

root = Tk()
root.title("Рафаэль")
icon = PhotoImage(file = "document.png")
root.iconphoto(False, icon)
root.geometry("700x500")

label = Label(text="Я вернулся с улучшениями :)\n \nЧто сделаешь со мной?\n")
label.pack()

btn1 = ttk.Button(text="Послать", cursor="X_cursor", command=open_error)
btn1.pack(side=BOTTOM)

btn2 = ttk.Button(text="Пнуть", cursor="X_cursor", command=open_error)
btn2.pack(side=RIGHT)
 
btn3 = ttk.Button(text="Убить", cursor="X_cursor", command=open_error)
btn3.pack(side=LEFT)
 
btn4 = ttk.Button(text="Погладить", command=click_button)
btn4.pack(side=TOP)

root.mainloop()