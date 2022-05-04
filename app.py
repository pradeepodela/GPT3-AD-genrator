import streamlit as st
import os
import openai

#openai.api_key = 'Your Key'

st.title('Ad from product description')
def add(qurey,campain):
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=f"Write a creative ad for the following product to run on {campain} aimed at parents:\n\nProduct: {qurey}",
    temperature=0.5,
    max_tokens=60,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0
    )
    return response.choices[0].text
campain = st.text_input("Campaign For", "")
qurey = st.text_area('Enter your product description:')
st.text('(example:Learning Room is a virtual environment to help students from kindergarten to high school excel in school.')
button = st.button('Generate Ad')
if button:
    st.write(add(qurey,campain))
