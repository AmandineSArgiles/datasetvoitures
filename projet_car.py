import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import plotly.express as px


st.title('Hey Wilders, voici mon étude sur le dataset voiture')
st.write("Ebauche d'appli")

st.header("Le dataframe df_car:")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_car = pd.read_csv(link)
st.write(df_car)


continent = (' US.', ' Europe.', ' Japan.')
genre = st.radio(
		'Veuillez choisir un continent de la liste',
		continent)

st.write('Vous avez sélectionné :', genre)

cond = df_car["continent"] == genre
st.write(df_car[cond])

st.header("Correlation:")

viz_correlation = sns.heatmap(df_car[cond].corr(), 
								center=0,
								cmap = sns.color_palette("vlag", as_cmap=True)
								)

st.pyplot(viz_correlation.figure)

if genre == " Japan.":

	st.subheader("Observation sur les corrélations pour le Japon :")
	st.write("On observe une corrélation positive entre hp et weights")
	st.write("On observe une corrélation négative entre hp et mpg")

elif genre == " US.":

	st.subheader("Observation sur les corrélations pour les USA :")
	st.write("On observe une corrélation positive entre hp et cylinders")
	st.write("On observe une corrélation négative entre cubicinches et mpg")


else:
	st.subheader("Observation sur les corrélations pour l'Europe:")
	st.write("On observe une corrélation positive entre weigthts et cylinders")
	st.write("On observe une corrélation négative entre hp et time-to-60")
	
st.header("Graphiques:")

df = df_car[cond]
fig = px.histogram(df, x="cylinders", title = "Total de voitures par nombres de cylindres")
st.plotly_chart(fig, use_container_width = True)

if genre == " Japan.":
	st.write("On peut observer qu'au Japon la majorité des véhicules sont des 4 cylindres et qu'il n'y a pas de 5 cylindre")
elif genre == " US.":
	st.write("On peut observer qu'aux USA il y a plus de grosses cylindrées (entre 7 et 9 cylindres)")
else:
	st.write("On peut observer qu'en Europe la majorité des véhicules sont des 4 cylindres mais qu'il y a aussi des véhicules allant jusqu'à 6 cylindres")
