list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

len_list = len(list_players)
len_list_team = int(len_list/2)

team_1 = list_players[0:len_list_team]
team_2 = list_players[len_list_team:]

print(team_1)
print(team_2)