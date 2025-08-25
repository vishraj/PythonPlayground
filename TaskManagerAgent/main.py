from dotenv import load_dotenv
import os

from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import AgentExecutor, create_openai_tools_agent


@tool
def add_task() -> str:
    """
    Add a new task to the user's task list. 
    Use this when the user wants to add a task or create a new one.
    """
    return "Task added"

tools = [add_task]

# load the API keys
load_dotenv()
todoist_api_key = os.getenv("TODOIST_API_KEY")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# create the llm instance
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash", 
    google_api_key=gemini_api_key,
    temperature=0.3
)

system_prompt = """
You are a helpful assistant that helps people manage their tasks
using Todoist. When a task is added, confirm with a message and stop.
"""
user_input = input("Enter task: ")

# create the prompt
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("user", "{input}"),
    ("ai", "{agent_scratchpad}")
])  

# create the agent
agent = create_openai_tools_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=False)

response = agent_executor.invoke({"input": user_input})
print(response['output'])



