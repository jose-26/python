#Conjuntos
c1=set()
c1.add(1)
c1.add(4)
c1.add(5)
c2=c1.copy()
c3=c1.copy()
c3.add(9)
c3.add(54)
c3.add(11)
c3.add(12)
c2.add(7)
c2.add(41)
c2.add(31)
print(c1)
print(c2)
print(c3)
#Borra valor
c2.discard(7)
#Borra entero
c3.clear()
print(c2)
print(c3)
#union
print(c1.union(c2))
