import streamlit as st
import random


quotes = [
    "Every setback is a setup for a comeback.",
"Dream big, work hard, and never give up.",
"Your attitude shapes your reality.",
"Great things take time—stay patient and persistent.",
"Success starts with believing you can.",
]

 
st.title("🧠 Here is your Mindset Web App" )
st.write("Write down your today's mindset and take a motivational quote!")

 
mindset = st.text_area("Write today's Mandset:", "")

 
if st.button("Show Mindset"):
    if mindset:
        st.success(f"✅ Your mindset: {mindset}")
    else:
        st.warning("Warning ⚠! Write Mindset First..")
 
st.subheader("🌟Today Motivation:")
st.write(random.choice(quotes))