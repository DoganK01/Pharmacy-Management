from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    StorageContext,
    load_index_from_storage,
)
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
import nest_asyncio
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from llama_index.agent.openai import OpenAIAgent
from llama_index.core import SummaryIndex
from llama_index.core.node_parser import SentenceSplitter
from tqdm.notebook import tqdm
import pickle
import os
import pandas as pd
from llama_index.core.query_engine import PandasQueryEngine
from llama_index.core.agent import ReActAgent
import csv

from llama_index.core.tools import FunctionTool

os.environ["OPENAI_API_KEY"] = "X"

Settings.llm = OpenAI(model="gpt-3.5-turbo")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-large")

tools = []

query_engines = {}

for file_name, df in dataframes.items():
  query_engine = PandasQueryEngine(
      df=df, verbose=True, instruction_str=instruction_str
  )
  query_engine.update_prompts({"pandas_prompt": new_prompt})

  tool = [
      note_engine,
      QueryEngineTool(
          query_engine=query_engine,
          metadata=ToolMetadata(
              name=f"pandas_tool_for_{file_name}_sales",
              description="Useful for questions related to specific aspects of"
              f" medicine sales for the {file_name} time period (e.g. hourly, daily, weekly, monthly medicine sales for a pharmacy)"
          ),
      ),
  ]
  query_engines[file_name] = query_engine
  tools.extend(tool)

llm = OpenAI(model="gpt-3.5-turbo-0613")
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True, context=context)


while (prompt := input("Enter a prompt (q to quit): ")) != "q":
    result = agent.query(prompt)
    print(result)


