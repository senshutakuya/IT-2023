import webbrowser
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from new_test import BruteForce
from DOS import DOS_attack

class Function:
    @staticmethod
    def click_btn(btn, brute_force, dos_attack):
        btn['text'] = "クリック"
        if btn.fn == 'f1':
            brute_force.run_brute_force()
        elif btn.fn == 'f2':
            dos_attack.Da()

    @staticmethod
    def frame(x, row):
        frame1 = Frame(root, width=100, height=100, borderwidth=2, relief='solid')
        frame1.place(x=x, y=row*100, width=150, height=100)
        return frame1

    @staticmethod
    def create_button(fn, btn_fn, brute_force, dos_attack):
        button = Button(fn, text="ボタン", command=lambda: Function.click_btn(button, brute_force, dos_attack))
        button.fn = btn_fn
        button.pack(pady=10)


if __name__ == '__main__':
    root = tk.Tk()
    root.title("demo_Tkinter")
    root.geometry("400x400")

    url = "http://10.8.0.1/login/"
    url2 = "http://10.8.0.1/home/"
    cookie = {'PHPSESSID': 'il9q48alh73bfn8pq2uc37u3ml'}
    bf = BruteForce(url, url2, cookie)

    dos = DOS_attack()

    # フレームを作成して配置
    f1 = Function.frame(130, 0)
    f2 = Function.frame(130, 1.2)

    # ボタンを作成
    Function.create_button(f1, 'f1', bf, dos)
    Function.create_button(f2, 'f2', bf, dos)

    root.mainloop()
