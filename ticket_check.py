ticket_order_num = input("Введите количество билетов, которые вы хотите приобрести на мероприятие:")
arr_for_age_for_every_ticket = []
arr_for_all_costs = []
final_costs_of_all_ticket = 0
for i in range(int(ticket_order_num)):
    print("Введите возраст человека номер", i + 1)
    single_person_age = 0
    single_person_age = input()
    arr_for_age_for_every_ticket.append(single_person_age)

print(arr_for_age_for_every_ticket)

for i in arr_for_age_for_every_ticket:
    if int(i) < 18:
        arr_for_all_costs.append(0)
    elif int(i) >= 18 and int(i) <= 25:
        arr_for_all_costs.append(990)
    elif int(i) > 25:
        arr_for_all_costs.append(1390)

for i in arr_for_all_costs:
    final_costs_of_all_ticket = i + final_costs_of_all_ticket


print(arr_for_all_costs)
print(final_costs_of_all_ticket)

if len(arr_for_all_costs) > 3:
    print("Цена со скидкой:")
    print(final_costs_of_all_ticket - (final_costs_of_all_ticket/100*10))
else:
    print("Цена без скидки:")
    print(final_costs_of_all_ticket)