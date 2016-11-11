from bs4 import BeautifulSoup
import requests
from Subtitulo import Subtitulo

# url de subdivx con una buscqueda ingresada en el campo de busqueda de subdivx
url = "http://www.subdivx.com/index.php?buscar=ironman&accion=5&masdesc=&subtitulos=1&realiza_b=1"
url2 = "http://docs.python-requests.org/en/master/user/quickstart/#make-a-request"
url3 = "http://www.subdivx.com/index.php?buscar=game+of+thrones+s06e01&accion=5&masdesc=&subtitulos=1&realiza_b=1"

# Realizamos la petición a la web
r = requests.get(url3)
statusCode = r.status_code
linkList = []
tituloList = []
descripcionList = []
descargaList = []
subtitulos = []

if statusCode == 200:

    html = BeautifulSoup(r.text, 'html.parser')

    # Checkeo si hay mas paginas y obtengo enlace de la proxima si existe
    pag = html.find('div', {"class": "pagination"})
    if len(pag) > 0:
        print("tiene mas paginas")
    else:
        print("no tiene una mierda")

    # obtengo Titulo, descripcion, descargas y enlaces por cada subtitulo y lo almaceno en una lista de objetos Subtitulo
    for titulo in html.find_all('div', id="menu_titulo_buscador"):
        tituloList.append(titulo.find('a').text)
    for descripcion in html.find_all('div', id="buscador_detalle_sub"):
        descripcionList.append(descripcion.text)
    for link in html.find_all('a', target="new", rel="nofollow"):
        linkList.append(link.get('href'))

    for descarga in html.find_all('div', id="buscador_detalle_sub_datos"):
        descargaList.append(descarga.text)

    for i in range(len(tituloList)):
        x = Subtitulo(tituloList[i], descripcionList[i], descargaList[i], linkList[i])

        subtitulos.append(x)

    for subs in subtitulos:
        print(
            "Titulo:" + subs.titulo + "\n" + "Descargas:" + subs.descargas + "\n" + "Descripcion:" + subs.descripcion + "\n" + "Enlace:" + subs.link)






else:

    print("Status Code %d" % statusCode)
