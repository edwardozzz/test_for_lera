# Исходные данные
data = [75, 31, 33, 82, 10, 12, 9, 33, 71, 5, 42]

# Сортируем данные по возрастанию
sorted_data = sorted(data)
groups = {}
group_num = 1
groups[sorted_data[0]] = group_num

# Проходим по отсортированным значениям и назначаем группу,
# увеличивая номер группы при значительном разрыве (условно 10)
for i in range(1, len(sorted_data)):
    if sorted_data[i] - sorted_data[i - 1] > 10:
        group_num += 1
    groups[sorted_data[i]] = group_num

# Присваиваем группы исходным данным в их изначальном порядке
result = [groups[num] for num in data]

print("Ответ:", result)