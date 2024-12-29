from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
#from phi.model.azure import openai_chat
import dotenv

dotenv.load_dotenv()
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

## model ai gent
multi_ai_agent=Agent(
    team=[web_search_agent,financial_agent],
    model=Groq(id="llama-3.1-70b-versatile"),
    instructions=['always include sources','use table to display the data'],
    show_tool_calls=True,
    markdown=True
)

multi_ai_agent.print_response('Summaraize analyst recommendation and share the latest news for NVIDIA',stream=True)