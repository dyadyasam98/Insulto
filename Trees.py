from Entities import InsultoTree
import random as rnd

# Мужское дерево
# Листья:
pri = InsultoTree("придурошный")
dur = InsultoTree("дурак")
tor = InsultoTree("тормоз")

glu = InsultoTree("глупый")
ned = InsultoTree("недалекий")

toop = InsultoTree("туп")
ots = InsultoTree("отсталый")

ebl = InsultoTree("еблан")
gon = InsultoTree("гондон")
dol = InsultoTree("долбоеб")

mud = InsultoTree("мудила")
pet = InsultoTree("петух")

che = InsultoTree("черт")
pid = InsultoTree("пидр")
chm = InsultoTree("чмошник")

muj = InsultoTree("Какой нахуй из тебя мужик?")
Ili = InsultoTree("Или у тебя действительно такое уебанское имя? Ахахахаха!!!")

# ветки:

Sov = InsultoTree("совсем")
Och = InsultoTree("очень")
Nem = InsultoTree("немного")

Kon = InsultoTree("конченный")
Eba = InsultoTree("ебанный")
Piz = InsultoTree("же пиздишь!")

Sov.next_words.append(pri)
Sov.next_words.append(dur)
Sov.next_words.append(tor)
Och.next_words.append(glu)
Och.next_words.append(ned)
Nem.next_words.append(toop)
Nem.next_words.append(ots)

Kon.next_words.append(mud)
Kon.next_words.append(pet)
Eba.next_words.append(che)
Eba.next_words.append(pid)
Eba.next_words.append(chm)
Piz.next_words.append(muj)
Piz.next_words.append(Ili)

# мат / не мат:
Mat = InsultoTree("")
Not_mat = InsultoTree("")



Not_mat.next_words.append(Sov)
Not_mat.next_words.append(Och)
Not_mat.next_words.append(Nem)
Mat.next_words.append(Kon)
Mat.next_words.append(Eba)
Mat.next_words.append(Piz)


# корень:

You = InsultoTree("ты")

You.next_words.append(Mat)
You.next_words.append(Not_mat)

#_____________________________________________

#Женское дерево
# Листья:
f_pri = InsultoTree("придурошная")
f_dur = InsultoTree("дура")
f_tor = InsultoTree("тормоз")

f_glu = InsultoTree("глупая")
f_ned = InsultoTree("недалекая")

f_toop = InsultoTree("туповата")
f_ots = InsultoTree("отсталая")

f_shl = InsultoTree("шлюха")
f_Pzd = InsultoTree("пизда")

f_ovc = InsultoTree("овца")
f_mrz = InsultoTree("мразь")

f_jen = InsultoTree("В зеркало смотрела? Ну и где там женщина?")
f_Ili = InsultoTree("Или тебя действительно назвали таким уебанским именем?)))")
# ветки:

f_Sov = InsultoTree("совсем")
f_Och = InsultoTree("очень")
f_Nem = InsultoTree("немного")

f_Kon = InsultoTree("конченная")
f_Eba = InsultoTree("ебанутая")
f_Piz = InsultoTree("же пиздишь!")

f_Sov.next_words.append(f_pri)
f_Sov.next_words.append(f_dur)
f_Sov.next_words.append(f_tor)
f_Och.next_words.append(f_glu)
f_Och.next_words.append(f_ned)
f_Nem.next_words.append(f_toop)
f_Nem.next_words.append(f_ots)

f_Kon.next_words.append(f_shl)
f_Kon.next_words.append(f_Pzd)
f_Eba.next_words.append(f_ovc)
f_Eba.next_words.append(f_mrz)
f_Piz.next_words.append(f_jen)
f_Piz.next_words.append(f_Ili)

# мат / не мат
f_Mat = InsultoTree("")
f_Not_mat = InsultoTree("")

f_Not_mat.next_words.append(f_Sov)
f_Not_mat.next_words.append(f_Och)
f_Not_mat.next_words.append(f_Nem)

f_Mat.next_words.append(f_Kon)
f_Mat.next_words.append(f_Eba)
f_Mat.next_words.append(f_Piz)



# корень:

f_You = InsultoTree("ты")

f_You.next_words.append(f_Not_mat)
f_You.next_words.append(f_Mat)

#_____________________________________

def print_info_words(node, i = 0):
  print("    " * i + "- " + node.word)
  for m in node.next_words:
    print_info_words(m, i + 1)

# 1. `generate_phrases(tree)` — возвращает все возможные оскорбительные фразы (пути от корня до листьев).

def generate_phrases(node, path = ''):
  phrases = []
  new_path = path + node.word + ' '
  if not node.next_words:
    phrases.append(new_path.strip())
  else:
    for child in node.next_words:
      phrases += generate_phrases(child, new_path)
  return phrases

