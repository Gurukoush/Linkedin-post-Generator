<<<<<<< HEAD
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)




=======
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)




>>>>>>> 19bc7e992874f753d9dc699da82442f0aaa3f359
