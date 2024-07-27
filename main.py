from currency_converter import CurrencyConverter
import tkinter as tk
a=CurrencyConverter()
window = tk.Tk()
window.geometry("500x360")

def clicked():
    amount = float(e1.get())  # Get the amount as a float
    curr1 = e2.get().upper()  # Source currency
    curr2 = e3.get().upper()  # Target currency
    data = a.convert(amount, curr1, curr2)
    rounded_data = round(data, 3)  # Round to 3 decimal places
    result_text = str(rounded_data) + " " + curr2  #format
    label_5.config(text=result_text)


label_1 = tk.Label(window, text="Currency Converter", font="Times 25 bold").place(x=100, y=30)

label_2 = tk.Label(window, text="enter amount here", font="Times 18 bold").place(x=50, y=80)
e1 = tk.Entry(window)

label_3 = tk.Label(window, text="enter currency", font="Times 18 bold").place(x=50, y=130)
e2 = tk.Entry(window)

label_4 = tk.Label(window, text="enter req currency", font="Times 18 bold").place(x=50, y=180)
e3 = tk.Entry(window)

b1=tk.Button(window,text="Convert",command=clicked).place(x=230, y=240)

label_5 = tk.Label(window, text="", font="Times 25 bold")   #label for result
label_5.place(x=200, y=290)

e1.place(x=300,y=90)
e2.place(x=300,y=140)
e3.place(x=300,y=190)

window.mainloop()

