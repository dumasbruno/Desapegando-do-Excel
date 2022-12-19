# Desapegando do Excel

Olá pessoal!
- A ideia deste repositório é compartilhar alguns códigos que estão me ajudando a desapegar do Excel, espero que te ajude também! São mais de 15 anos de Curso Técnico, Gradução e Mestrado em Meteorologia e mais de 10 anos trabalhando com Meteorologia Operacional, então dá pra imaginar a quantidade de planilhas de Excel que já precisei elaborar e alimentar.

## Vossa Excelência, o dado observado!
- Começo hoje com a manipulação dos dados das estações automáticas de superfície do **Instituto Nacional de Meteorologia (INMET).**
- Na Meteorologia, **extrair informações dos dados observados é fundamental** na **interpretação das condições de tempo presente** e na **validação de modelos de previsão do tempo** de curto, médio e longo prazo, além é claro da construção de um banco de dados meteorológicos que nos permita **conhecer as características do clima de uma região** (falarei mais de tempo e clima no próximo texto, sobre visualização e interpretação dos dados).

O site do INMET permite o download dos dados históricos de suas estações automáticas de 2000 até o ano presente (https://portal.inmet.gov.br/dadoshistoricos). O link das pastas zipadas com os dados de cada ano é do tipo "dadoshistoricos/'ano'.zip", assim, o primeiro passo em "dadosbrutos_INMET" é importar os módulos os e zipfile para:

  - criar/apagar diretórios e baixar arquivos do site do INMET com o pacote os;
  - extrair arquivos zipados com o pacote zipfile.

#definindo o periodo dos dados
#nesse caso, dados entre 2000 e 2022
periodo = []
for ano in range (2000, 2023):
  periodo.append(ano)
 
for i in periodo:
  arquivo = [f'https://portal.inmet.gov.br/uploads/dadoshistoricos/{i}.zip']
  for i,j in zip(periodo, arquivo):
    download = os.system(f'wget -o {i}.zip {j}')
    
#extraindo os arquivos zipados e deletando os zips
#para arquivos até 2018
for i in periodo[1:-3]:
  zipfile.ZipFile(f'/content/dados_brutos/{i}.zip').extractall('/content/dados_brutos')
  os.remove(f'/content/dados_brutos/{i}.zip')

Em "dadosbrutos_INMET" estão alguns loops e f-strings bem legais e procedimentos para:






## Variáveis meteorológicas disponíveis - INMET


Ainda tenho muuuuuito a aprender, então qualquer sugestão é muito bem-vinda.


A manipulação dos dados das estações do INMET ficará para a próxima!
