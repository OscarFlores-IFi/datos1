# SCRAPPING DE WWW.CASASYTERRENOS.COM ÚNICAMENTE PARA TERRENOS EN VENTA.

from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from time import sleep
from multiprocessing import pool

def get_soup(link_principal, link_secundario, iterador):
    #función para conseguir el html de la pagina web
    html = urlopen(link_principal + link_secundario + str(iterador))  # + str(iterador))
    site = html.read()
    soup = bs(site, 'html.parser')
    return soup
def sacar_datos_terrenos(soup, lista):
    if len(lista) == 0:
        lista = "ubicación,precio,tamaño,precio por metro, link\n"
    propiedades = (soup.find_all('div', class_="listado-propiedad"))
    #saca: ubicación, precio total, metros del terreno, link
    for i in propiedades:
        ubicacion = i.find('h2').get_text()  # ubicación de la casa
        precio = i.find('h5').get_text()  # precio de la casa
        p_real = int("".join((str(precio)[1:-4]).split(",")))
        tamaño = i.find('h3').get_text() # metros cuadrados de la casa
        tam = [line.strip() for line in tamaño.splitlines()]
        tam = (l for l in tam if l != '')
        tamaño = "".join(tam)
        tamaño = tamaño[:-3]
        if len(str((("".join(str(tamaño).split(",")))))) > 0:
            t_real = int((("".join(str(tamaño).split(",")))))
        else:
            t_real = 1
        hipervinculo = link_principal + str(i.find('a').get('href'))  # link_principal de la propiedad
        p_por_m = round(p_real/t_real,2)
        lista = lista + str(ubicacion) + "," + str(p_real) + "," + str(t_real) + "," + str(p_por_m) + "," + hipervinculo + "\n"
    return lista
def sacar_datos_casas(soup, lista):
    if len(lista) == 0:
        lista = "ubicación,precio,tamaño,habitaciones,baños,estacionamientos,link\n"
    propiedades = (soup.find_all('div', class_="listado-propiedad"))
    for i in propiedades:
        ubicacion = i.find('h2').get_text()  # ubicación de la casa
        precio = i.find('h5').get_text()  # precio de la casa
        precio = int("".join((str(precio)[1:-4]).split(",")))
        try:
            tamaño = i.find('span', class_="amenidad").get_text() # metros cuadrados de la casa
            tam = [line.strip() for line in tamaño.splitlines()]
            tam = (l for l in tam if l != '')
            tamaño = "".join(("".join(tam)).split(","))
            tamaño = tamaño[:-3]
        except:
            tamaño = 1

        try:
            habitaciones = (i.find('img', title='habitaciones').parent).get_text()
        except:
            habitaciones = 0
        try:
            baños = (i.find('img', title='Baños').parent).get_text()
        except:
            baños = 0
        try:
            estacionamientos = (i.find('img', title='Estacionamientos').parent).get_text()
        except:
            estacionamientos = 0
        hipervinculo = link_principal + str(i.find('a').get('href'))  # link_principal de la propiedad
        lista = lista + str(ubicacion) + "," + str(precio) + "," + str(tamaño) + "," + str(habitaciones) + "," + str(baños) + "," + str(estacionamientos) + "," + hipervinculo + "\n"
    return lista
def repeticiones(soup):
    try:
        repeticiones = int((soup.find('span', id='cantidad-resultados')).get_text())
        if repeticiones % 10 == 0:
            repeticiones = repeticiones // 10
        else:
            repeticiones = (repeticiones // 10) + 1
        rep = input("ITERACIONES (si se desean todas teclear \"t\", sino teclear el número de iteraciones deseadas): ")
        if rep != "t":
            repeticiones = int(rep)
    except:
        repeticiones = int(input("repeticiones deseadas: "))
    return repeticiones
def guardar_archivo(lista):
    nombre = input("nombre de archivo: ")
    doc = (open(("C:\\Users\\Oscar Flores\\Desktop\\" + nombre + ".csv"), 'w'))
    doc.writelines(lista)
    doc.close()




link_principal = "http://www.casasyterrenos.com"
#link_secundario = input("link secundario: ")
link_secundario = "/jalisco/tlajomulco+de+zuniga/nueva+galicia/casas/venta/"
lista = ""

for iterador in range(1,repeticiones(get_soup(link_principal, link_secundario, 1)) + 1):
    soup = get_soup(link_principal, link_secundario, iterador)
    if "terrenos" in link_secundario:
        lista = sacar_datos_terrenos(soup, lista)
    elif "casas" in link_secundario:
        lista = sacar_datos_casas(soup, lista)
    sleep(1)
print(lista)
if input("guardar archivo? (s,n)") == "s":
    guardar_archivo(lista)
