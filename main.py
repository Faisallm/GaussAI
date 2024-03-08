import streamlit as st
from langchain_experimental.agents.agent_toolkits.csv.base import create_csv_agent
from langchain_community.llms import OpenAI
from dotenv import load_dotenv



load_dotenv()

st.set_page_config(page_title="GaussAI 📈")
st.header("GaussAI")

user_csv = st.file_uploader("Upload your CSV file", type='csv')

if user_csv is not None:
    user_question = st.text_input("Ask a question about your CSV: ")
    # not creative
    llm = OpenAI(temperature=0)
    # create agent
    # verbose=True indicate that the agent is running code...
    # and is not asking for permission.
    agent = create_csv_agent(llm, user_csv, verbose=True)

    if user_question is not None and user_question != "":
        st.write(f"Your Question was: {user_question}")

        response = agent.run(user_question)
        st.write(response)

