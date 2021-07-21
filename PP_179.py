pro_num = list(map(int, input("Введите целые числа через пробел").split()))
cel_num = int(input("Введите целое число"))

def check():
    while type:
        try:
            pro_num
            if len(pro_num)==0:
                raise ValueError
        except ValueError:
            print("Некорректный ввод данных")
        else:
            break
check()

def sort():
    for i in range(len(pro_num)):
        for j in range(len(pro_num) - i - 1):
            if pro_num[j] > pro_num[j + 1]:
                pro_num[j], pro_num[j + 1] = pro_num[j + 1], pro_num[j]
    return pro_num

sort()
sp = []

for idx, val in enumerate(pro_num):
    sp.append(idx)
left = sp[0]
right = sp[-1]

def binary_search(pro_num, cel_num, left, right):
    while left < right:
        middle = (left + right) // 2
        if pro_num[middle] < cel_num:
            left = middle + 1
        else:
            right = middle
        if left > 0 and pro_num[left] != cel_num:
            c=(pro_num[left - 1])
        else:
            c=(pro_num[left])
    return print(c)
(binary_search(pro_num, cel_num, left, right))
