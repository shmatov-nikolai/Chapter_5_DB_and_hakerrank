import random

num_test = int(input("Введите количество тестов: "))
listok = ','.join(input("Введите слово для преобразования: ")).split(',')
stroka = ''.join(listok)
low_list = []
high_list = []
for i in stroka:
    if i == (i).lower():
        low_list.append(i)
    else:
        high_list.append(i)
 
print(f"В данном слове: '{stroka}', состоит из: \n{len(low_list)} строчных букв \n{len(high_list)} заглавных букв")

j = 0 
while j < num_test:
    random__num = random.randint(0, len(low_list))
    j_ = 0
    stroka_new = stroka
    print(f"рандомное количество строчных букв в слове для преобразования {random__num}")
    while j_ < random__num:
        random_choice = random.choice(low_list)
        
        for letter in stroka_new:
            if letter == random_choice:
                stroka_new = stroka_new.replace(letter, letter.upper(), 1)
                j_+=1
                break
    c = 0
    p=0
    j+=1
    stroka_new = ','.join(stroka_new).split(',')
    while p < (len(low_list)-random__num):
        for letter in stroka_new:
            if letter in low_list:
                stroka_new.remove(letter)
                c += 1
                p += 1
                break
    if c == 0:
        print('False')
    else:
        print(''.join(stroka_new))   