class Stack:
  def __init__(self):
    self.__list = []

  def __str__(self):
    return '--->'.join(map(str, self.__list))

  def push(self, element):
    self.__list.append(element)
    return True

  def pop(self):
    if self.is_empty():
      return "No hay elementos en pila"
    return self.__list.pop()

  def top(self):
    if self.is_empty():
      return "No hay elementos en pila"
    return self.__list[-1]

  def len(self):
    return len(self.__list)

  def is_empty(self):
    return len(self.__list) == 0