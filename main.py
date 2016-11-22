from bs4 import BeautifulSoup
import requests
from Subtitulo import Subtitulo
import re
import codecs
import urllib.request, shutil, rarfile

def getsubs(url):
    linkList = []
    tituloList = []
    descripcionList = []
    descargaList = []
    subtitulos = []
    cantP = []
    nextList = []
    hasnext = True
    cant = 0

    while hasnext is True:

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
                wordList = re.sub("[^0-9,]", " ", descarga.text).split()
                descargaList.append(wordList[0])

            for i in range(len(tituloList)):
                x = Subtitulo(tituloList[i], descripcionList[i], descargaList[i], linkList[i])

                subtitulos.append(x)
        else:

            print("Status Code %d" % statusCode)
    return subtitulos


def geturl(title, season, chapter):
    title = "+".join(title.split())

    if len(season) == 0 | len(chapter) == 0:

        url = "http://www.subdivx.com/index.php?accion=5&masdesc=&buscar=" + title + "&oxdown=1"
    else:

        url = "http://www.subdivx.com/index.php?accion=5&buscar=" + title + "+s" + season + "e" + chapter + "&oxdown=1"
    return url


def saveresultfile(subtitulos):

    f = codecs.open('file.txt', 'w', "utf-8")
    for subs in subtitulos:
        f.write("--------------------------------------------------------------------------------------------------------------------------------------------\n")
        f.write("Titulo:" + subs.titulo + "\n" + "Descargas:" + subs.descargas + "\n" + "Descripcion:" +
                subs.descripcion + "\n" + "Enlace:" + subs.link + "\n")


def download_rar(url):
    file_name = 'myzip.rar'

    with urllib.request.urlopen(url) as response, open(file_name, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)


