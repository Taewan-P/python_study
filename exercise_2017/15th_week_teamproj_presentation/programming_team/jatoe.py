# 수독 9x9
import random,time,pygame
from tkinter import *
from tkinter import messagebox

#Model

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
		"""우하향 대각선을 기준으로 히오스"""
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

class App(Frame):
	def __init__(self):
		self.level_button()

	def level_button(self):
		Label(self, text='Level:').grid(row=1, column=0, sticky=W)
		self.level=StringVar()
		self.level.set(None)
		Radiobutton(self, text='Hard', variable=self.level, value='hard').grid(row=1, column=1)
		Radiobutton(self, text='Normal', variable=self.level, value='normal').grid(row=1, column=2)
		Radiobutton(self, text='Easy', variable=self.level, value='easy').grid(row=1, column=3)

		sw = StopWatch()
		sw.pack(side = TOP)
		Button(self, text='GO', command= sw.Start).grid(row=1, column=4)

		
	def gui_board(self, root, board):
		a, b=1, 0
		for i in range(9):
			for j in range(9):
				if board[i][j]== 0:
					self.entry=Entry(self, text='')
					self.entry.grid(row=a, column=b)
				# else:
				# 	Label(self, text=str(board[i][j])).grid(row=a, column=b, outline='#fffffffff')
				b+=1
			a+=1
		        # create the drawing canvas
		# sq = 50
		# numsq = 9
		# thickevery = 3
		# normal = 1
		# wide = 3
		# canvas = Canvas(root, width=numsq*sq, height=9*sq, bg='white')
		# canvas.pack()

		# # draw horizontal lines
		# x1 = 0
		# x2 = 9*sq
		# for k in range(0, sq*(numsq+1), sq):
		# 	y1 = k
		# 	y2 = k
		# 	if k % thickevery: w = normal
		# 	else: w = wide
		# 	canvas.create_line(x1, y1, x2, y2, width=w)

		# # draw vertical lines
		# y1 = 0
		# y2 = 9*sq
		# for k in range(0, sq*(numsq+1), sq):
		# 	x1 = k
		# 	x2 = k
		# 	if k % thickevery: w = normal
		# 	else: w = wide
		# 	canvas.create_line(x1, y1, x2, y2, width=w)

	# def stopWatch(self):
	# 	a = 0
	# 	self.hours = 0
	# 	while a < 1:
	# 		for self.minutes in range(0, 60):
	# 			for self.seconds in range(0, 60):
	# 				# self.time_label=Label(self)
	# 				# self.time_label["text"]=str(hours)+":"+str(minutes)+":"+str(seconds)
	# 				# self.time_label.grid(row=1, column=1)
	# 				time.sleep(1)

	# 				# messagebox.showinfo("Timer", str(hours)+":"+str(minutes)+":"+str(seconds))
	# 				# print(hours,":", minutes,":", seconds)
	# 	self.hours += 1
	# 	# return (hours, minutes, seconds)

	def comepletebox(self):
		messagebox.showinfo("Comepleted!", "어-썸\n"+ "Adiós\n"+ "It took "+"hours"+" minutes"+\
							" seconds for you to solve this sudoku.\n"+\
							"Developer: team.Hoecoda\n"+"Park, Lee, Hoe\n"+ "Assist: Prof.Pooh(Doh)")


#View

class Hogaeng:
	@staticmethod
	def get_level(self, level):
		"""빈칸의 갯수로 난이도를 설정"""
		if level.get() == 'hard':
			a = 40
			return a
		elif level.get() == 'normal':
			a = 34
			return a
		elif level.get()=='esay':
			a = 28
			return a

	@staticmethod
	def show_board(board):
		"""modify for gui programming"""
		print()
		print('S', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9')
		print('-', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-')
		i = 1
		for row in board:
			print(i, end=' ')
			print('|', end=' ')
			for entry in row:
				if entry == 0:
					print(' ', end=' ')
				else:
					print(entry, end=' ')
			print()
			i += 1
		print()

	@staticmethod
	def get_integer(message, i, j): 
		"""입력받은 값이 정수인지 확인하는 함수"""
		number = input(message)
		while not (number.isdigit() and i <= int(number) <= j):
			number = input(message)
		return int(number)


#Controllor
class SudokControllor(Frame):
	def __init__(self, master):
		"""set a initial attribute"""
		super().__init__(master)
		self.pack(padx=10, pady=20)

		self.sudok=Board()  # object
		self.solution = self.sudok.create_solution_board()
		# level=App.level_button(self)
		self.no_of_holes = App.level_button(self)
		self.puzzle = self.sudok.copy_board(self.solution)
		# (self.puzzle, self.holeset) = self.sudok.make_holes(self.puzzle, self.no_of_holes)

		# App.level_button()
		App.gui_board(self, window, self.solution)
		App.comepletebox(self)


	def play(self):
		"""play sudok game"""
		Hogaeng.show_board(self.puzzle)
		while self.no_of_holes > 0:
			i = Hogaeng.get_integer("row number(1~9): ", 1, 9) - 1
			j = Hogaeng.get_integer("column number(1~9): ", 1, 9) - 1
			if (i, j) not in self.holeset:
				print("It already has a number.")
				continue
			n = Hogaeng.get_integer("number(1~9): ", 1, 9)
			sol = self.solution[i][j]
			if n == int(sol):
				self.puzzle[i][j] = sol
				Hogaeng.show_board(self.puzzle)
				self.holeset.remove((i, j))
				self.no_of_holes -= 1
			else:
				print(n, "is a wrong number. HAHAHAHA! Try again.")
		print("Good job. Never come back!")


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
    
    def _update(self): 
        """ Update the label with elapsed time. """
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)
    
    def _setTime(self, elap):
        """ Set the time string to Minutes:Seconds:Hundreths """
        minutes = int(elap/60)
        seconds = int(elap - minutes*60.0)
        hseconds = int((elap - minutes*60.0 - seconds)*100)                
        self.timestr.set('%02d:%02d:%02d' % (minutes, seconds, hseconds))
        
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


#########여기서 해야될것#########
#GO 버튼을 눌렀을때 Stopwatch Class 에 Start 함수가 구동되게끔 한다.
#If 정답 처리가 됬을때 이것이 Stopwatch Class에 Stop 함수가 구동되게끔 한다.






window=Tk()
window.title("Jatoe")
window.geometry()
SudokControllor(window)
window.mainloop()