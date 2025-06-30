from typing import Optional
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel, Field
from langchain_core.prompts import PromptTemplate
from langgraph.graph import START, END, StateGraph

load_dotenv(override=True)

llm  = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0.8)

class GraphState(BaseModel):
    user_input: str = Field(description="User input.")
    title: Optional[str] = Field(default=None, description="The title of the story.")
    story: Optional[str] = Field(default=None, description="The story.")
    improved_story: Optional[str] = Field(default=None, description="The imporved version of our story.")

def title_generator(state: GraphState):
    user_input = state.user_input
    prompt = PromptTemplate(
        template="Generate a title for the following input: {user_input}. Respond with only the title.",
        input_variables = ["user_input"]
    )
    chain = prompt | llm
    response = chain.invoke({"user_input": user_input})
    return {"title": response.content}

def story_generator(state: GraphState):
    title = state.title
    prompt = PromptTemplate(
        template="Generate a story for the following title: {title}. Respond with only the story.",
        input_variables = ["title"]
    )
    chain = prompt | llm
    response = chain.invoke({"title": title})
    return {"story": response.content}

def improve_story(state: GraphState):
    story = state.story
    prompt = PromptTemplate(
        template="Imrpove the following story: {story}. Respond with only the story.",
        input_variables = ["story"]
    )
    chain = prompt | llm
    response = chain.invoke({"story": story})
    return {"improved_story": response.content}

builder = StateGraph(GraphState)

builder.add_node("title_generator", title_generator)
builder.add_node("story_generator", story_generator)
builder.add_node("improve_story", improve_story)

builder.add_edge(START, "title_generator")
builder.add_edge("title_generator", "story_generator")
builder.add_edge("story_generator", "improve_story")
builder.add_edge("improve_story", END)

graph = builder.compile()

response = graph.invoke({"user_input": "Tell me a random story"})

print(response)

# print(graph.get_graph().draw_ascii())