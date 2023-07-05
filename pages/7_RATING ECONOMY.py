import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("GOD'sDATA.csv")
df.columns = df.columns.str.strip()

order = ['low income', 'lower middle income', 'upper middle income', 'high income']
df['Rating_economy'] = pd.Categorical(df['Rating_economy'], categories=order, ordered=True)

st.sidebar.header('User Input Parameters')

default_countries = df['Country'].unique().tolist()
selected_countries = st.sidebar.multiselect('Country', default_countries, default=default_countries)

selected_data = df[df['Country'].isin(selected_countries)]
rating_counts = selected_data.groupby(['Rating_economy', 'Country']).size().unstack(fill_value=0)

# Fill NaN values with zeros
rating_counts.fillna(0, inplace=True)

fig, ax = plt.subplots(figsize=(20, 5))
sns.barplot(data=rating_counts, x=rating_counts.index, y=rating_counts.columns, stacked=True, ax=ax)

ax.set_title("RATING ECONOMY OF SOUTHEAST ASIAN COUNTRIES \nData source: World Bank", fontweight='bold', loc='center', color='#FF4500', fontsize=18)
ax.set_xlabel("Rating economy", fontweight='bold', loc='center', fontsize=18, color='#00AA00')
ax.set_ylabel("Count", fontweight='bold', fontsize=14, color='#00AA00')
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)
sns.set_style('whitegrid')
ax.set_xticklabels(ax.get_xticklabels(), rotation=15)

ax.legend(title='Country', loc='best', bbox_to_anchor=(0.5, -0.4), ncol=5)
plt.tight_layout()
st.pyplot(fig)
