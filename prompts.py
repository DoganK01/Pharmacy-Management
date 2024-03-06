from llama_index.core import PromptTemplate


instruction_str = """\
    1. You can choose whether or not to use the provided tools but give the proper answers for given query.
    2. Analyze and summarize relevant data using advanced Data Science techniques.
    3. Only use the data given and requested to you.
    5. PRINT ONLY THE ESPRESSION.
    6. Do not quote the expression.

"""


new_prompt = PromptTemplate(
    """\
    You are working with a pandas dataframe in Python.
    The name of the dataframe is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions:
    {instruction_str}
    Query: {query_str}

    Expression:  """
)

context = """Purpose: The primary role of this agent is to assist users by providing accurate 
            information about medicine sales with their codes based on some time periods and details about some medicine with code informations. """
