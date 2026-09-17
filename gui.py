import os
import sys
import tkinter as tk
import warnings
from tkinter import messagebox

from fracbase2dex import fracbase2dex
from fracdex2base import fracdex2base
from fracbase2base import fracbase2base

def _resource_path(name):
    base = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
    bundled = os.path.join(base, name)
    if os.path.exists(bundled):
        return bundled
    return os.path.join(os.path.expanduser("~"), "Desktop", name)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("进制转换器")
        self.root.geometry("440x280")
        self.root.resizable(False, False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        self.show_menu()

    def on_close(self):
        if messagebox.askyesno("退出", "确定要退出吗？"):
            self.root.destroy()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def show_menu(self):
        self.clear()

        body = tk.Frame(self.root)
        body.pack(expand=True)

        self._mascot = self._load_mascot()
        if self._mascot is not None:
            tk.Label(body, image=self._mascot).pack(side="left", padx=18)

        btns = tk.Frame(body)
        btns.pack(side="left", padx=10)
        tk.Button(btns, text="base2dex", width=12,
                  command=lambda: self.show_convert("base2dex")).pack(pady=5)
        tk.Button(btns, text="dex2base", width=12,
                  command=lambda: self.show_convert("dex2base")).pack(pady=5)
        tk.Button(btns, text="base2base", width=12,
                  command=lambda: self.show_convert("base2base")).pack(pady=5)

        tk.Button(self.root, text="退出", width=12,
                  command=self.on_close).pack(side="bottom", pady=16)

    def _load_mascot(self):
        path = _resource_path("图片.png")
        try:
            return tk.PhotoImage(file=path).subsample(8)
        except tk.TclError:
            return None

    def show_convert(self, kind):
        self.clear()
        if kind == "base2dex":
            fields = [("数值", "value"), ("进制", "base")]
        elif kind == "dex2base":
            fields = [("十进制数", "value"), ("目标进制", "base")]
        else:
            fields = [("数值", "value"), ("原进制", "fromBase"), ("目标进制", "toBase")]

        panel = tk.Frame(self.root)
        panel.place(relx=0.5, rely=0.5, anchor="center")

        self.entries = {}
        for i, (label, key) in enumerate(fields):
            tk.Label(panel, text=label).grid(row=i, column=0, padx=10, pady=6, sticky="e")
            e = tk.Entry(panel, width=20)
            e.grid(row=i, column=1, padx=10, pady=6)
            self.entries[key] = e

        btns = tk.Frame(panel)
        btns.grid(row=len(fields), column=0, columnspan=2, pady=10)
        tk.Button(btns, text="确认", width=10,
                  command=lambda: self.on_confirm(kind)).pack(side="left", padx=8)
        tk.Button(btns, text="返回", width=10, command=self.show_menu).pack(side="left", padx=8)

        tk.Label(panel, text="结果").grid(row=len(fields) + 1, column=0, sticky="e")
        self.result = tk.Entry(panel, width=20, state="readonly")
        self.result.grid(row=len(fields) + 1, column=1, pady=6)

        self.status = tk.Label(panel, text="", fg="red", wraplength=380)
        self.status.grid(row=len(fields) + 2, column=0, columnspan=2, pady=4)

    def _set_result(self, text):
        self.result.config(state="normal")
        self.result.delete(0, "end")
        self.result.insert(0, text)
        self.result.config(state="readonly")

    def on_confirm(self, kind):
        self.status.config(text="")
        caught = []
        try:
            value = self.entries["value"].get()
            if kind == "base2dex":
                base = int(self.entries["base"].get())
                out = fracbase2dex(value, base)
            elif kind == "dex2base":
                base = int(self.entries["base"].get())
                with warnings.catch_warnings(record=True) as caught:
                    warnings.simplefilter("always")
                    out = fracdex2base(float(value), base)
            else:
                fromBase = int(self.entries["fromBase"].get())
                toBase = int(self.entries["toBase"].get())
                out = fracbase2base(value, fromBase, toBase)
        except ValueError as e:
            self._set_result(str(e))
            return

        self._set_result(str(out))
        if caught:
            self.status.config(text="小数部分已截断到 10 位")


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
