h = { 1: "Belajar", 2: "Python", 3: "di Duniailkom" }
g = { "mengapa": "Belajar", "apa": "Python", "dimana": "di Duniailkom" }
p = { 1: "Belajar", "apa": "Python", "dimana": "di Duniailkom" }
 
print(type(h))
print(type(g))
print(type(p))
 
print(h)
print(g)
print(p)

i = { 1: "Belajar", 
        2: ["Pascal", "C", "Python"],
        "website": "Duniailkom",
        "menyerah" : False,
        "target": 2020,
        "riwayat_sekolah": {
          "SD": "SDN 3 Hijau Daun",
          "SMP": "SMP 7 Hijau Lumut",
          "SMA": "SMA 8 Hijau Rumput"}
      }
       
print(i)

p = { "kegiatan": "Belajar Python",
        "website": "Duniailkom",
        "hasil": "Yakin bisa!" }
 
print(p["website"])

t = { "kegiatan": "Belajar Python",
        "website": "Duniailkom",
        "hasil": "Yakin bisa!" }
 
t["kegiatan"] = "Belajar Bahasa Pemrograman"
print(t)

g = { "kegiatan": "Belajar Python",
        "website": "Duniailkom",
        "hasil": "Yakin bisa!" }
 
g["target"] = 2020
print(g)

t = { "kegiatan": "Belajar Python",
        "website": "Duniailkom",
        "hasil": "Yakin bisa!" }
 
del t["kegiatan"]
print(t)

p = dict ( kegiatan = "Belajar Python",
             website = "Duniailkom",
             hasil = "Yakin bisa!" )
              
print(p)