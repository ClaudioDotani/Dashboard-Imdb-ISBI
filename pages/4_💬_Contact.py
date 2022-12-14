###Librerie
import datetime as dt
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
from PIL import Image
from IPython.core.display import display,HTML

css_prova="""
<style>
[data-testid="stImage"]{
    padding-left: 40%;
    padding-right: 40%;
}
[data-testid="collapsedControl"]{
    color: white;
   
}
[data-testid="stAppViewContainer"]{
    background-image: url(https://free4kwallpapers.com/uploads/originals/2022/07/16/-colorful-abstract-background-wallpaper.jpg);
    background-repeat: no-repeat;
    background-position: center;
    background-size: cover;
}

[id="contact"]{
    font-size: 72px;
    color: crimson;
    text-shadow: -1px 0 snow, 0 1px snow, 1px 0 snow, 0 -1px snow;
}

[id="Mauro Galateo - M63001332"]{
    font-size: 72px;
    color: crimson;
    text-shadow: -1px 0 snow, 0 1px snow, 1px 0 snow, 0 -1px snow;
}

[data-testid="stSidebar"]{
    background-color: dodgerblue;
    opacity: 0.8;
}
[data-testid="stHeader"]{
    background-color: black;
}
[data-testid="stToolbar"]{
    color: white;
}
.css-1hverof:visited{
    color:black;
}
.css-17lntkn{
    color:black;
}
.css-17nby6i:visited{
    background-color: rgb(255 255 255) !important
}

h2{
    color: limegreen;
    font-weight: bold !important;
}


</style>
"""


###Informazioni Pagina
st.set_page_config(
    page_title="Imdb Dashboard",
    page_icon="📽",
    layout="wide"
)


st.title("Contact")
st.markdown(css_prova, unsafe_allow_html=True)


st.title("Mauro Galateo - M63001332")
st.markdown(css_prova, unsafe_allow_html=True)


st.title("Claudio Dotani - M63001400")
st.markdown(css_prova, unsafe_allow_html=True)


st.title("Gianfranco Foscardi - M63001371")
st.markdown(css_prova, unsafe_allow_html=True)


st.title("Antonio Forino - ")
st.markdown(css_prova, unsafe_allow_html=True)
