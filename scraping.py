print('Start van de scraping applicatie')

from bs4 import BeautifulSoup
import requests

pagina = requests.get('https://www.bitcoinmeester.nl/')

heeldehtml = BeautifulSoup(pagina.content, 'html.parser')
tabel = heeldehtml.find('div')

# print(tabel.prettify())

bitcoinprijs = heeldehtml.find(id = "price1")

print(bitcoinprijs.prettify())
