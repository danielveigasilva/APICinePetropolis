import requests
from bs4 import BeautifulSoup

def cinemaxx(pagina):
    CinePag = BeautifulSoup(pagina.content, 'html.parser')
    listaFilmes = CinePag.find('li', id ='aba1')
    filmeInfo = listaFilmes.find_all('div', id ='progr')

    for Info in filmeInfo:
        print(Info.get_text())
        print("-------------------------------")



paginas = []

paginas.append(requests.get("http://www.cinemaxx.com.br/index2.php?x=petro1"))
paginas.append(requests.get("http://www.cinemaxx.com.br/index2.php?x=petro2"))

cinemaxx(paginas[0])

