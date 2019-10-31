#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import func_json as fj
import f_bf_lossaversion as LA
import plotly.graph_objects as go
from plotly.subplots import make_subplots

def f_bf_lossaversion(data):
    """
    data: Base de datos con las operaciones del trader a evaluar
    
    Esta función mide en qué cantidad un trader incide en el sesgo de aversión a la pérdida
    """
    
    #Definir el sesgo
    e_explicacion = f'Loss aversion: Este sesgo consiste en contabilizar las ocasiones en las que se decide cerrar una operación, con pérdida, antes del stop loss que se había indicado.'
    
    
    # Obtenemos la información que necesitamos para observar si hay sesgo o no
    Mov_tot = len(data) #Número de operaciones
    Tot_loss = len(data[data['Profit']<0]) #Contamos las veces que se registró una pérdida
    Loss_av = len(data[(data['Profit']<0)&(data['closePrice']>data['S/L'])]) #Operaciones con pérdida antes del S/L
    Comp = Tot_loss-Loss_av #Complemento (para la gráfica)
    Porcentaje = round((Loss_av/Tot_loss)*100)
    e_escala = f'El trader tiene una incidencia al sesgo del:{Porcentaje}%'
    if Porcentaje>.5:
        R = 'Si'
    else:
        R = 'No'
            
    
    #Construcción de los gráficos que ejemplifiquen nuestro caso
    colors2 = ['gold','blue']
    labels2 = ['Cierres antes de S/L','Cierre normal']
    values2 = [Loss_av,Comp]
    colors1 = ['green', 'red']
    labels1 = ['Ganancia','Pérdida']
    values1 = [Mov_tot,Tot_loss]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=labels1, values=values1, name="Histórico",marker_colors=colors1),1, 1)
    fig.add_trace(go.Pie(labels=labels2, values=values2, name="Comportamiento en pérdidas",marker_colors=colors2),1, 2)
    fig.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig.update_layout(
        title_text="Sesgo de aversión a la pérdida",
        annotations=[dict(text='Histórico', x=0.18, y=0.5, font_size=20, showarrow=False),
                 dict(text='Pérdidas', x=0.82, y=0.5, font_size=20, showarrow=False)])
    #fig.show()
    # Datos para presentar
    
    dic = {'Número de operaciones':[Mov_tot],
           'Número de pérdidas': [Tot_loss],
           'Incidencias al sesgo': [Loss_av],
           'Incidencias al sesgo (%)': [Porcentaje],
           '¿Actúa bajo el sesgo?': [R]}
    df_datos = pd.DataFrame(dic)
    
    return {'datos': df_datos,
           'grafica': fig,
           'explicacion': e_explicacion,
           'escala': {'valor': Porcentaje,
                      'texto': e_escala}}


# In[ ]:




