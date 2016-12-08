class Node:
  def __init__(self, value, tail):
    self.tail = tail
    self.value = value
    self.isEmpty=False

  def RemoveTail(self):
        self.tail=None