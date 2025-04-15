# -*- coding: utf-8 -*-
# import streamlit as st

# st.title("AI-Powered Personalized Research Agent")
# st.write("This is a demo interface for the research agent.")

# if st.button("Click Me"):
#     st.success("Hello! Your frontend is working.")

# -*- coding: utf-8 -*-
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
        try:
            response = requests.post("http://localhost:8000/search", json={"topics": topics, "sources": sources, "time_range": time_range})
            response.raise_for_status()  # Raise an error for HTTP errors
            result = response.json()
        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching data: {e}")
            result = {"summary": "No data available."}

        st.success("Results loaded!")

        st.subheader("🔍 Summarized Insights")
        st.write(result.get("summary", "No summary available."))

        st.subheader("📊 Keyword Cloud")
        wordcloud = WordCloud(width=800, height=300, background_color="white").generate(result.get("summary", ""))
        fig, ax = plt.subplots()
        ax.imshow(wordcloud, interpolation='bilinear')
        ax.axis("off")
        st.pyplot(fig)

        st.subheader("📈 Trend Chart (Demo)")
        fig = px.line(x=["Week 1", "Week 2", "Week 3"], y=[12, 18, 29], labels={"x": "Weeks", "y": "Mentions"})
        st.plotly_chart(fig)