money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

# TODO Посчитайте количество  месяцев, которое можно протянуть без долгов


counter = 0

sum_capital = money_capital + salary - spend # 19000

while sum_capital >= 0 :
    sum_capital = sum_capital + salary - spend * (1 + increase)
    spend = spend * (1 + increase)
    counter += 1

print("Количество месяцев, которое можно протянуть без долгов:", counter)
