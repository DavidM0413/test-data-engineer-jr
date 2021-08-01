#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


L_a = pd.read_json('C:/Users/jmartinez/prueba/lineas_aereas.json')
p_2016 = pd.read_json('C:/Users/jmartinez/prueba/pasajeros_2016.json')
p_2017 = pd.read_json('C:/Users/jmartinez/prueba/pasajeros_2017.json')
v_2016 = pd.read_json('C:/Users/jmartinez/prueba/vuelos_2016.json')
v_2017 = pd.read_json('C:/Users/jmartinez/prueba/vuelos_2017.json')


# In[3]:


p_2016.insert(3, "Año", 2016)
p_2017.insert(3, "Año", 2017)


# In[4]:


pasajeros = pd.concat([p_2016, p_2017])
viajes = pd.concat([v_2016, v_2017])
print(pasajeros)
print(viajes)


# In[5]:


viajes = viajes.rename(columns = {'Cve_Cliente': 'ID_Pasajero'})


# In[6]:


print(viajes[viajes['ID_Pasajero'] == 553])
print("\n")
print(pasajeros[pasajeros['ID_Pasajero'] == 553])


# In[7]:


consolidados = pd.merge(pasajeros,viajes, on = "ID_Pasajero", how = "outer")
consolidados.describe()


# In[8]:


consolidados[consolidados['Precio'].isnull()]


# In[9]:


consolidados = pd.merge(pasajeros,viajes, on = "ID_Pasajero", how = "inner")
consolidados


# In[26]:


L_a


# In[10]:


L_a = L_a.rename(columns = {'Code': 'Cve_LA'})


# In[11]:


consolidados2 = pd.merge(consolidados, L_a, on = "Cve_LA", how = "left")
consolidados2['Linea_Aerea'].fillna('Otra', inplace = True)
consolidados2


# In[12]:


consolidados3 = consolidados2[["Viaje","Clase", "Precio", "Ruta", "Edad", "Linea_Aerea"]]
consolidados3


# In[13]:


consolidados3['Año'] = consolidados2['Año']
consolidados3['Semestre'] = " "
consolidados3


# In[14]:


consolidados3['Viaje'] = pd.to_datetime(consolidados3['Viaje'])


# In[15]:


consolidados3["Semestre"][consolidados3['Viaje'].between("2016-01-01", "2016-06-30", inclusive = True)] = "Primero"
consolidados3["Semestre"][consolidados3['Viaje'].between("2017-01-01", "2017-06-30", inclusive = True)] = "Primero"


# In[16]:


consolidados3["Semestre"][consolidados3['Viaje'].between("2016-07-01", "2016-12-31", inclusive = True)] = "Segundo"
consolidados3["Semestre"][consolidados3['Viaje'].between("2017-07-01", "2017-12-31", inclusive = True)] = "Segundo"


# In[17]:


consolidados3


# In[18]:


promedios = consolidados3.groupby(["Semestre", "Año", "Clase", "Linea_Aerea"])["Precio"].mean()
promedios


# In[ ]:




