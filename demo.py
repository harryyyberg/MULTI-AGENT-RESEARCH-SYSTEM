from agents import llm,build_search_agent
from tools import web_search

# llm_with_tools = llm.bind_tools([web_search])

# response = llm_with_tools.invoke(
#     "Search the web for recent information about El Nino"
# )

# print(response.content)

search_agent = build_search_agent()

result = search_agent.invoke({
    "messages": [
        ("user", "Find recent information about El Nino")
    ]
})

print(result)