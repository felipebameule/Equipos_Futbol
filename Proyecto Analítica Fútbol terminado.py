#!/usr/bin/env python
# coding: utf-8

# In[142]:


#Análisis de datos
import numpy as np
import pandas as pd

#Visualización de datos
import matplotlib.pyplot as plt
import seaborn as sb


# In[143]:


#Nombramos al dataframe utilizado "df"
df = pd.read_csv("./data.csv")
sb.set_style(style="whitegrid")


# In[144]:


#Lo imprimimos para visualizarlo
df


# In[145]:


#Utilizamos .columns para ver las columnas del dataset
df.columns


# In[146]:


#Utilizamos .head para obtener una visualización del dataframe
df.head()


# # Top 20 equipos con los mejores 11(top11)
# 

# In[147]:


#Utilizamos .columns nuevamente para ver las columnas del dataframe
df.columns


# In[190]:


team_with_the_best_11  =best_11_for_all_club.groupby(["Club"]).mean().sort_values(by="Overall",ascending=False).head(20).reset_index().sort_values(by="Overall")


# In[191]:


#Creamos una tabla de mejores jugadores de acuerdo a sus nombre y atributos 
players_value = df.groupby(["Name"])["Overall"].nlargest(10).reset_index()[["Name","Overall"]]
players_value.sort_values(by="Overall",ascending=False).head(20)


# In[152]:


#Creamos la tabla de aquellos equipos con mejor 11 inicial
team_with_the_best_11.sort_values(by="Overall")


# In[188]:


#Graficamos los clubes con mejor once inicial
plt.figure(figsize=(12,5))
sb.barplot(y= team_with_the_best_11.Club, x=team_with_the_best_11.Overall)
plt.title("Top 20 Equipos Con Mejor 11 Incial");


# # TOP 20 EQUIPOS MEJOR VALORADOS

# In[157]:


#Creamos un promedio de valoración por equipo y lo llamamos por el nombre de sus columnas
club_and_player_overall_rating = df.groupby(["Club"])["Overall"].mean()


# In[158]:


#Ordenamos a los aquellos que tengan la media más alta
player_with_the_best_team = club_and_player_overall_rating.nlargest(20).reset_index()


# In[159]:


#Realizamos un gráfico de barras de aquellos equipos con mejor valoración en base a sus jugadores
plt.figure(figsize=(12,5))
sb.barplot(x=player_with_the_best_team.Overall,y=player_with_the_best_team.Club)
plt.title("Top 20 Equipos Mejor Valorados");


# In[ ]:





# In[160]:


#Nuevamente imprimimos las columnas del dataframe
df.columns


# In[161]:


#Usamos .unique para obtener cada posición de la columna de posiciones
df.Position.unique()


# In[162]:



def get_best_player(position):
    top_20 = df.loc[df["Position"] == position].sort_values(by="Overall",ascending=False).head(20)
    return top_20
    


# # TOP 20 MEJORES CENTRODELANTEROS

# In[ ]:





# In[163]:


#Obtenemos una tabla de los mejores centrodelanteros para luego graficarla
top_20_best_strikers = get_best_player("ST")
top_20_best_strikers


# In[164]:


#Graficamos con scatterplot la relación entre las dos variables
plt.figure(figsize=(12,5))
sb.scatterplot(x="Name",y="Overall",hue="Club",data=top_20_best_strikers);
plt.xticks(rotation="vertical")
plt.legend(loc='upper right')
plt.title("Top 20 Mejores centrodelanteros")


# # TOP 20 MEJORES EXTREMOS IZQUIERDOS

# In[165]:


#Aplicamos el mismo gráfico para las distintas posiciones 
top_20_best_lw = get_best_player("LW")


# In[166]:


plt.figure(figsize=(12,5))
sb.scatterplot(x="Name",y="Overall",hue="Club",data=top_20_best_lw);
plt.xticks(rotation="vertical")
plt.legend(loc='upper right')
plt.title("Top 20 Mejores Extremos Izquierdo ")


# In[167]:


df.Position.unique()


# #  TOP 20 MEJORES EXTREMOS DERECHOS

# In[168]:


top_20_best_rw = get_best_player("RW")


# In[169]:


plt.figure(figsize=(12,5))
sb.scatterplot(x="Name",y="Overall",hue="Club",data=top_20_best_rw);
plt.xticks(rotation="vertical")
plt.legend(loc='upper right')
plt.title("Top 20 Mejores Extremos Derechos")


# # TOP 20 MEJORES DELANTEROS DERECHOS
# 

# In[170]:


top_20_best_rf = get_best_player("RF")


# In[171]:


plt.figure(figsize=(12,5))
sb.scatterplot(x="Name",y="Overall",hue="Club",data=top_20_best_rf);
plt.xticks(rotation="vertical")
plt.legend(loc='upper right')
plt.title("Top 20 Mejores Delanteros Derechos")


# # TOP 20 MEJORES DEFENSAS CENTRALES

# In[172]:


top_20_best_cf = get_best_player("CF")


# In[173]:


plt.figure(figsize=(12,5))
sb.scatterplot(x="Name",y="Overall",hue="Club",data=top_20_best_cf);
plt.xticks(rotation="vertical")
plt.legend(loc='upper right')
plt.title("Top 20 Mejores Defensas Centrales")


# # TOP 20 MEJORES GOLEROS

# In[175]:


top_20_best_gk = get_best_player("GK")


# In[176]:


plt.figure(figsize=(12,5))
sb.scatterplot(x="Name",y="Overall",hue="Club",data=top_20_best_gk);
plt.xticks(rotation="vertical")
plt.legend(loc='upper right')
plt.title("Top 20 Mejores Goleros")


# # TOP 20 MEJORES MEDIOCAMPISTAS

# In[177]:


#Indicamos que posiciones pertenecen a la variable de mediocampistas
midfielders = ['RCM' , 'LCM', 
       'LDM', 'CAM', 'CDM','RM', 'LAM', 'LM',  'RDM',
        'CM',  'RAM']


# In[178]:


#Creamos la tabla para los 20 mejores mediocampistas
top_20_best_midfielders = df.loc[df["Position"].apply(lambda x: x in midfielders )].sort_values(by="Overall",ascending=False).head(20).sort_values(by="Overall")
top_20_best_midfielders


# In[179]:


#La graficamos mediante barplot
plt.figure(figsize=(12,5))
sb.barplot(y="Name",x="Overall",data=top_20_best_midfielders.sort_values(by="Overall",ascending=False));


plt.title("Top 20 Mejores Mediocampistas")


#  # JUGADORES CON LA MEJOR CURVA DE DISPARO

# In[180]:


#Creamos la variable de aquellos jugadores con mejor curva de disparo
players_with_best_curve = df.nlargest(30,"Curve")[["Name","Curve","Club"]].head(15)
players_with_best_curve


# In[181]:


plt.figure(figsize=(12,5))
sb.scatterplot(x="Name",y="Curve",hue="Club",data=players_with_best_curve);
plt.xticks(rotation="vertical")
plt.legend(loc='upper right')
plt.title("Top 20 Jugadores con Mejores Atributos")


# # MATRIZ DE CORRELACIÓN

# In[182]:


#Creamos una matriz de correlación que indica las correlaciones entre las variables del dataset
corr_matrix =df.corr(method="pearson")


# In[183]:


plt.figure(figsize = (40, 25))
#agregamos al mapa de calor dos decimales para mejor comprensión
sb.heatmap(corr_matrix, annot = True, fmt='.2g')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




