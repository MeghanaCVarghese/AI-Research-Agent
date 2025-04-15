# -*- coding: utf-8 -*-
# import streamlit as st

# st.title("AI-Powered Personalized Research Agent")
# st.write("This is a demo interface for the research agent.")

# if st.button("Click Me"):
#     st.success("Hello! Your frontend is working.")

import streamlit as st
import requests
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt

st.set_page_config(page_title="AI Research Agent", layout="wide")

st.title("🤖 AI-Powered Personalized Research Agent")

with st.sidebar:
    st.header("Query Settings")
    topics = st.multiselect("Select Topics", ["AI", "Climate", "Health", "Finance", "Education"], default=["AI"])
    sources = st.multiselect("Select Sources", ["news", "arxiv"], default=["news"])
    time_range = st.selectbox("Time Range", ["7d", "30d", "90d"])
    btn = st.button("Fetch Research")



if btn:
    with st.spinner("Collecting data and analyzing..."):
        response = requests.post("http://localhost:8000/search", json={"topics": topics, "sources": sources, "time_range": time_range})
        result = response.json()

        st.success("Results loaded!")

        st.subheader("🔍 Summarized Insights")
        st.write(result["summary"])

        st.subheader("📊 Keyword Cloud")
        wordcloud = WordCloud(width=800, height=300, background_color="white").generate(result["summary"])
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        st.pyplot(plt)

        st.subheader("📈 Trend Chart (Demo)")
        fig = px.line(x=["Week 1", "Week 2", "Week 3"], y=[12, 18, 29], labels={"x": "Weeks", "y": "Mentions"})
        st.plotly_chart(fig)
