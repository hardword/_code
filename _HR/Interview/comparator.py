#!/bin/python
# http://hr.gs/16xx

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def __repr__(self):
        return "("+self.name+","+str(self.score)+")"
    def comparator(p1, p2):
        cmp = p2.score - p1.score
        if cmp == 0:
            if p1.name > p2.name:
                cmp = 1
            else:
                cmp = -1
        return cmp

#p1 = Player('amy', 100)
p2 = Player('amy', 100)
#p2 = Player('david', 100)
p1 = Player('david', 100)
p3 = Player('heraldo', 50)
p4 = Player('aakansha', 75)
p5 = Player('aleksa', 150)

data = []
data.append(p1)
data.append(p2)
data.append(p3)
data.append(p4)
data.append(p5)

print sorted(data, cmp=Player.comparator)