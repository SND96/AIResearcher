import sys
from query_generator import generate_arxiv_queries
from arxiv_downloader import download_arxiv_papers

def main():
    if len(sys.argv) != 2:
        raise ValueError("Usage: python search_arxiv.py <initial_search_query>")

    search_query = sys.argv[1]
    download_papers_for_query(search_query)


def download_papers_for_query(initial_query: str):
    api_key = "d54dae610f891c57039c871fc9fa4fdb247116726e06f5d8308e3edde2f9f946"  
    generated_queries = generate_arxiv_queries(initial_query, api_key)

    for query in generated_queries:
        download_arxiv_papers(search_query=f"all:{query}")

if __name__ == "__main__":
    main()
