import requests
import xml.etree.ElementTree as ET
import os
import re

def download_arxiv_papers(search_query: str, start: int = 0, max_results: int = 10, pdf_dir: str = "arxiv_pdfs", summary_dir: str = "arxiv_summaries"):
    """
    Download PDFs and summaries of papers from arXiv based on the search query.
    
    Args:
        search_query (str): The search query to use for fetching papers from arXiv.
        start (int): The starting index for fetching results.
        max_results (int): The maximum number of results to fetch.
        pdf_dir (str): The directory to save the downloaded PDFs.
        summary_dir (str): The directory to save the summaries of the papers.
    """
    url = f"http://export.arxiv.org/api/query?search_query={search_query}&start={start}&max_results={max_results}"

    response = requests.get(url)

    os.makedirs(pdf_dir, exist_ok=True)
    os.makedirs(summary_dir, exist_ok=True)

    def create_valid_filename(title: str) -> str:
        """Replace special characters in filename to make it valid."""
        return re.sub(r'[\\/*?:"<>|]', "", title)

    if response.status_code == 200:
        root = ET.fromstring(response.content)
        
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            title = entry.find("{http://www.w3.org/2005/Atom}title").text.strip()
            summary = entry.find("{http://www.w3.org/2005/Atom}summary").text.strip()
            link = entry.find("{http://www.w3.org/2005/Atom}id").text.strip()

            valid_title = create_valid_filename(title)
            pdf_filename = os.path.join(pdf_dir, f"{valid_title}.pdf")
            summary_filename = os.path.join(summary_dir, f"{valid_title}.txt")

            pdf_link = f"{link}.pdf"

            pdf_response = requests.get(pdf_link)
            if pdf_response.status_code == 200:
                with open(pdf_filename, "wb") as pdf_file:
                    pdf_file.write(pdf_response.content)

            with open(summary_filename, "w") as summary_file:
                summary_file.write(summary)
    else:
        print(f"Failed to retrieve data: {response.status_code}")

