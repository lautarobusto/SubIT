from bs4 import BeautifulSoup
import requests
import Subtitulo

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
subtitulos = []

if statusCode == 200:

    html = BeautifulSoup(r.text, 'html.parser')

    for titulo in html.find_all('div', id="menu_titulo_buscador"):
        tituloList.append(titulo.find('a').text)
    for descripcion in html.find_all('div', id="buscador_detalle_sub"):
        descripcionList.append(descripcion.text)
    for link in html.find_all('a', target="new", rel="nofollow"):
        linkList.append(link.get('href'))


     ##Si esto funciona porque al meterlo dentro de  un for, todos los objetos tienen el mismo contenido?
    sub=Subtitulo
    sub.titulo=tituloList[0]
    sub.descripcion=descripcionList[0]
    sub.link=linkList=linkList[0]
    subtitulos.append(sub)

    print(subtitulos[0].titulo)
    print(subtitulos[0].descripcion)
    print(subtitulos[0].link)


    #for index in range(0, len(linkList)):
       # sub = Subtitulo

       # sub.titulo = tituloList[index]
       # sub.descripcion = descripcionList[index]
       # sub.link = linkList[index]
       # subtitulos.append(sub)

else:

    print("Status Code %d" % statusCode)
