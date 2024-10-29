from bs4 import BeautifulSoup
import requests
import nltk
from nltk.probability import FreqDist

url = 'https://www.pecaditos.com.br/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print("Titulo:", soup.title.string)
dados1 = soup.title.string

meta_description = soup.find('meta', attrs={'name': 'description'})
if meta_description:
    print("Descrição Meta", meta_description['content'])


nltk.download('punkt_tab')
dados_do_site = str(soup.get_text()) # TEM QUE ARRUMAR UMA FORMA DE JOGAR O RESULTADO DA PARTE DE CIMA AQUI !!

palavras = nltk.word_tokenize(dados_do_site)
frequencia = FreqDist(palavras)

print(frequencia.most_common(10))