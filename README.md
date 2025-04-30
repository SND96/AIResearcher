# AIResearcher

AIResearcher is a Python-based tool for automated research paper analysis and topic extraction. It helps researchers and academics by automatically downloading papers from arXiv, analyzing their content, and extracting key topics and section summaries.

## Features

- Automated arXiv paper downloading based on search queries
- Topic extraction from PDF papers using AI
- Section-wise summary generation
- Citation management
- CSV export of analyzed data

## Project Structure

```
AIResearcher/
├── arxiv_scraper/         # Module for arXiv paper downloading
├── get_pdf_topics/        # Module for PDF analysis and topic extraction
├── get_subtopics.py       # Script for handling subtopics
├── join_tables.py         # Utility for combining data tables
├── orchestrator.py        # Main orchestration script
├── prompts.py            # AI prompts for analysis
├── utils.py              # Utility functions
└── arxiv_downloader_environment.yaml  # Conda environment configuration
```

## Prerequisites

- Python 3.10
- Conda package manager

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/AIResearcher.git
cd AIResearcher
```

2. Create and activate the conda environment:
```bash
conda env create -f arxiv_downloader_environment.yaml
conda activate ai_researcher
```

## Usage

1. Set up your API key in the `orchestrator.py` file.

2. Run the main script:
```bash
python orchestrator.py
```

The script will:
- Download papers from arXiv based on the specified query
- Extract topics and section summaries
- Generate CSV files with the analysis results

## Output

The script generates two main CSV files:
- `papers_df.csv`: Contains extracted topics for each paper
- `sections_df.csv`: Contains section-wise summaries

