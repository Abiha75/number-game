import streamlit as st
import streamlit_agraph import agraph, Node, Edge, Config
import pandas as pd
st.set_page_config(layout="wide")
from streamlit_agraph.config import Config, ConfigBuilder

final_vd = pd.read_csv(r'./final_top51.csv')

with st.sidebar:
  option = st.selectbox(
  "Please slect your Type:"
  ('CVA', 'IHD', 'CM', 'ARR', 'VD', 'CMD'))

final_arr_short = final_vd[final_vd.Condition == option]

nodes = []
edges = []

df_genes = dict()

st.title('Knowledge graph')
df_genes=dict(enumerate(final_arr_short.Protein.unique()))
for i in df_genes:
            nodes.append( Node(id=df_genes[i],
                          label=df_genes[i],
                               size = 25,
                               shape = "diamond",
                               color = '#0000BB'
                              )
                        )
df_disease = pd.DataFrame(final_arr_short.neighbour_name.value_counts().reset_index().values, columns=["name", "count"])
df_disease = df_disease.sort_index(axis = 0, ascending=True)
df_disease = df_disease[df_disease.name !='na']
for indec, row in df_disease.iterrows():

            nodes.append( Node(id = row['name'],
                          label = row['name'],
                          size = 200,
                               shape = "circle",
                               color = '#00FFFF'
                              )
                        )

df_connections = final_arr_short.filter(items=['Protein', 'neighbour_name']).drop_duplicates()
d_connections = df_connections[df_connections.neighbour_name !='na']
for index, row in df_connections.iterrows():
          edges.append( Edge(source = row['Protein'],
                        label = "--",
                        target = row['neighbour_name'],
                            )
                      )
df_mconnections = final_arr_short.filter(items=['Protein', 'Condition']).drop_duplicates()
for index, row in df_mconnections.iterrows():
          edges.append( Edge(source=row['Condition'],
                          label="--",
                          target=row['Protein'],
                          )
                      )

config_builder = ConfigBuilder(nodes)
config = config_builder.build()

config.save("config.json")

config = Config(from_json="config.json")

return_value = agraph(nodes = nodes,
                      edges=edges,
                      config=config)
