# -*- coding : utf-8- -*-
#UTF-8 encoding when using korean
import random,time
from tkinter import *
from tkinter import messagebox

#Model
class Board:
	"""
	This class is the "Model" part of MVC architecture.
	"""
	@staticmethod
	def create_board():
		"""This function create initial sudoku board."""
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
		"""This function mixes every three rows randomly."""
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
		"""This funcion flips the board rightward diagonally."""
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
		"""This function creates solution board for Sudoku."""
		self.board = Board.create_board()
		Board.shuffle_ribbons(self, self.board)
		Board.transpose(self, self.sboard)
		Board.shuffle_ribbons(self, self.tboard)
		Board.transpose(self, self.sboard)
		self.board=self.tboard
		return self.board

	def copy_board(self, board):
		"""This function copies input board and returns copied board."""
		board_clone = []
		for row in board :
		    row_clone = row[:]
		    board_clone.append(row_clone)
		return board_clone

	def make_holes(self, board, no_of_holes):
		"""
		This function makes holes in input board.
		The number of holes differ by the level you choose.
		"""
		hboard=board
		holeset = set()
		while no_of_holes > 0:
			i = random.randint(0, 8)
			j = random.randint(0, 8)
			if hboard[i][j] != 0:
				hboard[i][j] = 0
				holeset.add((i, j))
				no_of_holes -= 1 
		return hboard

class StopWatch(Frame):  
	""" Implements a stop watch frame widget. """                                                                
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
		hours=int(elap/3600)
		minutes = int(elap/60-hours*60.0)
		seconds = int(elap - minutes*60.0-hours*3600)               
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



#View
class App(Frame):
	"""
	This class is a window that shows user to choose difficulty.
	"""
	def __init__(self,master):
		super().__init__(master)
		self.pack(padx = 50, pady = 30)
		# self.sudok=SudokControllor()
		self.create_widgets()

		# self.sudoku=SudokControllor(first)

	def create_widgets(self):
		"""
		This method creates widgets for difficulty select window.
		"""
		Label(self, text="Welcome to 數獨(수독)!!",font=("Chalkduster",30), justify=CENTER).grid(row = 0, column = 0)
		Label(self, text="Please select level.", font=("Herculanum",20), justify=CENTER).grid(row = 1, column = 0)
		Button(self, text="Hard", fg = 'red', command=lambda: SudokControllor.hard_select(self), width = 10, height = 5, justify=CENTER).grid(row = 2, column = 0)
		Button(self, text="Normal", fg = 'orange', command=lambda: SudokControllor.normal_select(self), width = 10, height = 5, justify=CENTER).grid(row = 3, column = 0)
		Button(self, text="Easy", fg = 'green', command=lambda: SudokControllor.easy_select(self), width = 10, height = 5, justify=CENTER).grid(row = 4, column=0)
		Button(self, text="Quit", command=self.quit, justify = CENTER).grid(row = 5, sticky = E, columnspan = 1)

class App_H(Frame):
	"""
	This class is the window that shows hard mode sudoku.
	no_of_holes of Hard mode is 40.
	"""
	def __init__(self,master):
		"""
		Initiating...
		"""
		super().__init__(master)
		self.pack(padx = 20, pady = 20)
		self.h = Board()
		self.a=0
		self.show_board()
		self.make_list()
		self.create_widgets()

	def make_list(self):
		"""make string list"""
		enlist=[]
		for i in range(81):
			b=self.entries[i].get()
			enlist.append(b)

		"""change string to integer in enlist"""
		elist_int=[]
		for j in enlist:
			if (j=='1' or j=='2' or j=='3' or j=='4' or j=='5'\
				or j=='6' or j=='7' or j=='8' or j=='9'):
				n=int(j)
				elist_int.append(n)
			if j=='':
				n=0
				elist_int.append(n)

		"""make flat list to list of list"""
		self.enlist_int=[[],[],[],[],[],[],[],[],[]]
		for i in range(9):
			for _ in range(9):
				s=elist_int[0]
				self.enlist_int[i].append(s)
				elist_int.remove(s)

		"""tmp가 int보다 한번 늦게 하기"""
		if self.a==0:
			self.enlist_tmp=self.enlist_int[:]
		if self.a>2:
			self.enlist_tmp=self.enlist_int[:]

		self.a+=1

	def create_widgets(self):
		"""
		This method creates widget for hard mode sudoku.
		"""
		Button(self, text = 'Quit', command = self.quit, justify = CENTER).grid(row = 9, column = 10, sticky = E, columnspan = 1)
		Button(self, text = "Submit", command=self.submit).grid(row = 8, column = 10, sticky = E)
	
	def show_board(self):
		"""
		This method shows sudoku board with holes.
		"""
		self.entries = {}
		self.tableheight = 9
		self.tablewidth = 9

		#hsb=hard solution board
		self.hsb=self.h.create_solution_board()

		#hqb=hard question board
		self.hqb=self.h.copy_board(self.hsb)

		#hqbf=hard question board final
		self.hqbf=self.h.make_holes(self.hqb,40)

		copyboard=self.hqbf[:]

		counter = 0
		for row in range(self.tableheight):
			for column in range(self.tablewidth):
				if ((column==0 or column==1 or column==2 or column==6 or column==7 or column==8) \
					and (row==0 or row==1 or row==2 or row==6 or row==7 or row==8)) or \
					((column==3 or column==4 or column==5) and (row==3 or row==4 or row==5)):
					if copyboard[row][column]==0:
						self.entries[counter]=Entry(self, bg='#dddddd', width=2, justify=CENTER)
						self.entries[counter].grid(row=row, column=column)
					else:
						self.x=StringVar()
						self.entries[counter] = Entry(self, readonlybackground='#dddddd', textvariable=self.x, width=2, justify=CENTER)
						self.x.set(str(copyboard[row][column]))
						self.entries[counter].grid(row=row, column=column)
						self.entries[counter].insert(0,str(copyboard[row][column]))
						self.entries[counter].config(state='readonly')
				else:
					if copyboard[row][column]==0:
						self.entries[counter]=Entry(self, bg='#ffffff', width=2, justify=CENTER)
						self.entries[counter].grid(row=row, column=column)
					else:
						x=StringVar()
						self.entries[counter] = Entry(self, bg='#ffffff', textvariable=x, width=2, justify=CENTER)
						x.set(str(copyboard[row][column]))
						self.entries[counter].grid(row=row, column=column)
						self.entries[counter].insert(0,str(copyboard[row][column]))
						self.entries[counter].config(state='readonly')
				counter += 1

		sw=StopWatch()
		sw.Start()
		sw.pack()

	def submit(self):
		"""int와 tmp가 차이나는 숫자(입력된 숫자)를 정답과 비교해서 틀리면 messagebox popup"""
		App_H.make_list(self)
		for i in range(9):
			for j in range(9):
				if self.enlist_int[i][j]!=self.enlist_tmp[i][j]:
					if self.enlist_int[i][j]!=self.hsb[i][j]:
						messagebox.showinfo("Wrong Answer", "Oh! It's worng number. HAHAHAHAHA! Try Again.")

		if self.enlist_int==self.hsb:
			messagebox.showinfo("Awesome!!!", "You have finished the puzzle!\n" + "Developer: team.Hoecoda\n"+"Park, Lee, Hoe\n"+ "Assist: Prof.Pooh(Doh)")

class App_N(Frame):
	"""
	This class is the window that shows normal mode sudoku.
	no_of_holes of Normal mode is 34.
	"""
	def __init__(self,master):
		"""
		Initiating...
		"""
		super().__init__(master)
		self.pack(padx = 20, pady = 20)
		self.n = Board()
		self.a=0
		self.show_board()
		self.make_list()
		self.create_widgets()

	def make_list(self):
		"""make string list"""
		enlist=[]
		for i in range(81):
			b=self.entries[i].get()
			enlist.append(b)

		"""change string to integer in enlist"""
		elist_int=[]
		for j in enlist:
			if (j=='1' or j=='2' or j=='3' or j=='4' or j=='5'\
				or j=='6' or j=='7' or j=='8' or j=='9'):
				n=int(j)
				elist_int.append(n)
			if j=='':
				n=0
				elist_int.append(n)

		"""make flat list to list of list"""
		self.enlist_int=[[],[],[],[],[],[],[],[],[]]
		for i in range(9):
			for _ in range(9):
				s=elist_int[0]
				self.enlist_int[i].append(s)
				elist_int.remove(s)

		"""tmp가 int보다 한번 늦게 하기"""
		if self.a==0:
			self.enlist_tmp=self.enlist_int[:]
		if self.a>2:
			self.enlist_tmp=self.enlist_int[:]

		self.a+=1


	def create_widgets(self):
		"""
		This method creates widgets for normal mode sudoku.
		"""
		Button(self, text = 'Quit', command = self.quit, justify = CENTER).grid(row = 9, column = 10, sticky = E, columnspan = 1)
		Button(self, text = "Submit", command=self.submit).grid(row = 8, column = 10, sticky = E)

	
	def show_board(self):
		"""
		This method shows sudoku board with holes.
		"""
		self.entries = {}
		self.tableheight = 9
		self.tablewidth = 9

		#nsb = normal solution board
		self.nsb=self.n.create_solution_board()

		#nqb = normal question board
		self.nqb=self.n.copy_board(self.nsb)

		#nqbf = normal question board final
		self.nqbf=self.n.make_holes(self.nqb,34)

		copyboard=self.nqbf[:]

		counter = 0
		for row in range(self.tableheight):
			for column in range(self.tablewidth):
				if ((column==0 or column==1 or column==2 or column==6 or column==7 or column==8) \
					and (row==0 or row==1 or row==2 or row==6 or row==7 or row==8)) or \
					((column==3 or column==4 or column==5) and (row==3 or row==4 or row==5)):
					if copyboard[row][column]==0:
						self.entries[counter]=Entry(self, bg='#dddddd', width=2, justify=CENTER)
						self.entries[counter].grid(row=row, column=column)
					else:
						self.x=StringVar()
						self.entries[counter] = Entry(self, readonlybackground='#dddddd', textvariable=self.x, width=2, justify=CENTER)
						self.x.set(str(copyboard[row][column]))
						self.entries[counter].grid(row=row, column=column)
						self.entries[counter].insert(0,str(copyboard[row][column]))
						self.entries[counter].config(state='readonly')
				else:
					if copyboard[row][column]==0:
						self.entries[counter]=Entry(self, bg='#ffffff', width=2, justify=CENTER)
						self.entries[counter].grid(row=row, column=column)
					else:
						x=StringVar()
						self.entries[counter] = Entry(self, bg='#ffffff', textvariable=x, width=2, justify=CENTER)
						x.set(str(copyboard[row][column]))
						self.entries[counter].grid(row=row, column=column)
						self.entries[counter].insert(0,str(copyboard[row][column]))
						self.entries[counter].config(state='readonly')
				counter += 1

		sw=StopWatch()
		sw.Start()
		sw.pack()

	def submit(self):
		"""int와 tmp가 차이나는 숫자(입력된 숫자)를 정답과 비교해서 틀리면 messagebox popup"""
		App_H.make_list(self)
		for i in range(9):
			for j in range(9):
				if self.enlist_int[i][j]!=self.enlist_tmp[i][j]:
					if self.enlist_int[i][j]!=self.nsb[i][j]:
						messagebox.showinfo("Wrong Answer", "Oh! It's worng number. HAHAHAHAHAHAHAHA! Try Again.")

		if self.enlist_int==self.nsb:
			messagebox.showinfo("Complete", "어-썸\n"+ "Adiós\n"+"Developer: team.Hoecoda\n"+"Park, Lee, Hoe\n"+ "Assist: Prof.Pooh(Doh)")

class App_E(Frame):
	"""
	This class is the window that shows easy mode sudoku.
	no_of_holes of Easy mode is 28.
	"""
	def __init__(self,master):
		"""
		Initiating...
		"""
		super().__init__(master)
		self.pack(padx = 20, pady = 20)
		self.e = Board()
		self.a=0
		self.show_board()
		self.make_list()
		self.create_widgets()
		
	def make_list(self):
		"""make string list"""
		enlist=[]
		for i in range(81):
			b=self.entries[i].get()
			enlist.append(b)

		"""change string to integer in enlist"""
		elist_int=[]
		for j in enlist:
			if (j=='1' or j=='2' or j=='3' or j=='4' or j=='5'\
				or j=='6' or j=='7' or j=='8' or j=='9'):
				n=int(j)
				elist_int.append(n)
			if j=='':
				n=0
				elist_int.append(n)

		"""make flat list to list of list"""
		self.enlist_int=[[],[],[],[],[],[],[],[],[]]
		for i in range(9):
			for _ in range(9):
				s=elist_int[0]
				self.enlist_int[i].append(s)
				elist_int.remove(s)

		"""tmp가 int보다 한번 늦게 하기"""
		if self.a==0:
			self.enlist_tmp=self.enlist_int[:]
		if self.a>2:
			self.enlist_tmp=self.enlist_int[:]

		self.a+=1

	def create_widgets(self):
		"""
		This method creates widgets for easy mode sudoku.
		"""
		Button(self, text = 'Quit', command = self.quit, justify = CENTER).grid(row = 9, column = 10, sticky = E, columnspan = 1)
		Button(self, text = "Submit", command=self.submit).grid(row = 8, column = 10, sticky = E)

	def show_board(self):
		"""
		This method shows sudoku board with holes.
		"""
		self.entries = {}
		self.tableheight = 9
		self.tablewidth = 9

		#esb = easy solution board
		self.esb=self.e.create_solution_board()

		#eqb = easy question board
		self.eqb=self.e.copy_board(self.esb)

		#eqbf = easy question board final
		self.eqbf=self.e.make_holes(self.eqb,28)

		copyboard=self.eqbf[:]

		counter = 0
		for row in range(self.tableheight):
			for column in range(self.tablewidth):
				if ((column==0 or column==1 or column==2 or column==6 or column==7 or column==8) \
					and (row==0 or row==1 or row==2 or row==6 or row==7 or row==8)) or \
					((column==3 or column==4 or column==5) and (row==3 or row==4 or row==5)):
					if copyboard[row][column]==0:
						self.entries[counter]=Entry(self, bg='#dddddd', width=2, justify=CENTER)
						self.entries[counter].grid(row=row, column=column)
					else:
						self.x=StringVar()
						self.entries[counter] = Entry(self, readonlybackground='#dddddd', textvariable=self.x, width=2, justify=CENTER)
						self.x.set(str(copyboard[row][column]))
						self.entries[counter].grid(row=row, column=column)
						self.entries[counter].insert(0,str(copyboard[row][column]))
						self.entries[counter].config(state='readonly')
				else:
					if copyboard[row][column]==0:
						self.entries[counter]=Entry(self, bg='#ffffff', width=2, justify=CENTER)
						self.entries[counter].grid(row=row, column=column)
					else:
						x=StringVar()
						self.entries[counter] = Entry(self, bg='#ffffff', textvariable=x, width=2, justify=CENTER)
						x.set(str(copyboard[row][column]))
						self.entries[counter].grid(row=row, column=column)
						self.entries[counter].insert(0,str(copyboard[row][column]))
						self.entries[counter].config(state='readonly')
				counter += 1

		sw=StopWatch()
		sw.Start()
		sw.pack()

	def submit(self):
		"""int와 tmp가 차이나는 숫자(입력된 숫자)를 정답과 비교해서 틀리면 messagebox popup"""
		App_H.make_list(self)
		for i in range(9):
			for j in range(9):
				if self.enlist_int[i][j]!=self.enlist_tmp[i][j]:
					if self.enlist_int[i][j]!=self.esb[i][j]:
						messagebox.showinfo("Wrong Answer", "Oh! It's worng number. HAHAHAHAHAHAHAHA! Try Again.")
		
		print("tmp:", self.enlist_tmp)
		print("int;", self.enlist_int)
		print("sol:", self.esb)

		if self.enlist_int==self.esb:
			messagebox.showinfo("Complete", "어-썸\n"+ "Adiós\n"+"Developer: team.Hoecoda\n"+"Park, Lee, Hoe\n"+ "Assist: Prof.Pooh(Doh)")


#Controller
class SudokControllor:
	def __init__(self):
		# super().__init__(master)
		first = Tk()
		first.title("수_Doh_구_월-드")
		App(first)
		first.mainloop()

	def hard_select(self):
		"""
		This method destroys difficulty select window and gets a new window for hard mode sudoku.
		"""
		self.destroy()
		SudokControllor.newTk_h()
		self.quit()

	def normal_select(self):
		"""
		This method destroys difficulty select window and gets a new window for normal mode sudoku.
		"""
		self.destroy()
		SudokControllor.newTk_n()
		self.quit()

	def easy_select(self):
		"""
		This method destroys difficulty select window and gets a new window for easy mode sudoku.
		"""
		self.destroy()
		SudokControllor.newTk_e()
		self.quit()

	
	def newTk_h(): 
		"""
		This method creates a new window for hard mode sudoku.
		"""
		hard = Tk()
		hard.title("Hard Mode")
		hard.geometry()
		sw=StopWatch(hard)
		sw.pack(side=TOP)
		App_H(hard)
		hard.mainloop()

	def newTk_n():
		"""
		This method creates a new window for normal mode sudoku.
		"""
		normal = Tk()
		normal.title("Normal Mode")
		normal.geometry()
		App_N(normal)
		normal.mainloop()
	
	def newTk_e():
		"""
		This method creates a new window for easy mode sudoku.
		"""
		easy = Tk()
		easy.title("Easy Mode")
		easy.geometry()
		App_E(easy)
		easy.mainloop()

"""
	Manual
		1. Press the level button that you want to try.
		2. If you press the button, sudoku game board will be poped-up.
		3. Click a box you want by using your mouse and input a number(1~9), and then click the 'submit' button.
			the 'submit' button tell you whether the number is right or wrong.
		4. When you are compelete. sudoku board, complete window would be poped-up.
		5. Congratuations!!! Thank you for playing
"""
SudokControllor()



