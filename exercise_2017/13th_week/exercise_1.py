from tkinter import *

class Counter(Frame):
	def __init__(self,Frame):
		super().__init__(master)
		self.counter = 0
		self.pack(padx = 20, pady = 20)
		Label(self,bg = "yellow", fg="red", text = "Counter").pack()
		self.label = Label(self)
		Button(self, text = "Click ME!", command = self.update_counter).pack()
		self.label["text"] = "Clicked me " + str(self.counter) + "times."
		self.label.pack()

		Button(self, text = "Quit", command = self.quit).pack()


	def update_counter(self):
		self.counter += 1
		self.label["text"] = "Clicked me " + str(self.counter) + "times."



master = Tk()
Counter(master)

master.mainloop()
