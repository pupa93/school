per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
print(per_cent)
money = input("сумма money, которую человек планирует положить под проценты: ")
my_arr = []
for x in per_cent:
    my_arr.append(float(money) / 100 * per_cent[x])

print("deposit = ", my_arr)
print("Максимальная сумма, которую вы можете заработать", max(my_arr))
