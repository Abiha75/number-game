import streamlit as st
from streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd
st.set_page_config(layout="wide")
from streamlit_agraph.config import Config, ConfigBuilder

final_vd = pd.read_csv(r'./final_top51.csv')

types_n = final_vd['node_type'].unique()

with st.sidebar:
    option = st.selectbox(
    'Would you like to look at diseases or comorbidity?',
    types_n)

 
final_arr_short1 = final_vd[final_vd.node_type == option]
types_u = final_arr_short1['Condition'].unique()
if option:
    with st.sidebar:
        option2 = st.selectbox(
        'Please select your Type:',
        types_u)    
    
final_arr_short = final_arr_short1[final_arr_short1.Condition == option2]

res = final_arr_short1['Condition'].value_counts().to_frame('Disease_count').reset_index()

st.bar_chart(res,x="Condition", y="Disease_count", color = "Disease_count",)


nodes = []
edges = []

df_genes = dict()

st.title('Knowledge graph for ' + option2 )
df_genes = dict(enumerate(final_arr_short.Protein.unique()))
for i in df_genes:
    nodes.append(Node(id=df_genes[i],
                      label=df_genes[i],
                      size=25,
                      shape="diamond",
                      color='#0000BB'))


df_disease = pd.DataFrame(final_arr_short.neighbour_name.value_counts().reset_index().values, columns=["name", "count"])
df_disease = df_disease.sort_index(axis = 0, ascending=True)
df_disease = df_disease[df_disease.name !='na']
for index, row in df_disease.iterrows():

            nodes.append( Node(id = row['name'],
                          label = row['name'],
                          size = 10*row['count'],
                               shape = "square",
                               color = '#bf9b30'
                              )
                        )

df_condition = dict()
df_condition = dict(enumerate(final_arr_short.Condition.unique()))
for k in df_condition:
    nodes.append(Node(id=df_condition[k],
                      label=f"   {option}      ",
                      size=200,
                      shape="circle",
                      color='#00FFFF'))

df_connections = final_arr_short.filter(items=['Protein', 'neighbour_name']).drop_duplicates()
df_connections = df_connections[df_connections.neighbour_name != 'na']
for index, row in df_connections.iterrows():
    edges.append(Edge(source=row['Protein'],
                      label="--",
                      target=row['neighbour_name']))

df_mconnections = final_arr_short.filter(items=['Protein', 'Condition']).drop_duplicates()
for index, row in df_mconnections.iterrows():
    edges.append(Edge(source=row['Condition'],
                      label="--",
                      target=row['Protein']))

config_builder = ConfigBuilder(nodes)
config = config_builder.build()

config.save("config.json")

config = Config(from_json="config.json")

return_value = agraph(nodes=nodes,
                      edges=edges,
                      config=config)


