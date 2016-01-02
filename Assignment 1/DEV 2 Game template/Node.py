from random import randint

class Empty: 
  def __init__(self):
    self.IsEmpty = True

Empty = Empty()

class Node:
    def __init__(self, value, tail):
        self.Tail = tail
        self.Value = value
        self.IsEmpty = False

    def output(self):
        map(self, lambda l: print(l))

    def length(self):
        return fold(self, lambda x, y: y + 1)

    def index(self, index):
        index = abs(index - self.length())
        return Node(filter2(self, lambda l: l.length() == index).Value.Value, Empty)

    def random(self):
        return self.index(randint(1, self.length()) - 1)

def map(l, f):
    if l is Empty:
        return Empty
    else:
        return Node(f(l.Value), map(l.Tail , f))

def filter(l, p):
    if l is Empty:
        return Empty
    else:
        if p(l.Value):
            return Node(l.Value, filter(l.Tail, p))
        else:
            return filter(l.Tail, p)

def filter2(l, p):
    if l is Empty:
        return Empty
    else:
        if p(l):
            return Node(l, filter2(l.Tail, p))
        else:
            return filter2(l.Tail, p)

def fold(l, f, z = 0):
    if l is Empty:
        return z
    else:
        return f(l.Value, fold(l.Tail, f, z))