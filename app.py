import streamlit as st
import openai
import pandas as pd

from openai import OpenAI
client = OpenAI()

with st.sidebar:
    file = st.file_uploader("Choose a file", type=["csv"])
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")

if file is not None:

    query_text = st.text_input("Enter your query")
    if st.button("Submit"):
        st.write(f"Query text: {query_text}")
        df = pd.read_csv(file)
        csv_data = df.to_csv(index=False)

        if openai_api_key == "":
            st.write("Please enter your OpenAI API key")
        else:
            # Set up the API key            
            openai.api_key = openai_api_key


        completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that works with CSV data. respond with answer no explaination required"},
            {"role": "user", "content": f"Given the following CSV data:\n{csv_data}\n\n{query_text}"}
        ]
        )

        st.write(completion.choices[0].message.content)






