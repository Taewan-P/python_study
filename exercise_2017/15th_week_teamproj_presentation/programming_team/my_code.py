import random,time
from tkinter import *
from tkinter import messagebox

class Board:
	@staticmethod
	def create_board():
		"""create initial board"""
		seed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		random.shuffle(seed)
		n1 = seed[0]
		n2 = seed[1]
		n3 = seed[2]
		n4 = seed[3]
		n5 = seed[4]
		n6 = seed[5]
		n7 = seed[6]
		n8 = seed[7]
		n9 = seed[8]
		return [[n1, n2, n3, n4, n5, n6, n7, n8, n9],
				[n4, n5, n6, n7, n8, n9, n1, n2, n3],
				[n7, n8, n9, n1, n2, n3, n4, n5, n6],
				[n2, n3, n1, n5, n6, n4, n8, n9, n7],
				[n5, n6, n4, n8, n9, n7, n2, n3, n1],
				[n8, n9, n7, n2, n3, n1, n5, n6, n4],
				[n3, n1, n2, n6, n4, n5, n9, n7, n8],
				[n6, n4, n5, n9, n7, n8, n3, n1, n2],
				[n9, n7, n8, n3, n1, n2, n6, n4, n5]]

	def shuffle_ribbons(self, board):
		"""한줄씩 가로로 세칸을 서로 섞기"""
		self.sboard=board
		top = self.sboard[:3]
		middle = self.sboard[3:6]
		bottom = self.sboard[6:]
		random.shuffle(top)
		random.shuffle(middle)
		random.shuffle(bottom)
		self.sboard=top+middle+bottom
		return self.sboard

	def transpose(self, board):
		"""우하향 대각선을 기준으로 회전"""
		self.tboard=board
		self.transposed = []
		for _ in range(len(self.tboard)):
		    self.transposed.append([])
		for row in self.tboard:
		    i = 0
		    for entry in row:
		        self.transposed[i].append(entry)
		        i += 1
		return self.transposed

	def create_solution_board(self):
		"""스독을 만드는 방법으로 만들기"""
		self.board = Board.create_board()
		Board.shuffle_ribbons(self, self.board)
		Board.transpose(self, self.sboard)
		Board.shuffle_ribbons(self, self.tboard)
		Board.transpose(self, self.sboard)
		self.board=self.tboard
		return self.board

	def copy_board(self, board):
		"""게임을 진행할 보드를 복제하기"""
		board_clone = []
		for row in board :
		    row_clone = row[:]
		    board_clone.append(row_clone)
		return board_clone

	def make_holes(self, board, no_of_holes):
		"""make a holes by level"""
		hboard=board
		holeset = set()
		while no_of_holes > 0:
			i = random.randint(0, 8)
			j = random.randint(0, 8)
			if hboard[i][j] != 0:
				hboard[i][j] = 0
				holeset.add((i, j))
				no_of_holes -= 1 
		return (hboard, holeset)

class StopWatch(Frame):  
    """ Implements a stopwatch frame widget. """                                                                
    def __init__(self, parent=None, **kw):        
        Frame.__init__(self, parent, kw)
        self._start = 0.0        
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()               
        self.makeWidgets()      

    def makeWidgets(self):                         
        """ Make the time label. """
        l = Label(self, textvariable=self.timestr)
        self._setTime(self._elapsedtime)
        l.pack(fill=X, expand=NO, pady=2, padx=2)
        # l.grid(row=4, column=12)
    
    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        hours = int(elap/3600)
        minutes = int(elap/60-hours*60.0)
        seconds = int(elap - minutes*60.0 - hours*3600)
        # hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (hours, minutes, seconds))
        
    def Start(self):                                                     
        """ Start the stopwatch, ignore if running. """
        if not self._running:            
            self._start = time.time() - self._elapsedtime
            self._update()
            self._running = 1        
    
    def Stop(self):                                    
        """ Stop the stopwatch, ignore if stopped. """
        if self._running:
            self.after_cancel(self._timer)            
            self._elapsedtime = time.time() - self._start    
            self._setTime(self._elapsedtime)
            self._running = 0
    
    def Reset(self):                                  
        """ Reset the stopwatch. """
        self._start = time.time()         
        self._elapsedtime = 0.0    
        self._setTime(self._elapsedtime)

class Hogaeng:
	def __init__(self):
		# self.level_button()
		# self.grid()
		self.sw = StopWatch()
		self.sw.pack(side = TOP)
		self.show_board()
		self.create_sudoku_widgets()
		self.combine_funcs()

		# self.completebox()

	def create_sudoku_widgets(self):
		self.level = IntVar()
		self.level.set(0)
		Label(self, text='Select Level').grid(row=0, column= 12, sticky=W)
		Radiobutton(self, text='Hard', variable=self.level, value=40).grid(row=1, column=12, sticky=W)
		Radiobutton(self, text='Normal', variable=self.level, value=34).grid(row=2, column=12, sticky=W)
		Radiobutton(self, text='Easy', variable=self.level, value=28).grid(row=3, column=12, sticky=W)
		#lambda x:func1() & func2()
		Button(self, text='GO', command=Hogaeng.combine_funcs).grid(row=2, column=13, columnspan=3)
		Button(self, text="Quit", command=self.quit).grid(row=3, column=13,columnspan=3)

	def combine_funcs():
		sw.Start
		self.submit_level
		Board.make_holes()

	def submit_level(self):
		# self.level ->no_of_holes 로 가게끔
		Hogaeng.create_sudoku_widgets(self)
		get=self.level.get()
		return get

	#completebox 는 일딴 나중에 만든다.
	#getlevel 는 만들 필요가 없다.
		
	def show_board(self, root, board):
		copyboard=board[:]

		self.entries = {}
		# self.tableheight = 9
		# self.tablewidth = 9
		grey='#dddddd'
		white='#ffffff'
		counter = 0
		for row in range(9):
			for column in range(9):
				if copyboard[row][column]==0:
					if row==column:
						self.entries[counter] = Entry(self, width=2, bg=grey)
						self.entries[counter].grid(row=row, column=column)
					else:
						self.entries[counter] = Entry(self, width=2, bg=white)
						self.entries[counter].grid(row=row, column=column)
				else:
					if row==column:
						x=StringVar()
						self.entries[counter]=Entry(self, bg=grey, textvariable=x, width=2)
						x.set(str(copyboard[row][column]))
						self.entries[counter].config(state='readonly')
						self.entries[counter].grid(row=row, column=column)
					else:
						x=StringVar()
						self.entries[counter]=Entry(self, bg=white, textvariable=x, width=2)
						x.set(str(copyboard[row][column]))
						self.entries[counter].config(state='readonly')
						self.entries[counter].grid(row=row, column=column)
				counter += 1

	# def sub(self):
	# 	self.board = self.bt.get()
	# 	self.solbd = self.st.get()
	# 	if  self.board == self.solbd :
	# 		self.completebox() #성공창 소환
	# 	else:
	# 		messagebox.showinfo("Wrong Answer","Oh! It's Worng.HAAHAHAHAHA Try Again")

	@staticmethod
	def completebox():
		#몇분 몇초 걸렸는지 값을 저장하는 변수를 만들어서 적용시켜 줘야됨.
		messagebox.showinfo("Complete!!", "어-썸\n"+ "Adiós\n"+ "It took "+"hours"+" minutes"+\
							" seconds for you to solve this sudoku.\n"+\
							"Developer: team.Hoecoda\n"+"Park, Lee, Hoe\n"+ "Assist: Prof.Pooh(Doh)")

	@staticmethod
	def get_integer(message, i, j): 
		"""입력받은 값이 정수인지 확인하는 함수"""
		number = input(message)
		while not (number.isdigit() and i <= int(number) <= j):
			number = input(message)
		return int(number)


class SudokControllor(Frame):
	def __init__(self, master):
		"""set a initial attribute"""
		super().__init__(master)
		self.pack(padx=10, pady=20)

		self.sudok=Board()  # object
		self.solution = self.sudok.create_solution_board()
		self.no_of_holes = Hogaeng.submit_level(self)

		# print(self.no_of_holes)
		self.puzzle = self.sudok.copy_board(self.solution)
		(self.puzzle, self.holeset) = self.sudok.make_holes(self.puzzle, self.no_of_holes)
		Hogaeng.show_board(self, window, self.puzzle)


	def play(self):
		"""play sudok game"""
		# print(self.puzzle)

		Hogaeng.show_board(self, window, self.puzzle)


		while self.no_of_holes > 0:
			i = Hogaeng.get_integer("as",1, 9) - 1
			j = Hogaeng.get_integer("as",1, 9) - 1
			if (i, j) not in self.holeset:
				messagebox.showinfo("alarm","It already has a number.")
				continue
			n = Hogaeng.get_integer("number(1~9): ", 1, 9)
			sol = self.solution[i][j]
			if n == int(sol):
				self.puzzle[i][j] = sol
				# Hogaeng.show_board(self.puzzle)
				self.holeset.remove((i, j))
				self.no_of_holes -= 1
			else:
				messagebox.showinfo("alarm", str(n)+"is a wrong number. HAHAHAHA! Try again.")
		# Hogaeng.completebox()






window=Tk()
window.title("Jatoe")
window.geometry()
SudokControllor(window).play()
window.mainloop()