from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://alertario.rio.rj.gov.br/upload/MaioresChuvas.html'

response = urlopen(url)
html = response.read()
soup = BeautifulSoup(html, 'html.parser')

# Preparando os dados
for i in range(0, 30, 3):
  print (i)

titulos = []
for i in range (2, 6):
  titulos.append(i)
  
registros = {}
datas = {}
horas = {}

titulos = soup.findAll('th')
titulos1 = []
for titulo in titulos:
  titulos1.append(titulo.getText())

dados = soup.findAll('td')
dados1 = []
for dado in dados:
  dados1.append(dado.getText())

dados = soup.findAll('td')
bruto = []
for dado in dados:
  bruto.append(dado.getText())
  
# Primeira Tabela
local = []
for i in range (1, 50, 5):
  local.append(bruto[i])

registro = []
for i in range (2, 50, 5):
  registro.append(bruto[i])

dia = []
for i in range (3, 50, 5):
  dia.append(bruto[i])

hora = []
for i in range (4, 50, 5):
  hora.append(bruto[i])

tabela1 = []
tabela1 = pd.DataFrame(tabela1)
tabela1['coluna1'] = local
tabela1['coluna2'] = registro
tabela1['coluna3'] = dia
tabela1['coluna4'] = hora
tabela1.columns = [titulos1[2], titulos1[3], titulos1[4], titulos1[5]]

# Segunda Tabela
local = []
for i in range (51, 100, 5):
  local.append(bruto[i])

registro = []
for i in range (52, 100, 5):
  registro.append(bruto[i])

dia = []
for i in range (53, 100, 5):
  dia.append(bruto[i])

hora = []
for i in range (54, 100, 5):
  hora.append(bruto[i])

tabela2 = []
tabela2 = pd.DataFrame(tabela1)
tabela2['coluna1'] = local
tabela2['coluna2'] = registro
tabela2['coluna3'] = dia
tabela2['coluna4'] = hora
tabela2.columns = [titulos1[8], titulos1[9], titulos1[10], titulos1[11]]
