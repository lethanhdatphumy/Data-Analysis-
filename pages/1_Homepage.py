import streamlit as st
import pandas as pd
from PIL import Image
from pandas import options

st.set_page_config(
    page_title="",
    page_icon=":wave:",
)

page_bg_img = '''
<style>
[data-testid="stAppViewContainer"]  {
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size:cover;
background-repeat: no-repeat;
}
[data-testid="stHeader"]{
    background-color : rgba(0,0,0,0)
    
}
[data-testid="stSidebar"]{
background-image: url("https://images.unsplash.com/photo-1501426026826-31c667bdf23d");
background-size:cover;
background-repeat: no-repeat;
}
[data-testid="stImage"] > img{
border-radius:50%;

}
[data-testid="stImage"]{
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)



url= "https://github.com/lethanhdatphumy/Data-Analysis-/blob/ef854d147328f710a33112644b26eee591e0e29f/GOD'sDATA.csv"
data = pd.read_csv(url)
data.columns = data.columns.str.strip()
data["Year"] = data["Year"].astype(str)


st.title("Welcome to data visualization")
st.header("Our data: ")
st.write(data)


with open("GOD'sDATA.csv", "rb") as f:
    image = Image.open(f)

st.image(image, caption="Our data")

st.sidebar.markdown("## Sidebar")
st.sidebar.info("Select pages above <3")
