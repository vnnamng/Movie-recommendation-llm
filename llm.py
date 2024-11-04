import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()
# tag::llm[]
# Create the LLM
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
    model=os.getenv("OPENAI_MODEL"),
)
# end::llm[]

# tag::embedding[]
# Create the Embedding model
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(
    openai_api_key=os.getenv("OPENAI_API_KEY"),
)
# end::embedding[]
