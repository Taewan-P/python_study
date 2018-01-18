def sliding_puzzle(size):
	board = create_init_board(size)
	goal = create_goal_board(size)
	empty = find_position(0,board)
	while True:
		print_board(board)
		if board == goal:
			print("Congratulations!")
			break
		num = get_number(size)
		if num == 0:
			break
		pos = find_position(num, board)
		(empty, board) = move(pos, empty, board)
	print("Please come again.")




def create_init_board(size):
	import random
	grouped = []
	not_grouped = random.sample(range(0,size**2),size**2)

	for i in range(0,size):
		temp = []
		for j in range(0,size): #리스트 안에 리스트 넣는거
			temp.append(not_grouped[j])
		not_grouped = not_grouped[size:]
		grouped.append(temp)
	
	return grouped


def create_goal_board(size):
	board_1 = []
	goal_board = []
	for i in range(1,(size**2)+1):
		board_1.append(i)

	for h in range(0,size):
		temp = []
		for j in range(0,size):
			temp.append(board_1[j])
		board_1 = board_1[size:]
		goal_board.append(temp)

	goal_board[size-1][size-1] = 0
	return goal_board


def print_board(board):
	for row in board:
		for num in row:
			if num == 0:
				print("  ",end = ' ')
			elif 10 <= num:
				print(num,end = ' ')
			else: #num 이 한자리 수인 경우
				print(str(num).rjust(2), end = ' ')
		print()
		


def get_number(size):
	num = input("Type the number you want to move (Type 0 to quit): ")
	while not(num.isdigit() and 0 <= int(num) <= (size**2)-1):
		num = input("Type the number you want to move (Type 0 to quit): ")
	return int(num)


def find_position(num,board):
	for i in range(int(size)):
		for j in range(int(size)):
			if num == board[i][j]:
				return (i,j)


def move(pos, empty, board): #move(pos,empty,board) => (new_empty,new_board)
	(x,y) = pos
	if empty == (x-1,y) or empty == (x+1,y) or empty == (x,y-1) or empty==(x,y+1):
		board[empty[0]][empty[1]] = board[x][y]
		board[x][y] = 0
		return (pos,board)
	else:
		print("Can't move! Try again.")
		return (empty,board)






# 콘솔창에서 파일 실행하면서 바로 입력값 받게 해주는 코드
if __name__ == "__main__":
	import sys
	size = sys.argv[1]
	if size.isdigit() and int(size) > 1:
		sliding_puzzle(int(size))
	else:
		print("Not a proper system argument.")




