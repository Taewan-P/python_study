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
        Button(self, text="지우기", command=self.clear_temp).grid(row=1, column=2, columnspan=2)
        

        Label(self, text="센티미터").grid(row=3, column=0)
        Label(self, text="피트").grid(row=3, column=1)
        self.entry2 = Entry(self, width=10, justify=CENTER)
        self.entry2.grid(row=4, column=0)
        self.entry3 = Entry(self, width=10, justify=CENTER)
        self.entry3.grid(row=4, column=1)
        Button(self, text="변환", command=self.cm2ft).grid(row=5, column=0)
        Button(self, text="변환", command=self.ft2cm).grid(row=5, column=1)
        Button(self, text="지우기", command=self.clear_length).grid(row=4, column=2, columnspan=2)


        Label(self, text="킬로그램").grid(row=6, column=0)
        Label(self, text="파운드").grid(row=6, column=1)
        self.entry4 = Entry(self, width=10, justify=CENTER)
        self.entry4.grid(row=7,column=0)
        self.entry5 = Entry(self, width=10, justify=CENTER)
        self.entry5.grid(row=7,column=1)
        Button(self, text="변환", command=self.kg2lb).grid(row=8, column=0)
        Button(self, text="변환", command=self.lb2kg).grid(row=8, column=1)
        Button(self, text="지우기", command=self.clear_weight).grid(row=7, column=2, columnspan=2)


        Button(self, text="종료", command=self.quit).grid(row=9, column=2, columnspan=2)

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

    def cm2ft(self):
        entry = self.entry2.get()
        if entry != '' and Reader.isint(entry):
            a = round(0.03281*int(entry),1)
            self.entry3.delete(0, END)
            self.entry3.insert(0, str(a))

    def ft2cm(self):
        entry = self.entry3.get()
        if entry != '' and Reader.isint(entry):
            a = round(30.48*int(entry),1)
            self.entry2.delete(0, END)
            self.entry2.insert(0, str(a))

    def kg2lb(self):
        entry = self.entry4.get()
        if entry != '' and Reader.isint(entry):
            a = round(2.2046*int(entry),1)
            self.entry5.delete(0, END)
            self.entry5.insert(0, str(a))

    def lb2kg(self):
        entry = self.entry5.get()
        if entry != '' and Reader.isint(entry):
            a = round(0.4536*int(entry),1)
            self.entry4.delete(0, END)
            self.entry4.insert(0, str(a))

 
    def clear_temp(self):
        self.entry0.delete(0, END)
        self.entry1.delete(0, END)

    def clear_length(self):
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)

    def clear_weight(self):
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)
        
class Reader:
    @staticmethod
    def isint(s):
        return s.isdigit() or \
                s[0] == '-' and s[1:].isdigit() or \
                s[0] == '+' and s[1:].isdigit()
        
# main        
root = Tk()
root.title("변환기")
App(root)
root.mainloop()