from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama
from browser_use import Agent
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
os.environ["ANONYMIZED_TELEMETRY"] = "false"

# Initialize the model
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash-002', api_key=GEMINI_API_KEY)
#llm=ChatOllama(model="llama3.2:latest", num_ctx=32000)

async def main():
    # Create agent with the model
    agent = Agent(
        task="Your task here",
        llm=llm
    )
    result = await agent.run()
    print(result)

asyncio.run(main())