"""
frecv = 1/T = 2000Hz
a. T = 1/2000 = 0.0005 (timpul intre 2 esantioane)
b. 1 ora = 60 minute = 3600 secunde
1 sec .... 2000 de masuratori
3600 sec .. 3600 * 2000 = 7200000 masuratori
1 masuratoare ... 4 biti
7200000 masuratori ... 4*7200000 = 28800000 biti = 3600000 bytes
"""

frecv = 2000
t = 1/frecv
print("Timpul intre 2 esantionari este ", t, ".")

samples = 3600 * frecv
bytes = samples/2
print("Este nevoie de ", bytes, "bytes pentru a retine datele de la o ora de achizitie.")