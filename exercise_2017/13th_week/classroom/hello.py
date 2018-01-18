from tkinter import *

class App(Frame):
	def __init__(self, window):
		super().__init__(window)
		self.pack(padx=20, pady=20)
		Label(self, text="Hello, world!", bg="yellow", fg="red").pack()
		Button(self, text="Quit", command=self.quit).pack()

window = Tk()
window.title("Hello")
window.geometry("200x100")
App(window)
window.mainloop()



		# self.pack(padx=20, pady=20, fill=X)
		# h = Label(self, text="Hello, world!")
		# h['bg'] = "yellow"
		# h['fg'] = "red"
		# h.pack(fill=X)
		#