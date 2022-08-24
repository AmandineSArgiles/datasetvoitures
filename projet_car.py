import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.title('Hey Wilders, voici mon étude sur le dataset voiture')

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

