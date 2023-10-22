salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

capitals = []

for i in range(1, months+1):
    money_capital = spend - salary
    spend = spend + spend * increase
    capitals.append(money_capital)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(sum(capitals), 2))
