"""
Topic 1.4 - Beginner Practice 2 Exercise
Building a Simple RAG Pipeline

Learning Goals:
- Understand basic RAG architecture
- Implement document chunking and embedding
- Build retrieval with cosine similarity
- Generate answers using Azure OpenAI

TODO: Complete the RAG pipeline implementation
"""

from openai import AzureOpenAI
import numpy as np
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


def chunk_document(text: str, chunk_size: int = 200, overlap: int = 50):
    """
    Split document into overlapping chunks
    
    TODO: Implement chunking strategy
    1. Split text into sentences or by character count
    2. Create chunks of chunk_size with overlap
    3. Return list of chunks
    """
    pass


def get_embeddings(texts: list, client: AzureOpenAI):
    """
    Get embeddings for text chunks using Azure OpenAI
    
    TODO: 
    1. Call Azure OpenAI embeddings API
    2. Extract embedding vectors
    3. Return as numpy array
    """
    pass


def retrieve_relevant_chunks(query: str, chunks: list, embeddings: np.ndarray, 
                             client: AzureOpenAI, top_k: int = 3):
    """
    Retrieve most relevant chunks for query
    
    TODO:
    1. Get query embedding
    2. Calculate cosine similarity with all chunk embeddings
    3. Return top_k most similar chunks
    """
    pass


def generate_answer(query: str, context_chunks: list, client: AzureOpenAI):
    """
    Generate answer using retrieved context
    
    TODO:
    1. Build prompt with context and query
    2. Call Azure OpenAI chat completion
    3. Return generated answer
    """
    pass


def simple_rag_pipeline(query: str, document: str, client: AzureOpenAI):
    """
    Complete RAG pipeline
    
    TODO: Orchestrate all steps:
    1. Chunk document
    2. Embed chunks
    3. Retrieve relevant chunks
    4. Generate answer
    """
    pass


def main():
    """Main execution function"""
    print("=" * 70)
    print("SIMPLE RAG PIPELINE DEMONSTRATION")
    print("=" * 70)
    
    # TODO: Initialize Azure OpenAI client
    client = None
    
    # Sample knowledge base
    document = """
    Python is a high-level programming language known for its simplicity and readability.
    It was created by Guido van Rossum and first released in 1991.
    Python supports multiple programming paradigms including procedural, object-oriented, and functional programming.
    
    Machine learning is a subset of artificial intelligence that enables systems to learn from data.
    Python has become the dominant language for machine learning due to libraries like scikit-learn, TensorFlow, and PyTorch.
    These libraries provide tools for data preprocessing, model training, and evaluation.
    
    Natural Language Processing (NLP) is a field of AI focused on enabling computers to understand human language.
    Python's NLTK and spaCy libraries are widely used for NLP tasks.
    Modern NLP relies heavily on deep learning and transformer models like BERT and GPT.
    
    Data science involves extracting insights from data using statistical and computational techniques.
    Python's pandas and numpy libraries are essential for data manipulation and numerical computing.
    Visualization libraries like matplotlib and seaborn help present findings effectively.
    """
    
    # Test queries
    queries = [
        "Who created Python?",
        "What libraries are used for machine learning in Python?",
        "What is NLP?",
        "What are pandas used for?"
    ]
    
    print("\nKnowledge Base Preview:")
    print(document[:200] + "...")
    
    # TODO: Process each query
    print("\n" + "=" * 70)
    print("RAG PIPELINE RESULTS")
    print("=" * 70)
    
    for query in queries:
        print(f"\nQuery: {query}")
        # TODO: Run RAG pipeline
        # answer = simple_rag_pipeline(query, document, client)
        # print(f"Answer: {answer}")
    
    print("\n" + "=" * 70)
    print("KEY CONCEPTS")
    print("=" * 70)
    print("\n1. RAG = Retrieval + Generation")
    print("2. Chunking balances context size vs relevance")
    print("3. Embeddings enable semantic search")
    print("4. Context in prompt grounds LLM responses")
    print("5. RAG reduces hallucinations vs pure generation")


if __name__ == "__main__":
    main()
