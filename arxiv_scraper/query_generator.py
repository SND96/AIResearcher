import os
from together import Together

def generate_arxiv_queries(initial_query: str, api_key: str) -> list:
    """
    Generate a list of 5 unique search queries for arXiv based on an initial query.
    
    Args:
        initial_query (str): The initial query to base the generated queries on.
        api_key (str): The API key for the Together service.
    
    Returns:
        list: A list of 5 unique search queries.
    """
    client = Together(api_key=api_key)

    prompt = (f"Generate a list of 5 unique search queries for arXiv based on the initial query '{initial_query}'. "
              f"Each query should be relevant and unique. Only provide the queries in a comma-separated format without any additional text.")

    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": prompt}],
    )

    response_content = response.choices[0].message.content
    generated_queries = [query.strip() for query in response_content.split(",")]

    return generated_queries