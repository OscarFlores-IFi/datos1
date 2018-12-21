import matplotlib.pyplot as plt

nombre = "tlajomulco_de_zuniga"
doc1 = (open(("C:\\Users\\Oscar Flores\\Desktop\\" + nombre + ".csv"), 'r'))
lines = [line for line in doc1]
precio = []
tamaño = []
#nombre = "terrenos tlajomulco"
#doc2 = (open(("C:\\Users\\Oscar Flores\\Desktop\\" + nombre + ".csv"), 'r'))
for i in lines:
    a = i.split(",")
    try:
        if int(a[1]) < 8000000:
            if int(a[1]) > 500000:
                precio.append(a[1])
                tamaño.append(a[2])
    except:
        print("")
print(precio,"\n",tamaño)

plt.scatter(tamaño,precio,s=5)
plt.show()





