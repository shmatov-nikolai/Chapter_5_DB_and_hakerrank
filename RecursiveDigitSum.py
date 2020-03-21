"""13)Recursive digit sum:
https://www.hackerrank.com/challenges/recursive-digit-sum/problem
"""

def recurs(str_list):
    list_2 = []
    for i in str(str_list):
        list_2.append(int(i))
    if len(list_2) == 1:
        print(f"Результат преобразования: {str_list}")
    else:
        return str(recurs(sum(list_2)))

num = input("Введите число для преобразования: ")
num2= int(input("Введите число множитель: "))
list_1 = []
list_1.append(num)
str_list = ', '.join(list_1) * num2  


recurs(str_list)    