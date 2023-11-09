# This file contains the main code for the chatbot and backend. It is used by webpage.py to get the answer to a question.

#-------------------------Imports-------------------------#

import os 

from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory


#-------------------------Main Code-------------------------#

os.environ["OPENAI_API_KEY"] = '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'

# Here we load the Unicamp base from the web
unicamp_base_loader = WebBaseLoader("https://www.pg.unicamp.br/norma/31594/0").load()

# Here we split the documents into chunks of 500 characters, with 50 characters of overlap
# Those values can be changed to whatever you want (further testing is needed to find the best values)
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    length_function = len
)

unicamp_base_loader = text_splitter.transform_documents(unicamp_base_loader)

# Check how many documents were loaded
print("Loaded {} documents".format(len(unicamp_base_loader)))

# Create the vector store with the OpenAI embeddings
embeddings = OpenAIEmbeddings()

store = Chroma.from_documents(
    unicamp_base_loader,
    embeddings,
    collection_name="unicamp_base",
    persist_directory="data/unicamp_base"
)
store.persist()

# Template for the prompt to be used by the chatbot
template = """

Você e um bot de perguntas e respostas sobre o vestibular da Unicamp, usando somente a base de dados da Unicamp 2024.
Se não souber a resposta, dizer que não sabe. Foque em respostas objetivas e claras.

Em caso de mais de uma resposta possivel, escreva as possibilidade separadas por virgula explicando o contexto de cada uma.

{context}

{chat_history}

Pergunta: {question}
"""

PROMPT = PromptTemplate(
    template=template,
    input_variables=["context", "chat_history", "question"]
)

# Chat model used by the chatbot is GPT-3.5-turbo
chat_model = ChatOpenAI(temperature=0.3, model="gpt-3.5-turbo")

# Memory used by the chatbot is ConversationBufferMemory
memory = ConversationBufferMemory(memory_key='chat_history',
                                input_key='question')

# Here we create the chatbot using the chain type RetrievalQA
# The chain type kwargs are the arguments used by the chain type
# The retriever is the vector store
# The prompt is the template used by the chatbot
# The verbose argument is used to print the prompt and the answer
# The memory is the memory used by the chatbot
qa_with_source = RetrievalQA.from_chain_type(
    llm=chat_model,
    chain_type="stuff",
    retriever=store.as_retriever(),
    chain_type_kwargs={"prompt": PROMPT,
    "verbose": False,
    "memory": memory,
    },
    return_source_documents=True,
)

def get_ans(question):
    """Given a question, returns the answer and the source documents used to answer the question"""
    answer = qa_with_source(question)

    # print("Answer: {}".format(answer['result']))
    # print("Source documents: {}".format(answer['source_documents']))
    
    return answer['result'], answer['source_documents']