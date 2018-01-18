import time as tm
import Tkinter as tk
import cProfile


GRIDA = [
        3, 0, 8, 0, 1, 4, 0, 0, 9,
        0, 0, 2, 0, 6, 0, 1, 7, 4,
        7, 1, 0, 5, 9, 0, 8, 0, 0,
        0, 0, 0, 9, 0, 3, 4, 1, 7,
        5, 9, 0, 2, 4, 0, 3, 0, 0,
        4, 3, 7, 0, 0, 6, 0, 5, 0,
        1, 0, 5, 4, 0, 0, 0, 3, 8,
        0, 2, 0, 0, 3, 5, 7, 0, 1,
        0, 4, 3, 6, 0, 1, 0, 9, 0 
        ]
GRIDNIL = [
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 0, 0, 0, 0 
        ]
ULTIGRID = [
         0, 0, 0, 0, 0, 4, 2, 0, 0,
         2, 0, 0, 5, 1, 0, 0, 0, 0,
         7, 8, 0, 0, 0, 6, 4, 0, 0,
         5, 9, 0, 0, 0, 7, 0, 0, 0,
         0, 4, 0, 0, 0, 0, 0, 8, 0,
         0, 0, 0, 2, 0, 0, 0, 9, 5,
         0, 0, 7, 4, 0, 0, 0, 3, 2,
         0, 0, 0, 0, 3, 9, 0, 0, 1,
         0, 0, 3, 1, 0, 0, 0, 0, 0
        ]
GRIDB = [
         0, 0, 5, 8, 0, 0, 0, 0, 2,
         8, 0, 0, 0, 0, 0, 4, 0, 0,
         0, 0, 9, 5, 0, 0, 0, 7, 8,
         7, 0, 0, 3, 0, 0, 1, 0, 0,
         0, 4, 0, 0, 0, 0, 0, 8, 0,
         0, 0, 6, 0, 0, 8, 0, 0, 3,
         6, 9, 0, 0, 0, 3, 7, 0, 0,
         0, 0, 2, 0, 0, 0, 0, 0, 9,
         1, 0, 0, 0, 0, 7, 2, 0, 0
        ]



class Solver(object):
    def __init__(self, grid, mode):
        self._grid = grid
        self._mode = mode
        solver = Grid(self._grid, self._mode)
        Solver.root = tk.Tk()
        Solver.root.title('')
        Solver.window = tk.Canvas(Solver.root, height=1000, width=750, bg='white')
        Solver.window.pack(expand=True)
        Solver.root.after(0, solver.draw_grid)
        Solver.root.mainloop()

class Grid(Solver):
    def __init__(self, grid, mode):
        Grid._grid = grid
        Grid._cells = []
        self._mode = mode
        self._labels = {}
        self.populate_cells()
        self._empty_cells = []
        self.empty_cells()
        self._iterations = 0

    def populate_cells(self):
        for ind in range(81):
            c = Cell(ind)
            self._cells.append(c)

    def empty_cells(self):
        """list of empty cells positions and removes those solvable."""
        for ind in range(81):
            c = self._cells[ind]
            if c._value == 0:
                c._search_range = c.new_search_range()
                self._empty_cells.append(c)
            else:
                c._solved = True
            if len(c._search_range) == 1:
                    c._value = c._search_range[0]
                    c._pre_solved = True
                    del self._empty_cells[-1]

    def solve(self, index):
        """main loop iterate through the empty cells and backtrack."""
        self._iterations += 1
        c = self._empty_cells[index]
        c.new_cell_value()
        if c._value == None:
            c._solved = False
            c._value = 0
            if self._mode != 'fast':
                self._labels[(c._rw, c._col)].config(text=str(' '))
            index -= 1  #backtrack to previous empty cell at next iteration            
        else:
            if self._mode != 'fast':
                self._labels[(c._rw, c._col)].config(text=str(c._value))
            c._solved = True
            index += 1
        Solver.root.update_idletasks()
        if index<len(self._empty_cells) and index>=0:
            Solver.root.after(0, lambda: self.solve(index))
        else:
            self.update_cells_tags()
            Solver.root.update()
            print("solved in {} iterations").format(self._iterations)
            tm.sleep(2)
            Solver.root.after(0, self.quit_solve)

    def quit_solve(self):
        try:
            Solver.root.destroy()
        except:
            pass

    def draw_grid(self):
        """draw the grid and create a label for each cell in Tk."""
        for i in range(50, 685, 70):
            if (i-50)%210 == 0:
                lw=5
            else:
                lw=1
            Solver.window.create_line([(50, i), (680, i)],
                                   width=lw,
                                   joinstyle='miter',
                                   capstyle='projecting')
            Solver.window.create_line([(i, 50), (i, 680)],
                                   width=lw,
                                   joinstyle='miter',
                                   capstyle='projecting'
                                   )
        for c in self._cells:
            if c._pre_solved:
                txt = str(c._value)
                backg = "#fcfce1" # solved before backtracking loop
            elif c._solved:
                txt = str(c._value)
                backg = "#f7d52e" # original grid
            else:
                txt = ' '
                backg = '#ffffff' # empty cells
            coloured_sq = Solver.window.create_rectangle(51 + c._y, 51 + c._x,
                                                         119 + c._y, 119 + c._x,
                                                         fill=backg,
                                                         outline=backg)
            self._labels[(c._rw, c._col)] = tk.Label(Solver.window,
                                                     text=txt,
                                                     relief=tk.FLAT,
                                                     bg = backg,
                                                     font=("Courier", 54))
            self._labels[(c._rw, c._col)].place (x=66+c._y, y=55+c._x)
            Solver.window.pack(expand=True)
        Solver.root.after(0, self.solve(0)) #start looping

    def update_cells_tags(self):
        for c in self._cells:
            self._labels[(c._rw, c._col)].config(text=str(c._value))

    def show(self):
        """for testing prints the grid in a pretty format."""
        for r in range(9):
            if r%3 == 0:
                print '+ - - - - + - - - - + - - - - +'
            s = ''
            for c in range(9):
                if c%3 == 0:
                    s += '|'
                if self._cells[r*9+c]._value == 0:
                    s += ' . '
                else:
                    s += ' '+str(self._cells[r*9+c]._value)+' '
            s += '|'
            print s
        print '+ - - - - + - - - - + - - - - +'


class Cell(Grid):
    """81 cells in a 9x9 sudoku grid."""
    def __init__(self, index):
        self._grid = Grid._grid
        self._rw = index/9
        self._col = index - self._rw * 9 
        self._index = index
        self._value = self._grid[index]
        self._x = self._rw * 70
        self._y = self._col * 70
        self._search_range = range(1, 10)
        self._pre_solved = False
        self._solved = not self._value==0

    def new_cell_value(self):
        """the next candidate value and the remaining candidates."""
        for v in self._search_range:
            if self.check_unique(v): # candidate value is unique one row, column or square
                self._search_range.remove(v)
                break 
        else:
            v = None # all values already in row, column or square
            self._search_range = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self._value = v

    def new_search_range(self):
        """the range of possible values for the cell."""
        return [n for n in range(1, 10) if self.check_unique(n)]

    def check_unique(self, v):
        """no cell with value v exists in the row, column or square."""
        if v not in self.row() and \
           v not in self.column() and \
           v not in self.square():
            return True
        else:
            return False

    def column(self):
         """Returns the list of cells in the column."""
         return [Grid._cells[self._col+incr]._value for incr in range(0, 81, 9)]

    def row(self):
         """Returns the list of cells in the row."""
         return [Grid._cells[self._rw*9+c]._value for c in range(9)]

    def square(self):
        """Returns the list of cells in the square."""
        sq = []
        rcorner = (self._rw/3)*3
        ccorner = (self._col/3)*3
        for r in (0, 1, 2):
            for c in (0, 1, 2):
                sq.append(Grid._cells[(r+rcorner)*9+c+ccorner]._value)
        return sq

def main():
    solver = Solver(ULTIGRID, None)

cProfile.run('main()')