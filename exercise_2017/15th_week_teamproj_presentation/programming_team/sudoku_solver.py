import numpy as np


class Sudoku():
    """Class for handling 9x9 sudokus.

    Args:
        input_grid (str): String with the path to a 9 line text
                          file with 9 numbers where gaps are
                          represented by '0'
        input grid (nda): 9 by 9 numpy array with gaps set as '0'

    Attributes:
        grid (nda): current state of the sudoku grid
        length (int): length of the grid, for now always 9
        sub_length (int): sqrt of the length
        check_sum (int): sum of a unique row/column
        bu_grid (lst): list of backup grids used for guessing
        guesses (int): number of guesses for the current grid
        max_guesses (int): maximal number of guesses for the current grid
        mask (nda): 9x9x9 numpy array (bit mask).

    Example:
        s = Sudoku(np.array(
        [[5, 3, 0, 0, 7, 0, 0, 0, 0],
         [6, 0, 0, 1, 9, 5, 0, 0, 0],
         [0, 9, 8, 0, 0, 0, 0, 6, 0],
         [8, 0, 0, 0, 6, 0, 0, 0, 3],
         [4, 0, 0, 8, 0, 3, 0, 0, 1],
         [7, 0, 0, 0, 2, 0, 0, 0, 6],
         [0, 6, 0, 0, 0, 0, 2, 8, 0],
         [0, 0, 0, 4, 1, 9, 0, 0, 5],
         [0, 0, 0, 0, 8, 0, 0, 7, 9]]))
        s.solve()
        s.print_grid()
        """

    def __init__(self, input_grid):
        """Initialize an instance of the Sudoku class.

        Set up the initial gird based on text or numpy array.
        Next get the length of one of the axis as well as the
        sub length. The check sum is used to validate the grid
        based on unique sum of all digits. The list of back up
        grids is initialized as an empty list together with
        the current guess and the current number of maximal
        guesses. Last the 'bit' mask is set to all zeros.
        """
        self.grid = self.read_grid(input_grid)
        self.length = int(np.sqrt(np.size(self.grid)))
        self.sub_length = int(np.sqrt(self.length))
        self.check_sum = int(np.sum(range(self.length + 1)))
        self.bu_grid = []
        self.guesses = 0
        self.max_guesses = 2
        self.mask = np.zeros([self.length, self.length, self.length])

    def __repr__(self):
        self.print_grid()

    def read_grid(self, input_grid):
        """Parse the sudoku grid.

        Read a text file containing 9 lines with 9 non-spaced digits
        and converts it to numpy array. Blank spaces are represented
        by 0. Alternatively takes a already formatted numpy array as
        input and returns the input as a 9x9 array.
        """
        if isinstance(input_grid, str):
            grid = []
            with open(input_grid) as f:
                text = f.read()
                for line in text.split():
                    grid.append([int(element) for element in line])
            return np.array(grid)
        elif isinstance(input_grid, np.ndarray):
            return input_grid
        else:
            raise ValueError('Not a valid input grid')

    def backup_grid(self):
        """Create a list of back up grids.

        Create a back up of of the current grid and guess number to
        have a restore point in case a guess turns out wrong.
        """
        bckup = BackUpGrid(self.grid, self.guesses)
        self.bu_grid.append(bckup)

    def restore_grid(self):
        """Restore the last backup grid.

        If a back up grid is present overwrite the current grid,
        and increase the guess count by one.
        """
        if not self.bu_grid:
            raise ValueError('No backup grid')
        else:
            self.bu_grid[-1].guesses += 1
            bckup = self.bu_grid[-1]
            self.grid = bckup.grid
            self.guesses = bckup.guesses

    def print_grid(self):
        """Print formatted grid."""
        BOLD = '\033[1m'
        ENDC = '\033[0m'

        fill_mask = np.sum(self.mask, axis=2) == 1

        top_line = '┏' + ('━━┯' * 2 + '━━┳') * 2 + '━━┯' * 2 + '━━┓'
        mid_line = '┣' + ('━━┿' * 2 + '━━╋') * 2 + '━━┿' * 2 + '━━┫'
        bot_line = '┗' + ('━━┷' * 2 + '━━┻') * 2 + '━━┷' * 2 + '━━┛'
        div_line = '┠' + ('──┼' * 2 + '──╂') * 2 + '──┼' * 2 + '──┨'
        num_line = '┃ %s│ %s│ %s' * 3 + '┃'

        counter = 1
        print(top_line)
        for row_index, row in enumerate(self.grid):
            line_to_print = []
            for col_index, cell in enumerate(row):
                if fill_mask[row_index, col_index] == 1:
                    line_to_print.append(BOLD + str(cell) + ENDC)
                elif cell == 0:
                    line_to_print.append(' ')
                else:
                    line_to_print.append(str(cell))
            print(num_line % tuple(line_to_print))
            if (counter % 3 == 0) and counter < 9:
                print(mid_line)
            elif counter < 9:
                print(div_line)
            counter += 1
        print(bot_line)

    def fill_grid(self):
        """Fill the sudoku grid based on the mask.

        Looks for all the points where the third axis has only one
        option and sets the corresponding number in the grid.
        """
        unique_mask = self.mask.sum(axis=2) == 1
        for i in range(self.length):
            value_mask = self.mask[:, :, i] != 0
            self.grid[np.logical_and(unique_mask, value_mask)] = i + 1

            sub_slice_index = np.arange(0, self.length + 1, self.sub_length)
            for k in range(self.sub_length):
                for l in range(self.sub_length):
                    sub_mask = \
                        self.mask[sub_slice_index[k]:sub_slice_index[k+1],
                                  sub_slice_index[l]:sub_slice_index[l+1], i]
                    if np.sum(sub_mask) == 1:
                        possition = np.where(sub_mask)
                        self.grid[sub_slice_index[k] + possition[0],
                                  sub_slice_index[l] + possition[1]] = i + 1

    def update_mask(self):
        """Solve the bit mask for each cell."""
        # Create initial mask and remove already filled points
        mask = np.dstack([self.grid == 0] * self.length)
        sub_slice_index = np.arange(0, self.length + 1, self.sub_length)
        full_slice = np.arange(self.length)
        for i in range(self.length):  # Loop trough numbers to fill
            for j in range(self.length):  # Loop trough columns/rows
                # Check for horizontal and vertical matches
                if i + 1 in self.grid[j, :]:
                    mask[j, :, i] = False
                if i + 1 in self.grid[:, j]:
                    mask[:, j, i] = False
                # Check the 3x3 blocks
            for k in range(self.sub_length):
                for l in range(self.sub_length):
                    # Get the 3x3 grid and mask
                    sub_slice = \
                        mask[sub_slice_index[k]:sub_slice_index[k+1],
                             sub_slice_index[l]:sub_slice_index[l+1], i]
                    sub_grid = \
                        self.grid[sub_slice_index[k]:sub_slice_index[k+1],
                                  sub_slice_index[l]:sub_slice_index[l+1]]
                    # If value is in 3x3 block set mask for entire block
                    # to false
                    if i + 1 in sub_grid:
                        mask[sub_slice_index[k]:sub_slice_index[k+1],
                             sub_slice_index[l]:sub_slice_index[l+1], i] \
                             = False
                    # If only one value exists in the 3th axis set all others
                    # in the sub slice to False
                    elif np.sum(sub_slice) == 1:
                        possition = np.where(sub_slice)
                        cut_slice = np.delete(full_slice, i)
                        mask[sub_slice_index[k] + possition[0],
                             sub_slice_index[l] + possition[1],
                             cut_slice] = False
                    # Check if position in 3x3 block eliminates some
                    # horizontal or vertical options
                    if (1 < np.sum(sub_slice) <= self.sub_length):
                        possition = np.where(sub_slice)
                        check_horizontal = possition[0][0] == possition[0]
                        check_vertical = possition[1][0] == possition[1]
                        if check_horizontal.all():
                            keep = sub_slice_index[l] + possition[1]
                            cut_slice = np.delete(full_slice, keep)
                            mask[possition[0][0] + sub_slice_index[k],
                                 cut_slice, i] = False
                        elif check_vertical.all():
                            keep = sub_slice_index[k] + possition[0]
                            cut_slice = np.delete(full_slice, keep)
                            mask[cut_slice, possition[1][0] +
                                 sub_slice_index[l], i] = False
        self.mask = mask

    def solve(self, max_itter=150, grid_out=False, verbose=False,
              user_controle=False):
        """Main solver routine to solve a 9x9 sudoku."""
        count = 0
        if verbose:
            self.print_grid()
        while count < max_itter:
            is_valid = self.is_valid()
            solved = self.is_solved()
            if solved and is_valid:
                if verbose:
                    print('Grid solved')
                if grid_out:
                    return True, self.grid
                else:
                    return True
            self.update_mask()
            if ((np.sum(self.mask, axis=2) == 1).any() and is_valid):
                if verbose:
                    print('Filling %i cells' %
                          int(np.sum(np.sum(self.mask, axis=2) == 1)))
                self.fill_grid()
            elif ((np.sum(self.mask, axis=2) > 1).any() and is_valid):
                if verbose:
                    print('Valid grid but nothing to fill. Guessing...')
                self.guesses = 0
                self.backup_grid()
                self.guess()
                self.fill_grid()
            else:
                if verbose:
                    print('Guessed wrong, resetting grid')
                self.restore_grid()
                self.update_mask()
                self.guess()
                self.fill_grid()
                if self.guesses == (self.max_guesses - 1):
                    self.bu_grid.pop(-1)

            count += 1
            if verbose:
                print('On loop: %02i' % count)
                self.print_grid()
            if user_controle:
                inp = input("'' --> Next\n'e' --> Go to end\n'q' --> Quit\n")
                if inp is 'e':
                    user_controle = False
                elif inp is 'q':
                    break
        return False

    def guess(self):
        """Guessing routine.

        Start by looking for the position where only two options are
        possible. For this position guess the first option by
        setting the second option to false in the mask. If there are no
        two option cells increase to 3 options etc.
        """
        n_options = 2
        while n_options < 9:
            position = np.where(self.mask.sum(axis=2) == n_options)
            if position[0].any():
                self.max_guesses = n_options
                x = position[0][0]
                y = position[1][0]
                options = np.arange(self.length)[self.mask[x, y, :]]
                options = np.delete(options, self.guesses)
                self.mask[x, y, options] = False
                return
            else:
                n_options += 1

    def is_valid(self):
        """Check for duplicates in sudoku grid."""
        for i in range(self.length):
            vertical = self.grid[:, i].tolist()
            horizontal = self.grid[i, :].tolist()
            for j in range(self.length):
                try:
                    vertical.remove(j + 1)
                except ValueError:
                    pass
                try:
                    horizontal.remove(j + 1)
                except:
                    pass
            if (np.sum(vertical) or np.sum(horizontal)) > 0:
                return False
        return True

    def is_solved(self):
        """Check if the gird is fully solved"""
        for i in range(self.length):
            if int(np.sum(self.grid[i, :])) != self.check_sum:
                return False
            if int(np.sum(self.grid[:, i])) != self.check_sum:
                return False
        return True


class BackUpGrid():
    """Back up class.

    Minimal class to store both the grid as well as the current
    number of guesses.
    """

    def __init__(self, grid, guesses):
        self.grid = np.array(grid)
        self.guesses = guesses




s = Sudoku(np.array(
[[5, 3, 0, 0, 7, 0, 0, 0, 0],
 [6, 0, 0, 1, 9, 5, 0, 0, 0],
 [0, 9, 8, 0, 0, 0, 0, 6, 0],
 [8, 0, 0, 0, 6, 0, 0, 0, 3],
 [4, 0, 0, 8, 0, 3, 0, 0, 1],
 [7, 0, 0, 0, 2, 0, 0, 0, 6],
 [0, 6, 0, 0, 0, 0, 2, 8, 0],
 [0, 0, 0, 4, 1, 9, 0, 0, 5],
 [0, 0, 0, 0, 8, 0, 0, 7, 9]]))
s.print_grid()
s.solve()
s.print_grid()