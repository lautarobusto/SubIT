from bs4 import BeautifulSoup
import requests
from Subtitulo import Subtitulo
import re

# url de subdivx con una buscqueda ingresada en el campo de busqueda de subdivx
url = "http://www.subdivx.com/index.php?buscar=ironman&accion=5&masdesc=&subtitulos=1&realiza_b=1"

linkList = []
tituloList = []
descripcionList = []
descargaList = []
subtitulos = []
cantP = []
nextList = []
hasnext = True
cant = 0

while hasnext == True:

    r = requests.get(url)
    statusCode = r.status_code
    if statusCode == 200:

        html = BeautifulSoup(r.text, 'html.parser')

        # Checkeo si hay mas paginas y obtengo enlace de la proxima si existe
        pag = html.find('div', {"class": "pagination"})
        # print(type(pag))

        if len(pag) > 0:
            current = pag.find('span', {"class": "current"}).text

            # con esto obtengo la cantidad de paginas que me devolvio la consulta inicial
            for a in pag.find_all('a'):
                cantP.append(a.text)
                nextList.append("http://www.subdivx.com/" + a.get("href"))
            if cant == 0:
                cant = cantP[-2]
            url = nextList[-1]

            if int(current) == int(cant):
                hasnext = False

        else:

            hasnext = False

        # obtengo Titulo, descripcion, descargas y enlaces por cada subtitulo y lo almaceno en una lista de objetos Subtitulo
        for titulo in html.find_all('div', id="menu_titulo_buscador"):
            tituloList.append(titulo.find('a').text)
        for descripcion in html.find_all('div', id="buscador_detalle_sub"):
            descripcionList.append(descripcion.text)
        for link in html.find_all('a', target="new", rel="nofollow"):
            linkList.append(link.get('href'))

        for descarga in html.find_all('div', id="buscador_detalle_sub_datos"):
            wordList = re.sub("[^0-9\\,]", " ", descarga.text).split()
            descargaList.append(wordList[0])

        for i in range(len(tituloList)):
            x = Subtitulo(tituloList[i], descripcionList[i], descargaList[i], linkList[i])

            subtitulos.append(x)








    else:

        print("Status Code %d" % statusCode)
f = open('file.txt', 'w')

for subs in subtitulos:
    f.write(
        "--------------------------------------------------------------------------------------------------------------------------------------------\n")
    f.write("Titulo:" + subs.titulo + "\n" + "Descargas:" + subs.descargas + "\n" + "Descripcion:" + str(
        subs.descripcion.encode('utf8')) + "\n" + "Enlace:" + subs.link + "\n")
