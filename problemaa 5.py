x=[0, 1, 2, 3, 4, 5]
y=x
print("s= suma primelor trei componente ale variabilei x este", sum(x[0:3]))
print("s1= suma tuturor componentelor variabilei y este", sum(y))
p=1
for i in range(0, len(x)):
    p=p*x[i]
    i+=1
print("p= produsul tuturor componentelor variabilei x este", p)
print("m= valoarea absoluta a componentei a treia a variabilei y este", abs(x[2]))
print("n= suma primelor componente ale variabilei x si y este", x[0]+y[0])