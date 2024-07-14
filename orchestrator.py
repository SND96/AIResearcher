from get_pdf_topics.read_pdf import get_topics_df, get_sections_df
from arxiv_scraper.search_arxiv import download_papers_for_query
import pandas as pd
import os
import shutil
import time



def main(folder_arxiv_pdfs, folder_arxiv_cits, api_key, num_topics=5, num_queries=2, max_results=2):
    download_papers_for_query(initial_query="RAG", context="", num_queries=num_queries, max_results=max_results)

    # Generate a list of all filenames in the folder
    file_list = os.listdir(folder_arxiv_pdfs)

    # Print the list of filenames
    # print(file_list)
    print("Getting the topic list.")
    paper_df_topic_list = []
    file_list.sort()
    for file in file_list:
        paper_df = get_topics_df(f"{folder_arxiv_pdfs}/{file}", api_key, num_topics)
        paper_df['Name']=file[:-4]
        with open(f"{folder_arxiv_cits}/{file[:-4]}.bib", "r") as txt_file:
            txt_contents = txt_file.read()
            paper_df['Citation'] = txt_contents

        paper_df_topic_list.append(paper_df)
   
    
    paper_topics_concat = (pd.concat(paper_df_topic_list))

    print("Getting the section summaries.")

    paper_df_sections_list = []
    for file in file_list:
        paper_df = get_sections_df(f"{folder_arxiv_pdfs}/{file}", api_key)
        paper_df['Name']=file[:-4]
        try:
            with open(f"{folder_arxiv_cits}/{file[:-4]}.bib", "r") as txt_file:
                txt_contents = txt_file.read()
                paper_df['Citation'] = txt_contents
        except:
            paper_df['Citation'] = "No citation available"

        paper_df_sections_list.append(paper_df)
    paper_sections_df = pd.concat(paper_df_sections_list)
    # paper_sections_df = (pd.concat(paper_df_sections_list))
    
    return paper_topics_concat.reset_index(drop=True), paper_sections_df.reset_index(drop=True)



if __name__ == "__main__":
    save_path = "downloaded_paper.pdf"
    folder_arxiv_pdfs = "arxiv_pdfs"
    folder_arxiv_cits = "arxiv_citations"
    api_key = "sk-proj-mAPSSokSt1DWvYIy7UBjT3BlbkFJ9j1IPuQQfFVJFC2eDQmN"
    # api_key = "d54dae610f891c57039c871fc9fa4fdb247116726e06f5d8308e3edde2f9f946"

    # Delete all files in folders
    shutil.rmtree(folder_arxiv_pdfs)
    os.mkdir(folder_arxiv_pdfs)
    shutil.rmtree(folder_arxiv_cits)
    os.mkdir(folder_arxiv_cits)
    # Delay for 1 second to ensure folders are deleted
    time.sleep(1)

    papers, sections = main(folder_arxiv_pdfs, folder_arxiv_cits, api_key, 2, 2, 2)
    print(sections)
    papers.to_csv("papers_df.csv", index=False)
    sections.to_csv("sections_df.csv", index=False)
