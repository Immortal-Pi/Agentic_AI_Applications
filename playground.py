from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
#from phi.model.azure import openai_chat
from dotenv import load_dotenv

import os 
import phi
from phi.playground import Playground, serve_playground_app

load_dotenv()
phi.api=os.getenv('PHI_API_KEY')

## web search agent
web_search_agent=Agent(
    name='web search Agent',
    role='Search the web for the information',# prompt 
    model=Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    tools=[DuckDuckGo()],
    instructions=['Always include sources'],
    show_tool_calls=True,
    markdown=True
)

## financial agent 
financial_agent=Agent(
    name='financial Agent',
    model=Groq(id='llama3-groq-70b-8192-tool-use-preview'),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=['use tables to display the data'],
    show_tool_calls=True,
    markdown=True,
)

app=Playground(agents=[financial_agent,web_search_agent]).get_app()

if __name__=='__main__':
    serve_playground_app('playground:app',reload=True)

