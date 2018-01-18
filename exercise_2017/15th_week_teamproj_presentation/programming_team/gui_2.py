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

#시간을 재는데 사용하는 클래스
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
        hours = int(elap/3600)
        minutes = int(elap/60 -hours*60.0)
        seconds = int(elap - minutes*60.0 -hours*3600)
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

class App(Frame):
	"""
	처음에 난의도를 선택할 수 있게끔 해주는 창이다.
	"""
	def __init__(self,master):
		super().__init__(master)
		self.pack(padx = 50, pady = 30)
		self.create_widgets()

	def create_widgets(self):
		Label(self, text="Welcome to 數獨(수독)!!",font=("Helvetica",60), justify=CENTER).grid(row = 0, column = 0)
		Label(self, text="Please select level.", font=("Helvetica",30), justify=CENTER).grid(row = 1, column = 0)
		Button(self, text="Hard", fg = 'red', command=self.hard_select, width = 10, height = 5, justify=CENTER).grid(row = 2, column = 0)
		Button(self, text="Normal", fg = 'orange', command=self.normal_select, width = 10, height = 5, justify=CENTER).grid(row = 3, column = 0)
		Button(self, text="Easy", fg = 'green', command=self.easy_select, width = 10, height = 5, justify=CENTER).grid(row = 4, column=0)
		Button(self, text="Quit", command=self.quit, justify = CENTER).grid(row = 5, column = 5, columnspan = 1)

	def hard_select(self):
		#no_of_holes 의 값이 40이게끔 보드를 형성한다.
		self.destroy()
		App.newTk_h()
		self.quit()

	def normal_select(self):
		#no_of_holes 의 값이 34이게끔 보드를 형성한다.
		self.destroy()
		App.newTk_n()
		self.quit()

	def easy_select(self):
		#no_of_holes 의 값이 28이게끔 보드를 형성한다.
		self.destroy()
		App.newTk_e()
		self.quit()

	
	def newTk_h():
		#하드모드의 새창을 만들어 준다.
		hard = Tk()
		hard.title("Hard모드 스도쿠")
		# hard.geometry("400x600")
		App_H(hard)
		hard.mainloop()

	def newTk_n():
		#노말모드의 새창을 만들어 준다.
		normal = Tk()
		normal.title("Normal모드 스도쿠")
		# normal.geometry("400x600")
		App_N(normal)
		normal.mainloop()
	
	def newTk_e():
		#이지모드의 새창을 만들어 준다.
		easy = Tk()
		easy.title("Easy모드 스도쿠")
		# easy.geometry("400x600")
		App_E(easy)
		easy.mainloop()


class App_H(Frame):
	"""
	스도쿠 난의도를 하드 모드로 선택했을때 실행되는 창이다.
	하드 모드는 빈칸의 갯수를 40개로 설정하였다.
	"""
	def __init__(self,master):
		super().__init__(master)
		self.pack(padx = 20, pady = 20)
		self.h = Board()
		self.create_widgets()
		
		#hsb = hard solution board
		hsb=self.h.create_solution_board()
		
		#hqb = hard question board
		hqb=self.h.copy_board(hsb)
		
		#hqbf = hard question board final
		hqbf=self.h.make_holes(hqb,40)

		self.show_board(hqbf)


	def create_widgets(self):

		Button(self, text = 'Quit', command = self.quit, justify = CENTER).grid(row = 9, column = 10, columnspan = 1)

	
	def show_board(self, board):
		copyboard=board[:]
		self.entries = {}
		
		counter = 0		
		for row in range(9):
			for column in range(9):
				if copyboard[row][column]==0:
					self.entries[counter] = Entry(self, width=2)
					self.entries[counter].grid(row=row, column=column)
				else:
					x=StringVar()
					self.entries[counter]=Entry(self, textvariable=x, width=2)
					x.set(str(copyboard[row][column]))
					self.entries[counter].config(state='readonly')
					self.entries[counter].grid(row=row, column=column)

				counter += 1











class App_N(Frame):
	"""
	스도쿠 난의도를 노말 모드로 선택했을때 실행되는 창이다.
	노말 모드는 빈칸의 갯수를 34개로 설정하였다.
	"""
	def __init__(self,master):
		super().__init__(master)
		self.pack(padx = 20, pady = 20)
		self.n = Board()
		self.create_widgets()

		#nsb = normal solution board
		nsb=self.n.create_solution_board()
		
		#nqb = normal question board
		nqb=self.n.copy_board(nsb)
		
		#nqbf = normal question board final
		nqbf=self.n.make_holes(nqb,34)

		self.show_board(nqbf)

	
	def create_widgets(self):

		Button(self, text = 'Quit', command = self.quit, justify = CENTER).grid(row = 9, column = 10, columnspan = 1)

	def show_board(self, board):
		copyboard=board[:]
		self.entries = {}
		
		counter = 0		
		for row in range(9):
			for column in range(9):
				if copyboard[row][column]==0:
					self.entries[counter] = Entry(self, width=2)
					self.entries[counter].grid(row=row, column=column)
				else:
					x=StringVar()
					self.entries[counter]=Entry(self, textvariable=x, width=2)
					x.set(str(copyboard[row][column]))
					self.entries[counter].config(state='readonly')
					self.entries[counter].grid(row=row, column=column)

				counter += 1










class App_E(Frame):
	"""
	스도쿠 난의도를 이지 모드로 선택했을때 실행되는 창이다.
	이지 모드는 빈칸의 갯수를 28개로 설정하였다.
	"""
	def __init__(self,master):
		super().__init__(master)
		self.pack(padx = 20, pady = 20)
		self.e = Board()
		self.create_widgets()

		#esb = easy solution board
		esb=self.e.create_solution_board()
		
		#eqb = easy question board
		eqb=self.e.copy_board(esb)
		
		#eqbf = easy question board final
		eqbf=self.e.make_holes(eqb,40)
		

		self.show_board(eqbf)

	def create_widgets(self):

		Button(self, text = 'Quit', command = self.quit, justify = CENTER).grid(row = 9, column = 10, columnspan = 1)


	def show_board(self, board):
		copyboard=board[:]
		self.entries = {}
		
		counter = 0		
		for row in range(9):
			for column in range(9):
				if copyboard[row][column]==0:
					self.entries[counter] = Entry(self, width=2)
					self.entries[counter].grid(row=row, column=column)
				else:
					x=StringVar()
					self.entries[counter]=Entry(self, textvariable=x, width=2)
					x.set(str(copyboard[row][column]))
					self.entries[counter].config(state='readonly')
					self.entries[counter].grid(row=row, column=column)

				counter += 1












#레벨 선택창 실
first = Tk()
first.title("수_Doh_구_월-드")
App(first)
first.mainloop()