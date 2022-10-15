posledovatelnost = input("последовательность чисел через пробел : ")
sluchajnoe_chislo = int(input("любое число : "))
splited_posled = posledovatelnost.split()
for i in range(0, len(splited_posled)):
    splited_posled[i] = int(splited_posled[i])


def binary_search(new_arr, sluchajnoe_chislo, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if new_arr[middle] < sluchajnoe_chislo <= new_arr[middle+1]:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif sluchajnoe_chislo < new_arr[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(new_arr, sluchajnoe_chislo, left, middle - 1)
    elif sluchajnoe_chislo > new_arr[middle+1] :  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(new_arr, sluchajnoe_chislo, middle + 1, right)
    else:  # иначе в правой
        print("net takogo chisla")
        return False




new_arr = splited_posled
new_arr.sort()
print('отсортированный список: ', new_arr)
print('число для сравнения: ', sluchajnoe_chislo)

if sluchajnoe_chislo >= new_arr[len(new_arr)-1]:
    print("Нет такого числа, так как число для сравнения: ", sluchajnoe_chislo, ", больше самого большего числа в последовательности!")
elif sluchajnoe_chislo <= new_arr[0]:
    print("Нет такого числа, так как число для сравнения: ", sluchajnoe_chislo, ", меньше самого маленького числа в последовательности!")
else:#запускаем алгоритм
    print('номер позиции элемента, который меньше введенного пользователем числа, а следующий за ним больше или равен этому числу:', binary_search(new_arr, sluchajnoe_chislo, 0, len(new_arr)))