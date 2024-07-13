import os
from together import Together

def generate_arxiv_queries(initial_query: str, api_key: str) -> list:
    """
    Generate a list of 20 unique search queries for arXiv based on an initial query.
    
    Args:
        initial_query (str): The initial query to base the generated queries on.
        api_key (str): The API key for the Together service.
    
    Returns:
        list: A list of 20 unique search queries.
    """
    client = Together(api_key=api_key)

    prompt = f"Generate a bullet-point list of 20 unique search queries for arXiv based on the initial query '{initial_query}'. Each query should be relevant and unique. For example, for the initial query '{initial_query}', you might generate queries like '{initial_query} 2024', '{initial_query} methods', '{initial_query} applications', and so on."

    response = client.chat.completions.create(
        model="meta-llama/Llama-3-8b-chat-hf",
        messages=[{"role": "user", "content": prompt}],
    )

    generated_queries = [
        query.strip()
        for query in response.choices[0].message.content.split("\n")
        if query.strip().startswith("• ")
    ]

    return generated_queries
