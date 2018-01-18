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

#Etc.
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
		""" Set the time string to Hours:Minutes:Seconds. """
		self.hours=int(elap/3600)
		self.minutes = int(elap/60-self.hours*60.0)
		self.seconds = int(elap - self.minutes*60.0-self.hours*3600)                
		self.timestr.set('%02d:%02d:%02d' % (self.hours, self.minutes, self.seconds))
		self.Stop()
        
	def Start(self):                                                     
		""" Start the stopwatch, ignore if running. """
		if not self._running:            
			self._start = time.time() - self._elapsedtime
			self._update()
			self._running = 1        
			
	def Stop(self):                                    
		""" Stop the stopwatch, ignore if stopped. """
		if self.seconds==5: # change this line to (self.puzzle==sol)
			self.after_cancel(self._timer)
			self.completebox(self.hours, self.minutes, self.seconds)  
			self._elapsedtime = time.time() - self._start
			self._setTime(self._elapsedtime)
			self.Reset()
			# self._running = 0
			
    def Reset(self):
		""" Reset the stopwatch. """
		self._start = time.time()         
		self._elapsedtime = 0.0    
		self._setTime(self._elapsedtime)



	def completebox(self,hours,minutes,seconds):
		messagebox.showinfo("Complete", "어-썸\n" + "Adiós\n" + "It took " + str(hours) + \
							 " hours, " + str(minutes) + " minutes, " + str(seconds) + \
							 " seconds for you to solve this sudoku.\nDeveloper: team.Hoecoda\nPark, Lee, Hoe\nAssist: Prof.Pooh(Doh)")
		

#Viewer
class App(Frame):
	"""
	This class is a window that shows user to choose difficulty.
	"""
	def __init__(self,master):
		super().__init__(master)
		self.pack(padx = 50, pady = 30)
		self.create_widgets()

	def create_widgets(self):
		"""
		This method creates widgets for difficulty select window.
		"""
		Label(self, text="Welcome to 數獨(수독)!!",font=("Chalkduster",30), justify=CENTER).grid(row = 0, column = 0)
		Label(self, text="Please select level.", font=("Herculanum",20), justify=CENTER).grid(row = 1, column = 0)
		Button(self, text="Hard", fg = 'red', command=self.hard_select, width = 10, height = 5, justify=CENTER).grid(row = 2, column = 0)
		Button(self, text="Normal", fg = 'orange', command=self.normal_select, width = 10, height = 5, justify=CENTER).grid(row = 3, column = 0)
		Button(self, text="Easy", fg = 'green', command=self.easy_select, width = 10, height = 5, justify=CENTER).grid(row = 4, column=0)
		Button(self, text="Quit", command=self.quit, justify = CENTER).grid(row = 5, sticky = E, columnspan = 1)

	def hard_select(self):
		"""
		This method destroys difficulty select window and gets a new window for hard mode sudoku.
		"""
		self.destroy()
		App.newTk_h()
		self.quit()

	def normal_select(self):
		"""
		This method destroys difficulty select window and gets a new window for normal mode sudoku.
		"""
		self.destroy()
		App.newTk_n()
		self.quit()

	def easy_select(self):
		"""
		This method destroys difficulty select window and gets a new window for easy mode sudoku.
		"""
		self.destroy()
		App.newTk_e()
		self.quit()

	
	def newTk_h():
		"""
		This method creates a new window for hard mode sudoku.
		"""
		hard = Tk()
		hard.title("Hard Mode")
		hard.geometry()
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

#여기서 부터 닥스트링 처리하자.
class App_H(Frame):
	"""
	스도쿠 난의도를 하드 모드로 선택했을때 실행되는 창이다.
	하드 모드는 빈칸의 갯수를 40개로 설정하였다.
	This class is the window that 
	"""
	def __init__(self,master):
		super().__init__(master)
		self.pack(padx = 20, pady = 20)
		self.h = Board()
		self.create_widgets()
		self.show_board()


	def create_widgets(self):
		Button(self, text = 'Quit', command = self.quit, justify = CENTER).grid(row = 9, column = 10, sticky = E, columnspan = 1)

	
	def show_board(self):
		self.entries = {}
		self.tableheight = 9
		self.tablewidth = 9

		#hsb=hard solution board
		hsb=self.h.create_solution_board()

		#hqb=hard question board
		hqb=self.h.copy_board(hsb)

		#hqbf=hard question board final
		hqbf=self.h.make_holes(hqb,40)

		copyboard=hqbf[:]

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
		self.show_board()


	def create_widgets(self):
		Button(self, text = 'Quit', command = self.quit, justify = CENTER).grid(row = 9, column = 10, sticky = E, columnspan = 1)

	
	def show_board(self):
		self.entries = {}
		self.tableheight = 9
		self.tablewidth = 9

		#hsb=hard solution board
		nsb=self.n.create_solution_board()

		#hqb=hard question board
		nqb=self.n.copy_board(nsb)

		#hqbf=hard question board final
		nqbf=self.n.make_holes(nqb,34)

		copyboard=nqbf[:]

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
		self.show_board()


	def create_widgets(self):
		Button(self, text = 'Quit', command = self.quit, justify = CENTER).grid(row = 9, column = 10, sticky = E, columnspan = 1)

	
	def show_board(self):
		self.entries = {}
		self.tableheight = 9
		self.tablewidth = 9

		#hsb=hard solution board
		esb=self.e.create_solution_board()

		#hqb=hard question board
		eqb=self.e.copy_board(esb)

		#hqbf=hard question board final
		eqbf=self.e.make_holes(eqb,28)

		copyboard=eqbf[:]

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


#Controller
class SudokController(Frame):
	def __init__(self,master):
		super().__init__(master)
		self.app=App(first)





#Level Select Window
first = Tk()
first.title("수_Doh_구_월-드")
App(first)
first.mainloop()