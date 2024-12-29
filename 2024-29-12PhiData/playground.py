from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
import phi

from dotenv import load_dotenv
from phi.playground import Playground, serve_playground_app
load_dotenv()
from fastapi import FastAPI
import uvicorn

phi.api = os.getenv("PHI_API_KEY")




websearch_agent = Agent(
    
    name = "Web search agent",
    role = "Search the web for the information",
    model = Groq(
        api_key=os.getenv('GROQ_API_KEY'),
        id="llama3-groq-8b-8192-tool-use-preview"
    
    ),
    tools= [DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True
)

# Financial Agent

finance_agent = Agent(
    name="Finance AI Agent",
    model = Groq(
        api_key=os.getenv('GROQ_API_KEY'),
        id="llama3-groq-8b-8192-tool-use-preview"
    
    ),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True,company_info=True)],
    instructions=["Use tables to display extensive data"],
    show_tool_calls=True,
    markdown=True

)

app = Playground(agents = [finance_agent,websearch_agent]).get_app()

if __name__ == "__main__":
    serve_playground_app("playground:app", reload=True) 