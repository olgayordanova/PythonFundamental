import collections

def position_exist(list_tup, position):
    for item in list_tup:
        if position == item[0]:
            return True
    return False

def update_skill(list_tup, position, skill):
    for i in range(0,len(list_tup)):
        if position == list_tup[i][0] and list_tup[i][1]<skill:
            t = (position,skill)
            list_tup[i] = t
    return list_tup


def battle(players, player_1, player_2):
    list_tup_1 = players[player_1]
    list_tup_2 = players[player_2]
    for i in range ( 0, len ( list_tup_1 ) ):
        for j in range ( 0, len ( list_tup_2 ) ):
            if list_tup_1[i][0] == list_tup_2[j][0]:
                if list_tup_1[i][1]>list_tup_2[j][1]:
                    del players[player_2]
                elif list_tup_1[i][1]<list_tup_2[j][1]:
                    del players[player_1]
    return players

def get_total_skill_lst(players):
    total_skill_lst=[]
    for player in players.keys():
        total_points = 0
        for key, value in players.items ():
            if player in key:
                for m in range(0,len(value)):
                    total_points+=value[m][1]
        t = (player, total_points)
        total_skill_lst.append ( t )
    total_skill_lst = sorted ( total_skill_lst, key=lambda x: (-x[1], x[0]) )
    return total_skill_lst

def get_position(players, player):
    position_lst = []
    if player in players.keys():
        for m in range(0,len(players[player])):
            t = (players[player][m][0], players[player][m][1])
            position_lst.append(t)
    position_lst = sorted(position_lst, key=lambda x: (-x[1], x[0]))
    return position_lst



players = {}
while True:
    line = input()
    if line == 'Season end':
        break

    if " -> " in line:
        player, position, skill = line.split(" -> ")
        t = (position, int(skill))
        if player not in players.keys():
            players.setdefault ( player, [] ).append ( t )
        else:
            if not position_exist(players[player], position):
                players[player].append( t )
            else:
                players[player] = update_skill(players[player], position, int(skill))
    elif " vs " in line:
        player_1, player_2 = line.split(" vs ")
        if player_1 in players and player_2 in players:
            players = battle(players,player_1,player_2)


total_points_lst = get_total_skill_lst(players)
for el in range ( 0, len ( total_points_lst ) ):
    print ( f"{total_points_lst[el][0]}: {total_points_lst[el][1]} skill" )
    position_lst = get_position(players, total_points_lst[el][0])
    for ss in range ( 0, len ( position_lst ) ):
        print ( f"- {position_lst[ss][0]} <::> {position_lst[ss][1]}" )
