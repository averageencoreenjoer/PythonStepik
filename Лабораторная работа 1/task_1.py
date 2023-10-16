numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
# TODO заменить значение пропущенного элемента средним арифметическим
digit_counter = 0
sum_counter = 0

for i in numbers:
    if type(numbers) == list:
        digit_counter += 1

for j in numbers:
    if j is not None:
        sum_counter += j

new_num = sum_counter / digit_counter
numbers_2 = [2, -93, -2, 8, new_num, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
print("Измененный список:", numbers_2)