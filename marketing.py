from google import genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import TypedDict, List
from langgraph.graph import StateGraph, END
from IPython.display import display, Image, Markdown

api_key = "" # Replace with your actual API key
os.environ["GOOGLE_API_KEY"] = api_key
#client = genai.Client(api_key=api_key)
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)

class MarketingContent(TypedDict):
    input_prompt : str
    location : str
    competitors : List[str]
    visitors : str
    strategy : str
    report : str

def location_agent(content: MarketingContent):
    """
    RESPONSIBILITY:
    - Understand the business intent of the query
    - Extract the geographical location for analysis
    - Analyze the location in terms of market potential, customer demographics, and competition
    """
    
    prompt = f"""
    You are a Retail Business Intelligence Analyst. Your task is to analyze the geographical location for a retail business based on the following information:

    Your responsibilities include:
    1. Identify the geographical location for analysis based on the input prompt.
    2. Confirm the intent is competitor analysis for clothing retail.

    Input Prompt: {content['input_prompt']}

    Ouput Only the location name. no explanation needed.
    """

    location = llm.invoke(prompt).content.strip()
    return {**content, "location": location }


def competitor_agent(content: MarketingContent):
    """
    RESPONSIBILITY:
    - Identify the nearby clothing store competitors in the specified location
    - Include major brands and strong local players
    """
    
    prompt = f"""
    You are a Market Research Agent specializing in retail competition.

    Your responsibilities include:
    - Identify 5 clothing store competitors
    - Focus on store with high visibility and visitors
    - Location : {content['location']}

    Output format:
    comma-separated list of competitor names. no explanation needed.
    """

    competitors = llm.invoke(prompt).content.strip()
    competitors = [comp.strip() for comp in competitors.split(",")]
    return {**content, "competitors": competitors }

def visitor_agent(content: MarketingContent):
    """
    RESPONSIBILITY:
    - Estimate the number of visitors for each identified competitor
    - Consider factors like foot traffic, store size, and location attractiveness
    """
    
    prompt = f"""
    You are a Retail Foot Traffic Analyst.

    Your responsibilities include:
    - Estimate the number of visitors for each competitor
    - Consider factors like foot traffic, store size, and location attractiveness
    - Compare weekdays vs weekends if relevant

    Location : {content['location']}
    Competitors: {', '.join(content['competitors'])}

    Output format:
    Provide concise, business friendly insights.
    """

    visitors = llm.invoke(prompt).content.strip()
    visitors = [visitor.strip() for visitor in visitors.split(",")]
    return {**content, "visitors": visitors }

def strategy_agent(content: MarketingContent):
    """
    RESPONSIBILITY:
    - Develop a competitive strategy for the retail business based on the analysis of competitors and visitor patterns
    """

    prompt = f"""
    You are a Retail Strategy Consultant.

    Your responsibilities include:
    - Develop a competitive strategy for the retail business based on the analysis of competitors and visitor patterns
    - Provide actionable recommendations to attract more visitors and differentiate from competitors
    - Consider factors like pricing, promotions, store layout, and customer experience

    visitors: {content['visitors']}

    Output:
    Provide concise, actionable recommendations in a business-friendly format.
    """

    strategy = llm.invoke(prompt).content.strip()
    return {**content, "strategy": strategy }   

def report_agent(content: MarketingContent):
    """
    RESPONSIBILITY:
    - Compile a comprehensive report summarizing the findings from the location analysis, competitor analysis, visitor estimates, and strategic recommendations
    - Ensure the report is clear, concise, and actionable for business decision-makers
    """

    report = f"""
    Competitive Intelligence Report for Retail Business

    Location: {content['location']}
    Competitors: {', '.join(content['competitors'])}
    Visitors: {', '.join(content['visitors'])}
    Strategy: {content['strategy']}

    """
    
    return {**content, "report": report }

graph = StateGraph(MarketingContent)
graph.add_node("location", location_agent)
graph.add_node("competitor", competitor_agent)
graph.add_node("visitor", visitor_agent)
graph.add_node("strategy", strategy_agent)
graph.add_node("report", report_agent, end_state=END)

graph.set_entry_point("location")

graph.add_edge("location", "competitor")
graph.add_edge("competitor", "visitor")
graph.add_edge("visitor", "strategy")
graph.add_edge("strategy", "report")
graph.add_edge("report", END)

app = graph.compile()
display(Image(app.get_graph().draw_mermaid_png))


input_state = {
    "input_prompt": "I want to open a new clothing retail store in downtown San Francisco"
    }

result = app.invoke(input_state)
print(result["report"])

display(Markdown(result["report"]))
