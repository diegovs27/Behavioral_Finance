#!/usr/bin/env python
# coding: utf-8

# In[1]:


def LossAversion(data):
    
    import numpy as np
    import pandas as pd
    import func_json as fj
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots
    
    # Obtenemos la información que necesitamos para observar si hay sesgo o no
    Mov_tot = len(data) #Número de operaciones
    Tot_loss = len(data[data['Profit']<0]) #Contamos las veces que se registró una pérdida
    Loss_av = len(data[(data['Profit']<0)&(data['closePrice']>data['S/L'])]) #Operaciones con pérdida antes del S/L
    Comp = Tot_loss-Loss_av #Complemento (para la gráfica)
    Porcentaje = (Loss_av/Tot_loss)
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
    res = pd.DataFrame(dic)
    
    return {'Resultados': res,
           'Gráficos': fig}

    
    
    
    
    
    
    


# In[ ]:




