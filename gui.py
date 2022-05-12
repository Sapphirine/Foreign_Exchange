import tkinter as tk
import tkinter.filedialog
from tkinter import ttk
from PIL import Image, ImageTk
import time


def create():
    top = tk.Toplevel()
    top.title('Prediction Result')
    top.geometry('900x700')
    tk.Label(top, text='Prediction Figure', font=('Times', 20, 'italic')).pack()

    img = Image.open('./img.png')
    photo = ImageTk.PhotoImage(img)
    render = tk.Label(top, image=photo)
    render.image = photo
    render.place(x=50, y=25)

    tk.Label(top, text='Prediction Data', font=('Times', 20, 'italic')).place(x=400, y=350)

    tree = ttk.Treeview(top, columns=['1', '2'], show='headings')
    tree.place(x=100, y=400)
    tree.column('1', width=300, anchor='center')
    tree.column('2', width=300, anchor='center')

    tree.heading('1', text='Date')
    tree.heading('2', text='Exchange Rate')

    data = [['2020-12-30', '0.7143'], ['2020-12-31', '0.7181'], ['2021-01-04', '0.7236'], ['2021-01-05', '0.7307'], ['2021-01-06', '0.7374'], ['2021-01-07', '0.7400'], ['2021-01-08', '0.7386']]
    for i in data:
        tree.insert('', 'end', values=i)



def uploadCSVCallBack():
    filename = tkinter.filedialog.askopenfilename(title='Please choose a CSV file',
                                                  filetypes=[('csv', '*.csv'), ('All Files', '*')],
                                                  initialdir='/Users/wangzhaomeng')
    if filename == '':
        print("error: No file!")
    else:
        print("filename" + filename)
        time.sleep(2.4)
        create()


if __name__ == "__main__":
    window = tk.Tk()
    window.title('Exchange Rate AI Predict System')
    window.geometry('600x400')
    tk.Label(window, text=' ', font=('Times', 25, 'bold italic')).pack()

    tk.Label(window, text='Welcome to the Exchange Rate AI Predict System!', font=('Times', 25, 'bold italic')).pack()
    tk.Label(window, text='EECSE 6895   Advanced Big Data & AI ', font=('Times', 20, 'italic')).pack()
    tk.Label(window, text='Developed by: Zhaomeng Wang & Hanlun Wang', font=('Times', 18, 'italic underline')).pack()

    tk.Label(window, text=' ', font=('Times', 20, 'bold italic')).pack()

    group = tk.LabelFrame(window, text="Please choose the exchange currency", padx=15, pady=15)
    group.pack(padx=10, pady=10)

    types = [
        ("AD to USD", 1),
        ("AD to CNY", 2),
        ("AD to EUR", 3),
        ("AD to GBP", 4)]

    v = tk.IntVar()

    for lang, num in types:
        b = tk.Radiobutton(group, text=lang, variable=v, value=num)
        b.pack(anchor=tk.W)

    start_btn = tk.Button(window, text="Click Here to Upload Data", fg="red", font=('Times', 20, 'italic'), command=uploadCSVCallBack)

    start_btn.pack()

    window.mainloop()
