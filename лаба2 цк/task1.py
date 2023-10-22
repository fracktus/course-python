money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен

budget_month = salary + money_capital
count = 0

while (budget_month >= spend):
    count += 1
    spend = spend + spend * increase
    budget_month = budget_month - (spend - salary)

print("Количество месяцев, которое можно протянуть без долгов:", count)
