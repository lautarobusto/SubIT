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
linkList=[]
tituloList=[]
descripcionList=[]
subtitulos=[]
subtitulo =Subtitulo
if statusCode == 200:

    html = BeautifulSoup(r.text, 'html.parser')

    descripciones = html.find_all('div', id="buscador_detalle_sub")
    divLinks = html.find_all('div', id="buscador_detalle_sub_datos")

    for titulo in html.find_all('div', id="menu_titulo_buscador"):
        tituloList.append(titulo.find('a').text)
    for descripcion in html.find_all('div', id="buscador_detalle_sub"):
        descripcionList.append(descripcion.text)
    for link in html.find_all('a', target="new", rel="nofollow"):
        linkList.append(link.get('href'))

    for i in xrange(linkList.len):
        subtitulo.titulo = tituloList[i]
        subtitulo.descripcion = descripcionList[i]
        subtitulo.link = linkList[i]






else:
    print("Status Code %d" % statusCode)

    # <a rel="nofollow" target="new" href="http://www.subdivx.com/bajar.php?id=247551&amp;u=7"><img src="bajar_sub.gif" border="0"></a>
    # http://www.subdivx.com/bajar.php?id=7413&u=1
    # http://www.subdivx.com/bajar.php?id=7413&amp;u=1
