import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.title('Quête STREAMLIT et GITHUB')

st.header('Import de la base de données')

st.subheader('Affichage de la base :')
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
st.write(df_cars)

st.write('Il y a 261 lignes pour 8 colonnes')

st.subheader('Quelques statistiques sur la base :')
df_cars.info()

df_cars.describe()

viz_correlation = sns.heatmap(df_cars.corr(), 
								center=0,annot = True,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

pays = df_cars['continent'].unique().tolist()
continent = st.radio('Choisissez le pays :', pays, 0)

df = df_cars[df_cars['continent'] == continent]

fig = px.scatter(df, x='hp', color='continent', hover_name='continent')

fig.update_layout(width=800)
st.write(fig)

fig3 = plt.figure(figsize=(5, 3))
sns.boxplot(df["mpg"])
st.pyplot(fig3)

pays2 = df_cars['continent'].unique().tolist()
continent2 = st.selectbox('Choisissez le pays :', pays2, 0)

df2 = df_cars[df_cars['continent'] == continent2]

fig2 = st.bar_chart(df2, x = 'cylinders', y = 'cubicinches')

#fig2.update_layout(width=800)
st.write(fig2)
