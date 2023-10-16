users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']

# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
digit_counter = 0

my_dict = {"Общее количество": 0, "Уникальные посещения": 0}

for i in users:
    if type(users) == list:
        digit_counter += 1

uniq_digit_counter = (len(set(users)))

my_dict["Общее количество"] = digit_counter
my_dict["Уникальные посещения"] = uniq_digit_counter

print(my_dict)