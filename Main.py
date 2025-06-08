from Trees import generate_phrases
from Trees import print_info_words
from Trees import You
from Trees import f_You
from Trees import f_Not_mat
from Trees import f_Mat
from Trees import Not_mat
from Trees import Mat


import random as rnd
f = generate_phrases(f_You)
f_not_mat = generate_phrases(f_Not_mat)
f_mat = generate_phrases(f_Mat)
not_m = generate_phrases(Not_mat)
m = generate_phrases(Mat)
no_matter = generate_phrases(You)

def name_phrase(name, sex, mat_or_not):
  random_index = rnd.randint(0, len(m)-1)
  if sex == 'мужской':
    if mat_or_not == True:
      return f'{name}, ты {m[random_index]}'
    elif mat_or_not == False:
      return f'{name}, ты {not_m[random_index % len(not_m) - 1]}'
    else:
      return f'{name}, {no_matter[random_index % len(no_matter) - 1]}'
  elif sex == 'женский':
    if mat_or_not == True:
      return f'{name}, ты {f_mat[random_index % len(f_mat) - 1]}'
    elif mat_or_not == False:
      return f'{name}, ты {f_not_mat[random_index % len(f_not_mat) - 1]}'
    else:
      return f'{name}, {f[random_index % len(f) - 1]}'
  else:
    return 'Езжай в Америку'



def read_insalto(the_file):
    try:
        file_to_read = open(str(the_file), 'r')
        lines = file_to_read.readlines()
        for line in lines:
            print(line)
    except FileNotFoundError:
        print("Ошибка! Что-то пошло не так.")

logs = open('logs.txt', 'a')

def generate_insalto(number, user_name, user_sex, are_you_ready):
    insultion = name_phrase(user_name, user_sex, are_you_ready)
    logs.write(f'{number}. Name: {user_name}, Sex: {user_sex}, {insultion}')
    logs.write('\n')

start_prog = input('Введите /generate_insulto, если схотите сгенерировать оскорбления. Или введите /print_all_insulto, если хотите увидеть уже имеющиеся оскорбления: ')
if start_prog == '/generate_insulto':
    r = input("Если вы поддерживаете использование мата, то введите: похуй, в противном случае введите: Экскьюзми")
    number = 0
    while True:
        number += 1
        user_name = input('Введите имя: ')
        if user_name == "стоп":
            print("Завершение работы программы по запросу пользователя.")
            break
        user_sex = input('Введите пол: ')
        if r == "похуй":
            insultion = generate_insalto(number, user_name, user_sex, True)
        else:
            insultion = generate_insalto(number, user_name, user_sex, False)
elif start_prog == '/print_all_insulto':
   read_insalto(logs)