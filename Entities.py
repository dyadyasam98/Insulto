class InsultoTree:
  def __init__(self, word):
    self.__word = word
    self.__next_words = []

  @property
  def word(self):
    return self.__word
  @word.setter
  def word(self, word):
    self.__word = word

  @property
  def next_words(self):
    return self.__next_words
  @next_words.setter
  def next_words(self, next_words):
    self.__next_words = next_words


