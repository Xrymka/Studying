for i in range (25, 51):
    print(i)

shows = ["Ходячие мертвецы", "Красавцы", "Клан Сопрано", "Дневники вампира"]
for index, show in enumerate(shows):
    print(index)
    print(show)

numbers = [11, 32, 33, 15, 1]

while True:
    answer = input("Угадайте число или введите Х для выхода.")
    if answer == "Х":
        break
    try:
        answer = int(answer)
    except ValueError:
        print("пожалуйста, введите число или Х для выхода.")
    if answer in numbers:
        print("Вы угадали!")
    else:
        print("Неправильно!")

list1 = [8, 19, 148, 4]
list2 = [9, 1, 33, 83]
list3 = []
for i in list1:
    for j in list2:
        list3.append(i * j)

print(list3)
