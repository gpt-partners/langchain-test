from typing import List

from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.tools import tool
from langchain.tools.render import render_text_description


@tool("Get Text Length")
def get_text_length(text: str) -> int:
    """Get the length of a string."""
    return len(text)


template = """
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
"""


def tool_bot():
    tools: List = [get_text_length]
    prompt = PromptTemplate.from_template(template).partial(
        tools=render_text_description(tools),
        tool_names=", ".join(t.name for t in tools),
    )
    llm = ChatOpenAI(model_name="gpt-4", stop=["\nOberservation:"])
    agent = {"input": lambda x: x["input"]} | prompt | llm
    return prompt
