from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama  
import streamlit as st

st.title("Abi's LangChain Chatbot")
input_txt = st.text_input("Enter your text queries")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an AI Assistant. Your name is Nilla."),
    ("user", "User queries: {query}")
])

 
llm = Ollama(model="llama2")

output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_txt:
    st.write(chain.invoke({"query": input_txt}))