from tkinter import *


class App(Frame):
	"""docstring for App"""
	def __init__(self, master):
		super().__init__(master)
		#frame reset
		self.pack(padx=20,pady=20) #frame optimize//pixel
		Label(self, bg="yellow", fg="red", text = "hello world!").pack()
		Button(self, text="quit", command=self.quit).pack()


		









master = Tk() #마스터 변수/모든걸 저장해놓는 변수가 필요하다
master.title("hello")
# master.geometry("200x100")
# Label(master, text = "hello world!").pack() #pack method : 윈도우 사이즈에 맞게 매치시켜줌
#지오메트리 사용 안하면 알아서 윈도우 사이즈가 맞게 변형됨

App(master) #class 실행


master.mainloop() #반드시 불러줘야됨// 이벤트루프를 계속 돌려줘야됨 창이 가만히 있는것 처럼 보여도 계속 작업을 하고 있다.

