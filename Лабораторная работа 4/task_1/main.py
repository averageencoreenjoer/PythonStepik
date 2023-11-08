# TODO решите задачу
import json


def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)

    total_sum = 0

    for dictionary in data:

        if 'score' in dictionary and 'weight' in dictionary:
            product = dictionary['score'] * dictionary['weight']
            total_sum += product
        else:
            print('error')

    rounded_total_sum = round(total_sum, 3)

    return rounded_total_sum

print(task())
