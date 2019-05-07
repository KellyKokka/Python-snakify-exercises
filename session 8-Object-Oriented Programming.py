#Session_8
#Advanced Counter Class

class Counter:
    def __init__(self, my_id):
        self._items =0
        self._id = my_id
        self.dictio={}
        self.amount=0
        self.price_of_unit=0.00
        self.totalvalue=0
    def add(self, item_name, amount, price_of_unit):
        self.dictio[item_name]=[amount,price_of_unit]
        self.amount+=amount
        self.totalvalue=round(self.totalvalue+amount*price_of_unit,2)
    def remove(self, item_name, amount):
        if item_name not in self.dictio.keys():
            pass
        elif item_name in self.dictio.keys() and self.amount>=amount:
            self.amount-=amount
            self.totalvalue-=self.dictio[item_name][1]
    def reset(self):
        self.dictio={}
        self.amount=0
        self.totalvalue=0
    def get_total(self):
        return self.totalvalue
    def status_print(self):
        print(self._id+" "+str(self.amount)+" "+str(self.totalvalue))

#NO modifications modify below this line
c = Counter("C001")
c.add("Spaghetti", 5, 1.8)
c.status_print()
c.add("Ice Cream", 2, 3.4)
c.status_print()
print(c.get_total())
c.add("Spaghetti", 3, 1.8)
c.status_print()
c.remove("Ice Cream", 1)
c.status_print()
c.reset()
c.add("Coke", 5, 1.45)
c.status_print()

#Circular Sector Class

class Sector:
    def __init__(self):
        self.fr = 0
        self.to = 0
        self.rad = 0
    def rotate(self, angle):
        #implement this
        #rotates sector by angle
        #you man assume the rotation never results in a sector with fr > to
        #(it is optional to solve this problem without this assumption; see above)
        self.fr+=angle
        self.to+=angle
    def intersect(self, other):
        #implement this
        #returns sector that is intersection of this and other sector
        #you may assume that the two sectors have nonempty intersection
        return str(other.fr)+" "+str(self.to)+" "+str(other.rad)
    def is_empty(self):
        #implement this
        #returns True if the sector has empty area, otherwise False
        if self.fr==self.to or self.rad==0:
            return True
        else:
            return False
    def __eq__(self, other):
        #implement this
        #returns True this sector is the same as the other, otherwise False
        if self.fr==other.fr and self.to==other.to and self.rad==other.rad:
            return True
        else:
            return False
    def __str__(self):
        #implement this
        #returns string "F T R" where F is from angle, T is to, and R is radius
        s=str(self.fr)+" "+str(self.to)+" "+str(self.rad)
        return s

#NO modications below this line
s1 = Sector()
s1.fr = 0
s1.to = 20
s1.rad = 40
print(s1)
s1.rotate(50)
print(s1)
s2 = Sector()
s2.fr = 50
s2.to = 80
s2.rad = 40
print(s1==s2)
s2.fr = 60
s2.to = 100
s2.rad = 30
s3 = s1.intersect(s2)
print(s3)
