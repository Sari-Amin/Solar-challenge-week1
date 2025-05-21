import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Solar Farm Insights", layout="wide")

st.title("🌞 Solar Irradiance Dashboard")
st.markdown("Compare solar potential across Benin, Togo, and Sierra Leone")

@st.cache
def load_data():
    
    benin = pd.read_csv("../data/benin_clean.csv")
    togo = pd.read_csv("../data/togo_clean.csv")
    sierraleone = pd.read_csv("../data/sierraleone_clean.csv")

    benin["Country"] = "Benin"
    togo["Country"] = "Togo"
    sierraleone["Country"] = "Sierra Leone"

    return pd.concat([benin, togo, sierraleone], ignore_index = True)


df = load_data()

# Sidebar for country selection
selected_countries = st.sidebar.multiselect(
    "Select Countries", options=df["Country"].unique(), default=df["Country"].unique()
)

filtered_df = df[df["Country"].isin(selected_countries)]


# GHI Boxplot
st.subheader("📦 GHI Distribution")
fig, ax = plt.subplots(figsize=(10, 5))
sns.boxplot(data=filtered_df, x="Country", y="GHI", ax=ax)
st.pyplot(fig)

# Mean GHI bar chart
st.subheader("📊 Average GHI by Country")
ghi_means = filtered_df.groupby("Country")["GHI"].mean().sort_values(ascending=False)
st.bar_chart(ghi_means)