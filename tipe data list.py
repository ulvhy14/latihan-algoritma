t = ["Belajar", "Python", "di", "Duniailkom"]
p = [100, 200, 300, 400]
w = ["Python", 200, 6.99, True]
  
print(t)
print(p)
print(w)

v = ["Belajar", "Python", "di", "Duniailkom"]
b = [100, 200, 300, 400]
d = ["Python", 200, 6.99, True]
 
print(type(v))
print(type(b))
print(type(d))

c = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
  
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[4])
print(c[5])

k = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
print(k)
  
k[0] = 'Belajar'
k[3] = False
print(k)

y = ["Python", 200, 6.99, True, 'Duniailkom', 99j]
print(y[2:5])
print(y[:3])
print(y[3:])
print(y[:])