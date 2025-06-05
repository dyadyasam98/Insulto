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

def name_phrase(name, sex):
  random_index = rnd.randint(0, len(m)-1)
  if sex == 'мужской':
    mat_or_not = input('Приветствуете ли вы ненормативную лексику? (Введите да, нет или без разницы): ')
    if mat_or_not == "да":
      return f'{name}, ты {m[random_index]}'
    elif mat_or_not == "нет":
      return f'{name}, ты {not_m[random_index % len(not_m) - 1]}'
    else:
      return f'{name}, {no_matter[random_index % len(no_matter) - 1]}'
  elif sex == 'женский':
    mat_or_not = input('Приветствуете ли вы ненормативную лексику? (Введите да, нет или без разницы): ')
    if mat_or_not == "да":
      return f'{name}, ты {f_mat[random_index % len(f_mat) - 1]}'
    elif mat_or_not == "нет":
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
    except:
        print("Ошибка! Что-то пошло не так.")

logs = open('logs.txt', 'a')

print('Для прекращения работы программы в строке ввода имени введите "стоп"')
number = 0
while True:
  number += 1
  user_name = input('Введите имя: ')
  if user_name == 'стоп':
    print('Завершение работы программы по запросу пользователя.')
    logs.close()
    break
  elif user_name == "инфо":
    read_insalto('logs.txt')
    break
  user_sex = input('Введите пол: ')
  insultion = name_phrase(user_name, user_sex)
  print(insultion)

  logs.write(f'{number}. Name: {user_name}, Sex: {user_sex}, {insultion}')
  logs.write('\n')

