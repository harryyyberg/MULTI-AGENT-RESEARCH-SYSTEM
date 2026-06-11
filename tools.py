from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print
import requests
import streamlit as st

load_dotenv()

tavily = TavilyClient(api_key=st.secrets["TAVILY_API_KEY"])

@tool
def web_search(query : str)->str:
    """Search the web using Tavily.

    Args:
        query: Search query string.

    Returns:
        A formatted string containing titles, URLs, and snippets."""
    results = tavily.search(query = query,max_results = 5)

    out = []

    for r in results['results']:
        out.append(
            f"Title : {r['title']}\n URL: {r['url']}\nSnippet: {r['content'][:300]}\n"
        )
    return "\n----\n".join(out)


@tool
def scrape_url(url:str)->str:
    """Scrape a webpage.

    Args:
        url: Full URL including https://

    Returns:
        Clean text extracted from the webpage."""
    try:
        resp = requests.get(url,timeout=8,headers={"User-Agent" : "Mozilla/5.0"})
        soup = BeautifulSoup(resp.text, "html.parser")
        [tag.decompose() for tag in soup(["script", "style","nav","footer","noscript"])]
        return soup.get_text(separator=" ", strip=True)[:3000]
    except Exception as e:
        return f"Error scraping URL: {str(e)}"

# print(scrape_url.invoke("https://byjus.com/free-ias-prep/el-nino"))
# print(web_search.invoke("What is the effect of El-Nino on india?"))