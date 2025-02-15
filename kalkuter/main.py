#autor Skiper
import tkinter as tk
def przycisk_click(symbol):
    obecny_tekst = wejscie.get()
    wejscie.delete(0, tk.END)
    wejscie.insert(0, obecny_tekst + symbol)

def oblicz():
    try:
        wynik = eval(wejscie.get())
        wejscie.delete(0, tk.END)
        wejscie.insert(0, str(wynik))
    except Exception as e:
        wejscie.delete(0, tk.END)
        wejscie.insert(0, "Bład!")

def clear():
    wejscie.delete(0, tk.END)


root = tk.Tk()
root.geometry("270x350")
root.title("Kalkuter")
root.iconbitmap("images/icon.ico")

wejscie = tk.Entry(root, width=20, font=('Arial', 18), justify="right")
wejscie.grid(row=0, column=0, columnspan=4)


buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for symbol, row, col in buttons:
    if symbol == '=':
        btn = tk.Button(root, text=symbol, width=5, height=2, font=('Arial', 14), command=oblicz)
    else:
        btn = tk.Button(root, text=symbol, width=5, height=2, font=('Arial', 14),
                        command=lambda s=symbol: przycisk_click(s))
    btn.grid(row=row, column=col)


btn_clear = tk.Button(root, text='C', width=5, height=2, font=('Arial', 14), command=clear)
btn_clear.grid(row=5, column=0, columnspan=4, sticky="we")

root.mainloop()
#autor Skiper