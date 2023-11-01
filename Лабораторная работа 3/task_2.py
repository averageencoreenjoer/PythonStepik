# TODO Напишите функцию find_common_participants
def find_common_participants(a, b, separator=','):
    a_list, b_list = a.split(separator), b.split(separator)
    result = []
    for test_name in a_list :
        if test_name in b_list:
            result.append(test_name)
            result.sort()
    return result


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group, '|'))
