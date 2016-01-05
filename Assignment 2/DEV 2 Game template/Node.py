from random import randint
from random import uniform

class Empty: 
    def __init__(self):
        self.IsEmpty = True

    def __str__(self):
        return "[]"

    def length(self):
        return 0

    def index(self, index):
        return Empty

    def map(self, f):
        return Empty

    def filter(self, p):
        return Empty

    def fold(self, f, z):
        return 0

Empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.Tail = tail
        self.Value = value
        self.IsEmpty = False

    def __str__(self):
        return str(self.Value) + "; " + str(self.Tail);

    def map(self, f):
        return Node(f(self.Value), self.Tail.map(f))

    def filter(self, p):
        if p(self.Value):
            return Node(self.Value, self.Tail.filter(p))
        else:
            return self.Tail.filter(p)

    def fold(self, f, z = 0):
       return f(self.Value, self.Tail.fold(f, z))

    def length(self):
        return 1 + self.Tail.length()

    def random(self, return_index = False):
        i = randint(0, self.length()-1)

        if return_index:
            return i

        return self.index(i)

    def index(self, index):
        if index == 0:
            return Node(self.Value, Empty)
        else:
            return self.Tail.index(index-1)

def AUX_length(l, acc):
  if l.IsEmpty: return acc
  else: return AUX_length(l.Tail, acc + 1)

def length(l):
  return AUX_length(l, 0)

def select_one_random(l):
  _length = length(l)
  rnd_num = int(uniform(0, _length ))
  while(rnd_num > 0):
    l = l.Tail
    rnd_num -= 1
  return l.Value