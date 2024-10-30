h = ("Belajar", "Python", "di", "Duniailkom")
s = (100, 200, 300, 400)
w = ("Python", 200, 6.99, True)
  
print(h)
print(s)
print(w)

y= ["Belajar", "Python", "di", "Duniailkom"]
print(type(y))
y = ("Belajar", "Python", "di", "Duniailkom")
print(type(y))

h = ("Python", 200, 6.99, True, 'Duniailkom', 99j)
  
print(h[0])
print(h[1])
print(h[2])
print(h[2:5])
print(h[:3])
print(h[3:])
print(h[:])

b = ("Python", 200, 6.99, True, 'Duniailkom', 99j)
b[0] = 'Belajar'
print(b)