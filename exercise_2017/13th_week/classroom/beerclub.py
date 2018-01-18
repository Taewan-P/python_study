from tkinter import *

class App(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=20, pady=20)
        self.create_widgets()
        
    def create_widgets(self):
        Label(self, text="Name").grid(row=0, column=0, sticky=E)
        self.name = Entry(self, width=10)
        self.name.grid(row=0, column=1)        
        Label(self, text="Email").grid(row=1, column=0, sticky=E)
        self.email = Entry(self, width=10)
        self.email.grid(row=1, column=1)
        Label(self, text="@smash.ac.kr").grid(row=1, column=2, sticky=W)        
        self.sex = StringVar()
        self.sex.set(None)
        Label(self, text="Sex").grid(row=2, column=0, sticky=E)
        Radiobutton(self, text='male',variable=self.sex, value='male').grid(row=2, column=1)
        Radiobutton(self, text='female',variable=self.sex, value='female').grid(row=2, column=2, sticky=W)       
        
        Label(self, text="Favorites").grid(row=3, column=1)
        self.lager = BooleanVar()    
        Checkbutton(self, text="Lager", variable=self.lager).grid(row=4, column=0)
        self.wheatbeer = BooleanVar()             
        Checkbutton(self, text="Wheat Beer", variable=self.wheatbeer).grid(row=4, column=1)
        self.pilsner = BooleanVar()
        Checkbutton(self, text="Pilsner", variable=self.pilsner).grid(row=4, column=2)
        self.paleale = BooleanVar()
        Checkbutton(self, text="Pale Ale", variable=self.paleale).grid(row=5, column=0)
        self.indiapaleale = BooleanVar()
        Checkbutton(self, text="India Pale Ale", variable=self.indiapaleale).grid(row=5, column=1)
        self.stout = BooleanVar()
        Checkbutton(self, text="Stout", variable=self.stout).grid(row=5, column=2)       
        
        Button(self, text="Register",command=self.write_summary).grid(row=6, column=0, columnspan=3, sticky=S)        
        self.summary = Text(self, width=48, height=10, wrap=WORD)
        self.summary.grid(row=7, column=0, columnspan=3, sticky=S)
        Button(self, text="Quit", command=self.quit).grid(row=8, column=0, columnspan=3)
        
    def write_summary(self):
        summary = "Name: " + self.name.get() + "\n"
        summary += "Email: " + self.email.get() + "@smash.ac.kr\n"
        summary += "Sex: " + self.sex.get() + "\n"
        summary += "Favorites are: "
        if self.lager.get():
            summary += "Lager, "
        if self.wheatbeer.get():
            summary += "Wheat Beer, "
        if self.pilsner.get():
            summary += "Pilsner, "
        if self.paleale.get():
            summary += "Pale Ale, "
        if self.indiapaleale.get():
            summary += "India Pale Ale, "
        if self.stout.get():
            summary += "Stout, "
        summary += "..."
        self.summary.delete(0.0, END)
        self.summary.insert(0.0, summary)
        
# main        
root = Tk()
root.title("SMaSH Beer Club")
root.geometry("400x420")
App(root)
root.mainloop()
