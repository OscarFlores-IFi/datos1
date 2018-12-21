import matplotlib.pyplot as plt

#nombre = input("nombre del archivo.")
nombre = "terrenos tlajomulco"
doc = (open(("C:\\Users\\Oscar Flores\\Desktop\\" + nombre + ".csv"), 'r'))
lines = [line for line in doc]
precio = []
tamaño = []
for i in lines:
    a = i.split(",")
    precio.append(a[1])
    tamaño.append(a[2])
precio.pop(0)
tamaño.pop(0)


plt.scatter(tamaño,precio,s=5,marker = "o",color = "b")
plt.show()
