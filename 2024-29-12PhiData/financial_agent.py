from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os
from dotenv import load_dotenv
load_dotenv()


# Web Search agent
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

multi_ai_agent = Agent(
    team=[websearch_agent,finance_agent],
    instructions=["Always Include sources","Use tables to display extensive data"],
    show_tool_calls=True,
    markdown=True,
    model = Groq(
        api_key=os.getenv('GROQ_API_KEY'),
        id="llama3-groq-8b-8192-tool-use-preview"
    
    ),
)

multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for TSLA", stream=True)