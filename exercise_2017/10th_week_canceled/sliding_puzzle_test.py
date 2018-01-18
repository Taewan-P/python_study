def create_init_board():
	import random
	grouped = []
	not_grouped = random.sample(range(0,size**2),size**2)

	for i in range(0,size):
		temp = []
		for j in range(0,size): #리스트 안에 리스트 넣는거
			temp.append(not_grouped[j])
		not_grouped = not_grouped[n:]
		grouped.append(temp)
	
	return grouped

# print(create_init_board(2))


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

print(create_goal_board(4))