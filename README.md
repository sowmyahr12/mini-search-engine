# Mini Search Engine 

A lightweight search engine built in Python that indexes documents, processes user queries, and ranks results using TF-IDF and Cosine Similarity.

## Features

- Document loading from local files
- Text preprocessing and tokenization
- Inverted index creation
- TF-IDF based document ranking
- Cosine similarity search
- Ranked search results
- Command-line search interface


## Project Architecture
User Query
|
↓
main.py
|
↓
Search Engine
|
├── Document Loader
|
├── Tokenizer
|
├── Inverted Index
|
├── TF-IDF Calculator
|
└── Cosine Similarity
|
↓
Ranked Results

## How It Works

### 1. Document Loading

The system reads text documents from the `data` directory.

Example:
data/
├── python.txt
├── java.txt
└── database.txt


### 2. Text Processing

Documents are converted into searchable tokens:

Example:

Input: Python is a programming language

Output:
[
"python",
"programming",
"language"
]


### 3. Inverted Index

The search engine creates a word-to-document mapping.

Example:
python → python.txt
database → database.txt


### 4. TF-IDF Ranking

The engine calculates the importance of words using:
TF-IDF = Term Frequency × Inverse Document Frequency


### 5. Similarity Ranking

Cosine similarity compares the query vector with document vectors and ranks the closest matches.


## Installation

Clone the repository:
git clone <repository-url>

Navigate into the project:
cd mini-search-engine


Run the application:
python3 main.py


## Usage

Example:
============================
MINI SEARCH ENGINE
Loading documents...
Indexed 6 documents.
Enter query:

Search:
python

Output:
Results:
python
Score: 0.1569


## Project Structure
mini-search-engine/
├── data/
│
├── engine/
│ ├── document_loader.py
│ ├── tokenizer.py
│ ├── inverted_index.py
│ ├── tfidf.py
│ ├── similarity.py
│ └── search_engine.py
│
├── tests/
│
├── main.py
├── requirements.txt
└── README.md


## Technologies Used

- Python 3
- Object-Oriented Programming
- Information Retrieval Algorithms
- TF-IDF
- Cosine Similarity
- Data Structures


## Future Improvements

- Web interface using Flask/FastAPI
- Support PDF and web documents
- Query suggestions
- Spell correction
- Search result highlighting
- Better ranking algorithms


## Author

Sowmya HR