import pandas as pd
from netCDF4 import Dataset
from wrf import getvar 
from matplotlib import pyplot as plt

#path = r'C:\Users\'
#wrf_file = Dataset(path + '\TROPwrfout_d01_2022-01-02_00h.nc')

TROPd01_t2_carira = []
TROPd01_t2_itabaianinha = []
TROPd01_t2_palmeira = []
TROPd01_t2_piranhas = []
TROPd01_t2_pverde = []
TROPd01_t2_maceio = []
TROPd01_t2_nsgloria = []

TROPd01_vento_carira = []
TROPd01_vento_itabaianinha = []
TROPd01_vento_palmeira = []
TROPd01_vento_piranhas = []
TROPd01_vento_pverde = []
TROPd01_vento_maceio = []
TROPd01_vento_nsgloria = []
       
for i in range(0, 12):
    t2K = getvar(wrf_file, "T2", timeidx=i)
    t2C = t2K - 273.15
    TROPd01_t2_carira.append(((t2C[43][38]).values)-0)
    TROPd01_t2_itabaianinha.append(((t2C[32][38]).values)-0)
    TROPd01_t2_palmeira.append(((t2C[54][52]).values)-0)
    TROPd01_t2_piranhas.append(((t2C[52][38]).values)-0)
    TROPd01_t2_pverde.append(((t2C[38][34]).values)-0)
    TROPd01_t2_maceio.append(((t2C[53][63]).values)-0)
    TROPd01_t2_nsgloria.append(((t2C[45][42]).values)-0)
    
    wspd10 = getvar(wrf_file, "wspd10", timeidx=i, units="m s-1")
    TROPd01_vento_carira.append(((wspd10[43][38]).values)-0)
    TROPd01_vento_itabaianinha.append(((wspd10[32][38]).values)-0)
    TROPd01_vento_palmeira.append(((wspd10[54][52]).values)-0)
    TROPd01_vento_piranhas.append(((wspd10[52][38]).values)-0)
    TROPd01_vento_pverde.append(((wspd10[38][34]).values)-0)
    TROPd01_vento_maceio.append(((wspd10[53][63]).values)-0)
    TROPd01_vento_nsgloria.append(((wspd10[45][42]).values)-0)

saidas = []
saidasTROP_d01 = pd.DataFrame(saidas)
saidasTROP_d01['coluna1'] = TROPd01_t2_carira
saidasTROP_d01['coluna2'] = TROPd01_t2_itabaianinha
saidasTROP_d01['coluna3'] = TROPd01_t2_palmeira
saidasTROP_d01['coluna4'] = TROPd01_t2_piranhas
saidasTROP_d01['coluna5'] = TROPd01_t2_pverde
saidasTROP_d01['coluna6'] = TROPd01_t2_maceio
saidasTROP_d01['coluna7'] = TROPd01_t2_nsgloria
saidasTROP_d01.columns = ['Carira', 'Itabaianinha', 'PalmeiradosÍndios', 'Piranhas', 'PoçoVerde', 'Maceió', 'NSdaGlória']
#saidasTROP_d01.to_csv('TROP_d01_t2.csv')
saidasTROP_d01.round(2)


vento = []
TROPvento_d01 = pd.DataFrame(vento)
TROPvento_d01['coluna1'] = TROPd01_vento_carira
TROPvento_d01['coluna2'] = TROPd01_vento_itabaianinha
TROPvento_d01['coluna3'] = TROPd01_vento_palmeira
TROPvento_d01['coluna4'] = TROPd01_vento_piranhas
TROPvento_d01['coluna5'] = TROPd01_vento_pverde
TROPvento_d01['coluna6'] = TROPd01_vento_maceio
TROPvento_d01['coluna7'] = TROPd01_vento_nsgloria
TROPvento_d01.columns = ['Carira', 'Itabaianinha', 'PalmeiradosÍndios', 'Piranhas', 'PoçoVerde', 'Maceió', 'NSdaGlória']
#TROPvento_d01.to_csv('TROP_d01_vento.csv')
TROPvento_d01.round(2)


maceio = pd.read_csv(path + '\A303_Maceio.csv', sep =';',
                 thousands = '.', decimal = ',',
                 encoding='latin-1', index_col=None)

piranhas = pd.read_csv(path + '\A371_Piranhas.csv', sep =';',
                 thousands = '.', decimal = ',',
                 encoding='latin-1', index_col=None)

itabaianinha = pd.read_csv(path + '\A417_Itabaianinha.csv', sep =';',
                 thousands = '.', decimal = ',',
                 encoding='latin-1', index_col=None)


temp_CONUS_9km = pd.read_csv(path + '\CONUS_d01_t2.csv')
temp_CONUS_3km = pd.read_csv(path + '\CONUS_d02_t2.csv')
temp_TROP_9km = pd.read_csv(path + '\TROP_d01_t2.csv')
temp_TROP_3km = pd.read_csv(path + '\TROP_d02_t2.csv')

vento_CONUS_9km = pd.read_csv(path + '\CONUS_d01_vento.csv')
vento_CONUS_3km = pd.read_csv(path + '\CONUS_d02_vento.csv')
vento_TROP_9km = pd.read_csv(path + '\TROP_d01_vento.csv')
vento_TROP_3km = pd.read_csv(path + '\TROP_d02_vento.csv')



#Plotagem da temperatura
fig, ax = plt.subplots(figsize=(15, 5))
ax.plot(maceio['Temp. Ins. (C)'], label='INMET', linewidth=1.0, marker='o')
ax.plot(temp_CONUS_9km.Maceió, label='CONUS - 9km', linewidth=2.0, linestyle ='--')
ax.plot(temp_CONUS_3km.Maceió, label='CONUS - 3km', linewidth=2.0, linestyle ='--')
#ax.plot(saidas_d03.Maceió, label='CONUS - 1km', linewidth=2.0, linestyle ='--')
ax.plot(temp_TROP_9km.Maceió, label='TROP - 9km', linewidth=2.0, linestyle ='--')
ax.plot(temp_TROP_3km.Maceió, label='TROP - 3km', linewidth=2.0, linestyle ='--')
ax.set_xlabel('Hora (Z)')
ax.set_ylabel('Temperatura 2m (°C)')
ax.set_title('Temperatura do Ar (°C) em 2m - INMET x WRF 9x3x1km - Maceió-AL')
ax.legend(loc=2)

plt.show()
fig.savefig('Maceió_Temp.png', dpi=600)



#Plotagem do vento
fig, ax = plt.subplots(figsize=(15, 5))
ax.plot(maceio['Vel. Vento (m/s)'], label='INMET', linewidth=1.0, marker='o')
ax.plot(vento_CONUS_9km.Maceió, label='CONUS - 9km', linewidth=2.0, linestyle ='--')
ax.plot(vento_CONUS_3km.Maceió, label='CONUS - 3km', linewidth=2.0, linestyle ='--')
#ax.plot(vento_d03.Maceió, label='CONUS - 1km', linewidth=2.0, linestyle ='--')
ax.plot(vento_TROP_9km.Maceió, label='TROP - 9km', linewidth=2.0, linestyle ='--')
ax.plot(vento_TROP_3km.Maceió, label='TROP - 3km', linewidth=2.0, linestyle ='--')
ax.set_xlabel('Hora (Z)')
ax.set_ylabel('Velocidade do Vento 10m (m/s)')
ax.set_title('Velocidade do Vento (m/s) em 10m - INMET x WRF 9x3x1km - Maceió-AL')
ax.legend(loc=2)

plt.show()
fig.savefig('Maceió_Vento.png', dpi=600)

                
