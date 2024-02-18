from langchain.chat_models import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

llm = ChatOpenAI()


class CommaSeperatedListeOutputParser(BaseOutputParser):
    def parse(self, output):
        return output.split(",")


def answer(company, prospect):
    template = "You are a salesperson for a company that sells {company}."
    human_template = (
        "What is your sales strategy to target the prospect {prospect}?"
    )
    chat_prompt = ChatPromptTemplate.from_messages(
        [("system", template), ("human", human_template)]
    )
    chain = chat_prompt | llm | CommaSeperatedListeOutputParser()
    res = chain.invoke(
        input={"company": f"{company}", "prospect": f"{prospect}"}
    )
    return res
