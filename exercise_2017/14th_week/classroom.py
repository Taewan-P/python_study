def load_member():
	file = open("members.txt", 'r')
	members = {}
	
	for line in file: #\n 마다 한줄씩 읽는다...?
		m = line.strip('\n').split(',')
		members[m[0]] = (int(m[1]), float(m[2]), int(m[3]))
	

	file.close()
	return members

def load_members2(): 
	file = open("members.txt", "r") 
	members = {} 
	for line in file: 
		name, tries, wins, chips = line.strip('\n').split(',') 
		members[name] = (int(tries), float(wins), int(chips)) 
	file.close() 
	return members

def store_member(members):
	file = opne("members.txt", 'w')

	for key in members:
		(tries,wins,chips) = members[key]
		line = key + ',' + str(tries) + ',' + str(wins) + ',' + str(chips) + '\n'
		file.write(line)

	file.close()

def store_members2(members): 
	file = open("members.txt", "w") 
	names = members.keys() 
	for name in names: 
		tries, wins, chips = members[name] 
		line = name + ',' + str(tries) + ',' + \
		       str(wins) + "," + str(chips) + '\n'    
		file.write(line) 
	file.close()

def login():
	name = input("Enter your name : (four char max)")
	while len(name) > 4:
		name = input("Enter your name : (four char max)")

	members = load_member()
	if name in members:
		(tries,wins,chips) = members(name)
		print(tries,"시도",wins,"이김")
		print("보유 칩 개수는 ", chips)
		winrate = (wins/tries)*100 if tries > 0 else 0
		print("손님의 숭률은 ", "{0:.2f}".format(winrate),"%")
		return name, tries, wins, chips

	else:
		members[name] = (0,0,0)
		return name,0,0,0

def show_top5(): 
    members = load_members() 
    print('-----') 
    sorted_members = sorted(members.items(),\
                            key=lambda x: x[1][2],\
                            reverse=True) 
    print("All-time Top 5") 
    rank = 1 
    for member in sorted_members[:5]: 
        chips = member[1][2] 
        if chips <= 0: 
            break 
        print(rank, '.', member[0], ':', chips) 
        rank += 1

















