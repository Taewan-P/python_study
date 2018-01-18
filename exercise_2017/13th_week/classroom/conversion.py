from tkinter import *

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=30, pady=20)
        self.create_widgets()
        
    def create_widgets(self):
        Label(self, text="섭씨").grid(row=0, column=0)
        Label(self, text="화씨").grid(row=0, column=1)
        self.entry0 = Entry(self, width=10, justify=CENTER)
        self.entry0.grid(row=1, column=0)
        self.entry1 = Entry(self, width=10, justify=CENTER)
        self.entry1.grid(row=1, column=1)
        Button(self, text="변환", command=self.c2f).grid(row=2, column=0)
        Button(self, text="변환", command=self.f2c).grid(row=2, column=1)
        Button(self, text="지우기", command=self.clear).grid(row=3, column=0, columnspan=2)
        Button(self, text="종료", command=self.quit).grid(row=4, column=0, columnspan=2)

    def c2f(self):
        entry = self.entry0.get()
        if entry != '' and Reader.isint(entry):
            t = round(9.0 / 5.0 * int(entry) + 32)
            self.entry1.delete(0, END)
            self.entry1.insert(0, str(t))
            #self.entry1.grid(row=1,column=1)

    def f2c(self):
        entry = self.entry1.get()
        if entry != '' and Reader.isint(entry):
            t = round((5 * int(entry) - 160) / 9.0)
            self.entry0.delete(0, END)
            self.entry0.insert(0, str(t))
            #self.entry0.grid(row=1,column=0)
            
    def clear(self):
        self.entry0.delete(0, END)
        self.entry1.delete(0, END)
        
class Reader:
    @staticmethod
    def isint(s):
        return s.isdigit() or \
               s[0] == '-' and s[1:].isdigit() or \
               s[0] == '+' and s[1:].isdigit()
        
# main        
root = Tk()
root.title("변환기")
root.geometry("280x180")
App(root)
root.mainloop()
