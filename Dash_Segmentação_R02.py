#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px
import dash
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
from dash import dash_table
import base64
from dash import dash_table
from dash_bootstrap_templates import load_figure_template
from IPython.display import Image
from IPython.display import display


# In[2]:


df = pd.read_csv('G:/Drives compartilhados/Informações/Serviços/2023/Professional Services/Solar/Análises/Segmentação 2/clusterizacao_porte_por_receita.csv',low_memory=False)


# In[5]:





# In[3]:


df


# In[4]:


df.columns


# In[5]:


df.groupby(['Canal'])[['Qde Checkouts']].describe()


# In[6]:


df['Cluster'] = df['Cluster'].astype('category')


# In[7]:


df = df[df['Receita_Liquida_Total']>0]


# In[8]:


df['Receita_Liquida_Total'].describe()


# In[9]:


(df[df['Receita_Liquida_Total'] < 3.869130e+03])


# In[10]:


gacorder = ['A', 'B', 'C', 'D', 'E', 'Ñ Definido']


# In[11]:


fig1 = px.box((df[df['Receita_Liquida_Total'] < 3.869130e+04]), x='GAC', y='Receita_Liquida_Total', color='GAC',  color_discrete_sequence=px.colors.qualitative.Pastel, category_orders={'GAC': gacorder})
fig1.update_layout(
    plot_bgcolor='white',
    height=500,
    width=800
)
fig1.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig1.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig1.update_layout(title = {
         'text': "Receita Líquida por GAC",
         'y':.95, # new
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top',
    # new
        })
fig1.show()


# In[12]:


df['Cluster'] = df['Cluster'].astype(str)


# In[13]:


cluster_order = [str(i) for i in range(10)]


# In[14]:


fig2 = px.box((df[df['Receita_Liquida_Total'] < 3.869130e+04]), x='Cluster', y='Receita_Liquida_Total', color='Cluster',  color_discrete_sequence=px.colors.qualitative.Pastel, category_orders={'Cluster': cluster_order})
fig2.update_layout(
    plot_bgcolor='white',
    height=500,
    width=800
)
fig2.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig2.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig2.update_layout(title = {
         'text': "Receita Líquida por Cluster",
         'y':.95, # new
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top',
    # new
        })
fig2.show()


# In[15]:


kpigac = df.groupby(['GAC'])[['Receita_Liquida_Total']].describe()


# In[16]:


kpigac


# In[17]:


kpigac.columns


# In[18]:


print(kpigac.columns.get_level_values(1))


# In[19]:


kpigac.columns.get_level_values(1)


# In[20]:


kpigac['Receita_Liquida_Total']['count']


# In[21]:


kpicluster = df.groupby(['Cluster'])[['Receita_Liquida_Total']].describe()


# In[22]:


kpigac


# In[23]:


kpigac['Receita_Liquida_Total']['std']/kpigac['Receita_Liquida_Total']['mean']


# In[24]:


(kpigac['Receita_Liquida_Total']['std']/kpigac['Receita_Liquida_Total']['mean']).sum()/6


# In[25]:


kpicluster


# In[26]:


kpicluster['Receita_Liquida_Total']['std']/kpicluster['Receita_Liquida_Total']['mean']


# In[27]:


(kpicluster['Receita_Liquida_Total']['std']/kpicluster['Receita_Liquida_Total']['mean']).sum()/10


# In[28]:


df = df[df['Aderência ao Pedido Sugerido']!=0]


# In[29]:


df


# In[30]:


df['Aderência ao Pedido Sugerido'].describe()


# In[31]:


df.groupby(['Cluster'])[['Aderência ao Pedido Sugerido']].describe()


# In[32]:


df.groupby(['GAC'])[['Aderência ao Pedido Sugerido']].describe()


# In[33]:


adergac = df.groupby(['GAC'])[['Aderência ao Pedido Sugerido']].describe()


# In[34]:


adergac


# In[35]:


adergac['Aderência ao Pedido Sugerido']['std']/adergac['Aderência ao Pedido Sugerido']['mean']


# In[36]:


(adergac['Aderência ao Pedido Sugerido']['std']/adergac['Aderência ao Pedido Sugerido']['mean']).sum()/6


# In[37]:


adercluster = df.groupby(['Cluster'])[['Aderência ao Pedido Sugerido']].describe()


# In[38]:


adercluster


# In[39]:


adercluster['Aderência ao Pedido Sugerido']['std']/adercluster['Aderência ao Pedido Sugerido']['mean']


# In[40]:


(adercluster['Aderência ao Pedido Sugerido']['std']/adercluster['Aderência ao Pedido Sugerido']['mean']).sum()/10


# In[ ]:





# In[ ]:





# In[ ]:





# In[41]:


fig3 = px.box(df, x='Cluster', y='Aderência ao Pedido Sugerido', color='Cluster',  color_discrete_sequence=px.colors.qualitative.Pastel, category_orders={'Cluster': cluster_order})
fig3.update_layout(
    plot_bgcolor='white',
    height=500,
    width=800
)
fig3.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig3.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig3.update_layout(title = {
         'text': "Aderência ao Pedido Sugerido por Cluster",
         'y':.95, # new
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top',
    # new
        })
fig3.show()


# In[42]:


fig4 = px.box(df, x='GAC', y='Aderência ao Pedido Sugerido', color='GAC',  color_discrete_sequence=px.colors.qualitative.Pastel, category_orders={'Cluster': cluster_order})
fig4.update_layout(
    plot_bgcolor='white',
    height=500,
    width=800
)
fig4.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig4.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig4.update_layout(title = {
         'text': "Aderência ao Pedido Sugerido por GAC",
         'y':.95, # new
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top',
    # new
        })
fig4.show()


# In[43]:


fig5 = px.scatter(df, x='X1', y='X2', color='Cluster', size='Volume_Total',opacity=0.7, color_discrete_sequence=px.colors.qualitative.Pastel)
fig5.update_layout(
    height=500,
    width=800,
)
fig5.update_traces(marker=dict(size=8, line=dict(width=1, color='white')))
fig5.update_layout(title="Decomposição de variáveis em X1 e X2",
    plot_bgcolor='white'
)
fig5.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig5.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig5.update_layout(title = {
         'text': "Decomposição de variáveis em X1 e X2",
         'y':.95, # new
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top' # new
        })
fig5.show()


# In[44]:


fig6 = px.scatter(df, x='X1', y='X2', color='Cluster', size='Volume_Total',opacity=0.7, color_discrete_sequence=px.colors.qualitative.Pastel)
fig6.update_layout(
    height=500,
    width=800,
)
fig6.update_traces(marker=dict(size=10, line=dict(width=1, color='white')))
fig6.update_layout(title="Decomposição de variáveis em X1 e X2",
    plot_bgcolor='white'
)
fig6.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig6.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig6.update_layout(title = {
         'text': "Decomposição de variáveis em X1 e X2",
         'y':.95, # new
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top' # new
        })
fig6.show()


# In[45]:


fig7 = px.scatter(df[df['Volume_Total'] <= 5000], x='X1', y='X2', color='Fluxo', size='Volume_Total',hover_data=['Canal', 'seg_ajustada','Renda_Media', 'Volume_Total',
            'Fluxo'],opacity=0.7, color_discrete_sequence=px.colors.qualitative.Pastel)
fig7.update_layout(
    height=500,
    width=800,
)
#fig1.update_traces(marker=dict(size=10, line=dict(width=1, color='white')))
fig7.update_layout(title="Decomposição de variáveis em X1 e X2",
    plot_bgcolor='white'
)
fig7.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig7.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig7.update_layout(title = {
         'text': "Variação do Volume e Fluxo",
         'y':.95, # new
         'x':0.5,
         'xanchor': 'center',
         'yanchor': 'top' # new
        })
fig7.show()


# In[46]:


df.columns


# In[47]:


portes = df.groupby(['Cluster', 'Porte por Receita'])[['CNPJ']].count()


# In[48]:


portes = portes.reset_index()


# In[49]:


portes


# In[50]:


fig8 = px.bar(portes, y="CNPJ", x= 'Cluster',  opacity=0.8,color='Porte por Receita',color_discrete_sequence = px.colors.qualitative.Set2, category_orders={'Cluster': cluster_order})

fig8.update_layout(
    plot_bgcolor='white'
    
)
fig8.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='white'
)
fig8.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig8.update_layout(title = {
         #'text': "Porte dos PDVs por cluster",
         'y':0.9, # new
         'x':0.45,
         'xanchor': 'center',
         'yanchor': 'top' # new
        })
fig8.update_traces(width=0.45)
fig8.update_layout(
   xaxis = dict(
      tickmode = 'linear',
      tick0 = 1,
      dtick = 1
   )
)
fig8.show()


# In[51]:


seg = df.groupby(['Cluster', 'seg_ajustada'])[['CNPJ']].count()


# In[52]:


seg = seg.reset_index()


# In[53]:


seg


# In[54]:


fig9 = px.bar(seg, y="CNPJ", x= 'Cluster', opacity=0.8,color='seg_ajustada',color_discrete_sequence = px.colors.qualitative.Set2, category_orders={'Cluster': cluster_order})

fig9.update_layout(
    plot_bgcolor='white'
    
)
fig9.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='white'
)
fig9.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig9.update_layout(title = {
        # 'text': "Seg Intra dos PDVs por cluster",
         'y':0.9, # new
         'x':0.45,
         'xanchor': 'center',
         'yanchor': 'top' # new
        })
fig9.update_traces(width=0.45)
fig9.update_layout(
   xaxis = dict(
      tickmode = 'linear',
      tick0 = 1,
      dtick = 1
   )
)
fig9.show()


# In[55]:


canal = df.groupby(['Cluster', 'Canal'])[['CNPJ']].count()
canal= canal.reset_index()


# In[56]:


fig10 = px.bar(canal, y="CNPJ", x= 'Cluster',  opacity=0.8,color='Canal',color_discrete_sequence = px.colors.qualitative.Set2, category_orders={'Cluster': cluster_order})

fig10.update_layout(
    plot_bgcolor='white'
    
)
fig10.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='white'
)
fig10.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig10.update_layout(title = {
         #'text': "Porte dos PDVs por cluster",
         'y':0.9, # new
         'x':0.45,
         'xanchor': 'center',
         'yanchor': 'top' # new
        })
fig10.update_traces(width=0.45)
fig10.update_layout(
   xaxis = dict(
      tickmode = 'linear',
      tick0 = 1,
      dtick = 1
   )
)
fig10.show()


# In[57]:


fig11 = make_subplots(rows=2, cols=5, horizontal_spacing=0.08)
fig11.update_layout(
    height=700,
    width=900
)
fig11.add_trace(go.Box(y=df[df['Cluster']=='0']['Receita_Liquida_Total'], name = "Cluster 0"), row=1, col=1)
fig11.add_trace(go.Box(y=df[df['Cluster']=='1']['Receita_Liquida_Total'], name = "Cluster 1"), row=1, col=2)
fig11.add_trace(go.Box(y=df[df['Cluster']=='2']['Receita_Liquida_Total'], name = "Cluster 2"), row=1, col=3)
fig11.add_trace(go.Box(y=df[df['Cluster']=='3']['Receita_Liquida_Total'], name = "Cluster 3"), row=1, col=4)
fig11.add_trace(go.Box(y=df[df['Cluster']=='4']['Receita_Liquida_Total'], name = "Cluster 4"), row=1, col=5)
fig11.add_trace(go.Box(y=df[df['Cluster']=='5']['Receita_Liquida_Total'], name = "Cluster 5"), row=2, col=1)
fig11.add_trace(go.Box(y=df[df['Cluster']=='6']['Receita_Liquida_Total'], name = "Cluster 6"), row=2, col=2)
fig11.add_trace(go.Box(y=df[df['Cluster']=='7']['Receita_Liquida_Total'], name = "Cluster 7"), row=2, col=3)
fig11.add_trace(go.Box(y=df[df['Cluster']=='8']['Receita_Liquida_Total'], name = "Cluster 8"), row=2, col=4)
fig11.add_trace(go.Box(y=df[df['Cluster']=='9']['Receita_Liquida_Total'], name = "Cluster 9"), row=2, col=5)


fig11.update_layout(colorway=px.colors.qualitative.Set2)
fig11.update_layout(title = {
        #'text': " Boxplots: Volume por Cluster",
        'y':0.93, # new
        'x':0.45,
        'xanchor': 'center',
         'yanchor': 'top' # new
        })

fig11.update_layout(
    plot_bgcolor='white')
fig11.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig11.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig11.show()


# In[58]:


fig12 = px.scatter(df[df['Volume_Total']<20000], x="Volume_Total", y="Renda_Media", color="Canal", category_orders={'Cluster': cluster_order})
fig12.update_layout(
    plot_bgcolor='white'
)
fig12.update_xaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
fig12.update_yaxes(
    mirror=True,
    ticks='outside',
    showline=True,
    linecolor='lightgrey',
    gridcolor='lightgrey'
)
#fig9.update_layout(title = {
        # 'text': "Scatterplot: Volume x Renda",
         #'y':0.95, # new
         #'x':0.5,
        # 'xanchor': 'center',
       #  'yanchor': 'top'
       # }
#)
fig12.show()


# In[67]:


grp = df.groupby(['Cluster']).agg(Quantidade_PDV =('CNPJ', 'count'), Volume_Mediana=('Volume_Total', 'median'), Receita_Mediana=('Receita_Liquida_Total', 'median'), Renda_Mediana=('Renda_Media', 'median'),Fluxo_Medio=('Fluxo', 'mean'),)


# In[68]:


grp=grp.reset_index()


# In[69]:


grp


# In[73]:


grp.astype(float)


# In[74]:


grp = grp.round(2)
grp


# In[87]:


opcoes = list(df['Cluster'].unique())
opcoes.append("Todos os Clusters")


# In[94]:


df.columns


# In[105]:


df = df[['Cluster','CNPJ', 'Canal', 'Subcanal','UF','Volume_Total', 'Receita_Liquida_Total' ]]


# In[108]:


table = dash_table.DataTable(
        id = 'datatable',
        data=grp.to_dict('records'))

# Reference only
firstpage = [
    dbc.Row([
        dbc.Col([html.H3('SOLAR DASHBOARD', className='text-center mb-3 p-3'),
        html.Hr(),         
        ],
            width={'size': 12, 'offset': 0, 'order': 0}),
    ]),
    dbc.Row([
        dbc.Col([
        html.H6('Selecione o cluster a analisar:', className='text-center mb-2 p-1'),   
        dcc.Dropdown(
                id = 'lista_clusters',
                options = opcoes,
                value = 'Todos os Clusters',
                clearable=False,
            ),    
            html.Div('PDVs Segmentados: 22860', className='text-center mt-3 p-2'),
            html.Div('Estados: CE, PE e BA', className='text-center p-2'),
            html.Div('Período de venda: 11/22- 03/23', className='text-center p-2'),
            html.Div('Número de canais: 11', className='text-center p-2'),
            html.Div(id='p/e', className='text-center p-2'),
        ],
            width={'size': 3, 'offset': 0, 'order': 0}),

        dbc.Col([
        
            html.H5('Volume x Renda', className='text-center p-1'),
            dcc.Graph(id='graph1', figure=fig12, style={'height': 400}),
        ],
            width={'size': 6, 'offset': 0, 'order': 0}),
        
        dbc.Col([
            html.H5('Tabela Clusters', className='text-center p-1'),
            html.Div(table, style={'height': 400}),
        ],
            width={'size': 3, 'offset': 0, 'order': 0}),
    ]),
    dbc.Row([
        dbc.Col([
        html.H5('', className='text-center'),
            html.H6('Portes', className='text-center font-italic'),
            dcc.Graph(figure=fig8, style={'height': 350}),   
        ],
            width={'size': 4, 'offset': 0, 'order': 0}),
        dbc.Col([
        html.H5('', className='text-center'),
            html.H6('Segmentação Intraurbana', className='text-center font-italic'),
            dcc.Graph(figure=fig9, style={'height': 350}),  
        ],
            width={'size': 4, 'offset': 0, 'order': 0}),
        dbc.Col([
            html.H5('', className='text-center'),
            html.H6('Canal', className='text-center font-italic'),
            dcc.Graph(figure=fig10, style={'height': 350}),  
        ],
            width={'size': 4, 'offset': 0, 'order': 0}),
    ]),
   
]


# In[ ]:


app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])

app.layout = html.Div(id='page-content', children=firstpage, className='p-3')

@app.callback(
    Output('graph1', 'figure'),
    Input('lista_clusters', 'value')
)

def update_output(value):
    if value == 'Todos os Clusters':
        fig = fig12
    else:
        tabelafiltrada = df[df['Cluster']== value]
        fig = px.scatter(tabelafiltrada, y="Renda_Media", x= 'Volume_Total', title="Volume x Renda", opacity=0.8, color='Canal')
    return fig

if __name__ == '__main__':
    app.run_server(debug=False)


# In[ ]:





# In[ ]:




