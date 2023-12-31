from langchain.chains import RetrievalQAWithSourcesChain
from langchain import OpenAI
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

import os
os.environ["OPENAI_API_KEY"] = "[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]"

embeddings = OpenAIEmbeddings()

docsearch = Chroma(persist_directory="db", embedding_function=embeddings)

chain = RetrievalQAWithSourcesChain.from_chain_type(OpenAI(temperature=0), chain_type="stuff", retriever=docsearch.as_retriever())

user_input = input("What's your question: ")

result = chain({"question": user_input}, return_only_outputs=True)

print("Answer: " + result["answer"].replace('\n', ' '))
print("Source: " + result["sources"])