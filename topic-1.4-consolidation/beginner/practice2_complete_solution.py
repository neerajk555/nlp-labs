"""
Topic 1.4 - Beginner Practice 2 Solution
Building a Simple RAG Pipeline

Complete implementation of a basic RAG system with chunking,
embedding, retrieval, and generation using Azure OpenAI.
"""

from openai import AzureOpenAI
import numpy as np
from dotenv import load_dotenv
import os
from typing import List

# Load environment variables
load_dotenv()


def chunk_document(text: str, chunk_size: int = 200, overlap: int = 50) -> List[str]:
    """
    Split document into overlapping chunks
    
    Simple character-based chunking with overlap to maintain context
    at chunk boundaries.
    """
    chunks = []
    start = 0
    text = text.strip()
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        
        # Try to break at sentence boundary
        if end < len(text):
            last_period = chunk.rfind('.')
            last_newline = chunk.rfind('\n')
            break_point = max(last_period, last_newline)
            
            if break_point > 0:
                end = start + break_point + 1
                chunk = text[start:end]
        
        chunks.append(chunk.strip())
        start = end - overlap
    
    return [c for c in chunks if c]  # Remove empty chunks


def get_embeddings(texts: List[str], client: AzureOpenAI) -> np.ndarray:
    """
    Get embeddings for text chunks using Azure OpenAI
    
    Batches requests for efficiency
    """
    deployment = os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT", "text-embedding-ada-002")
    
    embeddings = []
    for text in texts:
        response = client.embeddings.create(
            model=deployment,
            input=text
        )
        embeddings.append(response.data[0].embedding)
    
    return np.array(embeddings)


def cosine_similarity(a: np.ndarray, b: np.ndarray) -> float:
    """Calculate cosine similarity between two vectors"""
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def retrieve_relevant_chunks(query: str, chunks: List[str], embeddings: np.ndarray, 
                             client: AzureOpenAI, top_k: int = 3) -> List[str]:
    """
    Retrieve most relevant chunks for query using semantic similarity
    """
    # Get query embedding
    query_embedding = get_embeddings([query], client)[0]
    
    # Calculate similarities
    similarities = []
    for i, chunk_embedding in enumerate(embeddings):
        sim = cosine_similarity(query_embedding, chunk_embedding)
        similarities.append((i, sim))
    
    # Sort by similarity and get top_k
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_indices = [idx for idx, _ in similarities[:top_k]]
    
    return [chunks[i] for i in top_indices]


def generate_answer(query: str, context_chunks: List[str], client: AzureOpenAI) -> str:
    """
    Generate answer using retrieved context
    
    Constructs a prompt with context and uses GPT to generate answer
    """
    deployment = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4")
    
    # Build context from chunks
    context = "\n\n".join(context_chunks)
    
    # Create prompt
    prompt = f"""Use the following context to answer the question. If the answer is not in the context, say "I don't have enough information to answer this question."

Context:
{context}

Question: {query}

Answer:"""
    
    # Call GPT
    response = client.chat.completions.create(
        model=deployment,
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions based on provided context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3,
        max_tokens=200
    )
    
    return response.choices[0].message.content


def simple_rag_pipeline(query: str, document: str, client: AzureOpenAI, 
                       chunk_size: int = 200, top_k: int = 3) -> dict:
    """
    Complete RAG pipeline
    
    Returns dictionary with answer and metadata for transparency
    """
    # Step 1: Chunk document
    chunks = chunk_document(document, chunk_size=chunk_size)
    print(f"  → Created {len(chunks)} chunks")
    
    # Step 2: Embed chunks
    embeddings = get_embeddings(chunks, client)
    print(f"  → Generated embeddings (shape: {embeddings.shape})")
    
    # Step 3: Retrieve relevant chunks
    relevant_chunks = retrieve_relevant_chunks(query, chunks, embeddings, client, top_k=top_k)
    print(f"  → Retrieved {len(relevant_chunks)} relevant chunks")
    
    # Step 4: Generate answer
    answer = generate_answer(query, relevant_chunks, client)
    
    return {
        "answer": answer,
        "relevant_chunks": relevant_chunks,
        "total_chunks": len(chunks)
    }


def main():
    """Main execution with complete implementation"""
    print("=" * 70)
    print("SIMPLE RAG PIPELINE - COMPLETE DEMONSTRATION")
    print("=" * 70)
    
    # Initialize Azure OpenAI client
    try:
        client = AzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("AZURE_OPENAI_API_VERSION", "2024-02-15-preview"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        print("\n✓ Azure OpenAI client initialized")
    except Exception as e:
        print(f"\n✗ Error initializing Azure OpenAI client: {e}")
        print("  Please check your .env file configuration")
        return
    
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
    
    print("\nKnowledge Base:")
    print(f"  Length: {len(document)} characters")
    print(f"  Preview: {document[:150]}...")
    
    # Process each query
    print("\n" + "=" * 70)
    print("RAG PIPELINE RESULTS")
    print("=" * 70)
    
    for i, query in enumerate(queries, 1):
        print(f"\n{'─' * 70}")
        print(f"Query {i}: {query}")
        print('─' * 70)
        
        try:
            result = simple_rag_pipeline(query, document, client, chunk_size=200, top_k=2)
            
            print(f"\n✓ Answer: {result['answer']}")
            
            print(f"\n  Retrieved chunks ({len(result['relevant_chunks'])}):")
            for j, chunk in enumerate(result['relevant_chunks'], 1):
                print(f"    {j}. {chunk[:100]}...")
        
        except Exception as e:
            print(f"\n✗ Error: {e}")
    
    # Demonstrate chunking strategies
    print("\n" + "=" * 70)
    print("CHUNKING STRATEGY COMPARISON")
    print("=" * 70)
    
    chunk_sizes = [100, 200, 400]
    sample_query = queries[0]
    
    print(f"\nQuery: '{sample_query}'")
    print("\nChunk Size Impact:")
    
    for size in chunk_sizes:
        chunks = chunk_document(document, chunk_size=size, overlap=50)
        print(f"  {size} chars: {len(chunks)} chunks created")
        print(f"    Example chunk: {chunks[0][:80]}...")
    
    # Key insights
    print("\n" + "=" * 70)
    print("KEY INSIGHTS & BEST PRACTICES")
    print("=" * 70)
    
    print("\n✓ RAG Architecture:")
    print("  1. Chunk documents into manageable pieces")
    print("  2. Embed chunks using semantic embeddings")
    print("  3. Retrieve relevant chunks via similarity search")
    print("  4. Generate answer with LLM using retrieved context")
    
    print("\n✓ Chunking Strategy:")
    print("  - Too small: Loss of context")
    print("  - Too large: Irrelevant information in prompt")
    print("  - Overlap: Maintains context at boundaries")
    print("  - Typical size: 200-500 tokens")
    
    print("\n✓ Retrieval Optimization:")
    print("  - Use top-k to balance context vs noise (k=2-5 typical)")
    print("  - Consider hybrid search (keyword + semantic)")
    print("  - Re-rank results with cross-encoder for accuracy")
    
    print("\n✓ Generation Quality:")
    print("  - Lower temperature (0.0-0.3) for factual answers")
    print("  - Instruct model to say 'I don't know' if uncertain")
    print("  - Include source attribution for transparency")
    
    print("\n✓ Production Considerations:")
    print("  - Cache embeddings to reduce API calls")
    print("  - Use vector databases (FAISS, Pinecone) for scale")
    print("  - Monitor retrieval quality and LLM costs")
    print("  - Implement fallback for API failures")


if __name__ == "__main__":
    main()
