from tkinter import *

class App(Frame):
	def __init__(self, master):
		super().__init__(master)
		self.pack(padx=10, pady=10)
		self.button_clicks = 0
		self.create_widgets()

	def create_widgets(self):
		self.button = Button(self)
		self.button["text"] = "Click me!"
		self.button["command"] = self.update_count
		self.button.pack()
		self.label = Label(self)
		self.label["text"] = "Clicked me " + str(self.button_clicks) + " times."
		self.label.pack()
		Button(self, text="Quit", command=self.quit).pack()

	def update_count(self):
		self.button_clicks += 1
		self.label["text"] = "Clicked me " + str(self.button_clicks) + " times."

root = Tk()
root.title("Counter")
root.geometry("200x100")
app = App(root)
root.mainloop()
