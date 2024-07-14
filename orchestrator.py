from get_pdf_topics.read_pdf import get_topics_df
from arxiv_scraper.search_arxiv import download_papers_for_query
import pandas as pd
import os



def main(folder_arxiv_pdfs, folder_arxiv_cits, api_key, num_topics=5):

    download_papers_for_query(initial_query="RAG", context="", num_queries=4, max_results=3)

    # Generate a list of all filenames in the folder
    file_list = os.listdir(folder_arxiv_pdfs)

    # Print the list of filenames
    # print(file_list)
    paper_df_list = []
    count = 0
    file_list.sort()
    for file in file_list:
        paper_df = get_topics_df(f"{folder_arxiv_pdfs}/{file}", api_key, num_topics)
        paper_df['Name']=file[:-4]
        with open(f"{folder_arxiv_cits}/{file[:-4]}.bib", "r") as txt_file:
            txt_contents = txt_file.read()
            paper_df['Citation'] = txt_contents

        paper_df_list.append(paper_df)
        if(count == 3):
            break
        count += 1
    
    paper_df_concat = (pd.concat(paper_df_list))
    
    return paper_df_concat.reset_index(drop=True)



if __name__ == "__main__":
    save_path = "downloaded_paper.pdf"
    folder_arxiv_pdfs = "arxiv_pdfs"
    folder_arxiv_cits = "arxiv_citations"
    api_key = "sk-proj-mAPSSokSt1DWvYIy7UBjT3BlbkFJ9j1IPuQQfFVJFC2eDQmN"
    papers = main(folder_arxiv_pdfs, folder_arxiv_cits, api_key, 2)
    print(papers)
    papers.to_csv("papers_df.csv", index=False)