# Pro inicio do projeto instalar
# pip install beautifulsoup4

from bs4 import BeautifulSoup
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

def clima(cidade):
    cidade = cidade.replace(" ", "+")
    res = requests.get(f'https://www.google.com/search?q={cidade}&oq={cidade}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8',headers=headers)
    print("Procurando sua cidade........\n")
    # Aqui o soup vai puxar a localização, horário, informações e clima do google que foi o link acima que puxa uma requisição HTTP GET (pra pegar as informações)
    soup = BeautifulSoup(res.text, 'html.parser')
    localizacao = soup.select('#wob_loc')[0].getText().strip()
    horario = soup.select('#wob_dts')[0].getText().strip()
    informacoes = soup.select('#wob_dc')[0].getText().strip()
    clima = soup.select('#wob_tm')[0].getText().strip()
    print(localizacao)
    print(horario)
    print(informacoes)
    print(clima+ "ºC") # ou ºF ou Kelvin se vc quiser vai que

cidade = input("Digita o nome de Qualquer Cidade ->  ")
cidade = cidade + "clima"
clima(cidade)

