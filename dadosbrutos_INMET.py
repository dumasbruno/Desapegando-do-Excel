import os                     #pacote os
import zipfile                #para arquivos zipados
import pandas as pd

#preparando a pasta
os.mkdir('dados_brutos')
os.chdir('dados_brutos')

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

#para arquivos a partir de 2019
for i in periodo[-3:]:
  zipfile.ZipFile(f'/content/dados_brutos/{i}.zip').extractall(f'/content/dados_brutos/{i}')
  os.remove(f'/content/dados_brutos/{i}.zip')

#concatenando os arquivos entre 2001 e 2018 da estação A101 - Manaus e A801 - Porto Alegre
ds_manaus = None
ds_PA = None

#começando por Manaus
for i in periodo[1:19]:
  if ds_manaus is None:
    ds_manaus = pd.read_csv(f'/content/dados_brutos/{i}/INMET_N_AM_A101_MANAUS_01-01-{i}_A_31-12-{i}.CSV', sep =';', 
                            thousands = '.', decimal = ',', skiprows=[0,1,2,3,4,5,6,7], 
                            encoding='latin-1', index_col=None)
  else:
    ds_manaus = pd.concat([ds_manaus, pd.read_csv(f'/content/dados_brutos/{i}/INMET_N_AM_A101_MANAUS_01-01-{i}_A_31-12-{i}.CSV', sep =';', 
                            thousands = '.', decimal = ',', skiprows=[0,1,2,3,4,5,6,7], 
                            encoding='latin-1', index_col=None)])
                            
#descartando algumas colunas e renomeando as restantes                           
ds_manaus = ds_manaus.drop(['PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)', 'PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)',
          'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)', 'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)', 'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)', 
          'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)', 'Unnamed: 19'], axis=1)

ds_manaus.columns = ['Data', 'HoraZ', 'Chuva', 'P', 'Rad', 'TempC', 'TempOrvC', 'TempMaxC',	'TempMinC', 'UR', 'Dir', 'Rajadas', 'Vento']
ds_manaus['Data'] = pd.to_datetime(ds_manaus['Data'], dayfirst=True)

#o mesmo procedimento, agora para Porto Alegre
for i in periodo[1:19]:
  if ds_PA is None:
    ds_PA = pd.read_csv(f'/content/dados_brutos/{i}/INMET_S_RS_A801_PORTO ALEGRE_01-01-{i}_A_31-12-{i}.CSV', sep =';', 
                            thousands = '.', decimal = ',', skiprows=[0,1,2,3,4,5,6,7], 
                            encoding='latin-1', index_col=None)
  else:
    ds_PA = pd.concat([ds_PA, pd.read_csv(f'/content/dados_brutos/{i}/INMET_S_RS_A801_PORTO ALEGRE_01-01-{i}_A_31-12-{i}.CSV', sep =';', 
                            thousands = '.', decimal = ',', skiprows=[0,1,2,3,4,5,6,7], 
                            encoding='latin-1', index_col=None)])
ds_PA = ds_PA.drop(['PRESSÃO ATMOSFERICA MAX.NA HORA ANT. (AUT) (mB)', 'PRESSÃO ATMOSFERICA MIN. NA HORA ANT. (AUT) (mB)',
          'TEMPERATURA ORVALHO MAX. NA HORA ANT. (AUT) (°C)', 'TEMPERATURA ORVALHO MIN. NA HORA ANT. (AUT) (°C)', 'UMIDADE REL. MAX. NA HORA ANT. (AUT) (%)', 
          'UMIDADE REL. MIN. NA HORA ANT. (AUT) (%)', 'Unnamed: 19'], axis=1)

ds_PA.columns = ['Data', 'HoraZ', 'Chuva', 'P', 'Rad', 'TempC', 'TempOrvC', 'TempMaxC',	'TempMinC', 'UR', 'Dir', 'Rajadas', 'Vento']
ds_PA['Data'] = pd.to_datetime(ds_PA['Data'], dayfirst=True)
