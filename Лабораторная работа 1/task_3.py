list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды

digit_counter = 0

for i in list_players:
    if type(list_players) == list:
        digit_counter += 1

count_of_player = int(digit_counter // 2)

team_1 = list_players[:count_of_player]
team_2 = list_players[count_of_player:]
print(team_1)
print(team_2)

