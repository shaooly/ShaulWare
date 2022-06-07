list1 = []
for i in range(1000):
    list1.append(i + 1)
min_num = list1[0]
index = 0  # מייצג את המיקום של המספר הכי קטן
x = 0  # מייצג את המספר הראשון ברשימה
for i in range(len(list1)):
    min_num = list1[i]
    for j in range(i, len(list1)):
        if list1[j] < min_num:
            min_num = list1[j]
            index = j
    x = list1[i]
    list1[i] = min_num
    list1[index] = x
print(list1)
