g=[6, 7, 7, 8, 9, 11, 12, 12, 13, 14, 15, 15, 15, 16, 15, 15, 14, 14, 13, 13, 12, 11, 11, 9]
o=[24, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
x=max(g)
a=g.index(x)
y=min(g)
b=g.index(y)
print("temp med este=", sum(g)/24)
print("maximul temp este=", max(g))
print("minimul temp este=", min(g))
print("temp maxima", o[a])
print("temp minima", o[b])