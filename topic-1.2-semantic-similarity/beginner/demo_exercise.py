"""
Topic 1.2 - Beginner Demo Exercise
Cosine Similarity from Scratch

Learning Goals:
- Understand cosine similarity formula
- Implement from scratch using numpy
- Compare with sklearn implementation
- Interpret similarity scores

TODO: Implement cosine similarity calculation
"""

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity as sklearn_cosine


def cosine_similarity_manual(vec_a, vec_b):
    """
    Calculate cosine similarity between two vectors
    
    Formula: cos(θ) = (A · B) / (||A|| × ||B||)
    
    TODO: Implement the formula
    1. Calculate dot product (A · B)
    2. Calculate magnitudes ||A|| and ||B||
    3. Return dot product / (magnitude_a * magnitude_b)
    
    Hint: Use np.dot() and np.linalg.norm()
    """
    pass


def text_to_vector(text, vocabulary):
    """
    Convert text to vector using simple word counts
    
    TODO: Create a vector where each dimension represents word count
    Vector[i] = count of vocabulary[i] in text
    """
    pass


def main():
    print("=" * 70)
    print("COSINE SIMILARITY DEMONSTRATION")
    print("=" * 70)
    
    # Sample document pairs
    doc_pairs = [
        ("the cat sat on the mat", "the cat lay on the rug"),
        ("machine learning is fun", "deep learning is interesting"),
        ("python programming", "java programming"),
        ("apple orange banana", "car truck bus")
    ]
    
    print("\n" + "=" * 70)
    print("STEP 1: Manual Implementation")
    print("=" * 70)
    
    for doc1, doc2 in doc_pairs:
        print(f"\nDocument 1: \"{doc1}\"")
        print(f"Document 2: \"{doc2}\"")
        
        # TODO: Create vocabulary
        words = set(doc1.split()) | set(doc2.split())
        vocabulary = sorted(list(words))
        
        # TODO: Convert to vectors
        vec1 = text_to_vector(doc1, vocabulary)
        vec2 = text_to_vector(doc2, vocabulary)
        
        # TODO: Calculate cosine similarity
        similarity = cosine_similarity_manual(vec1, vec2)
        
        print(f"Vocabulary: {vocabulary}")
        print(f"Vector 1: {vec1}")
        print(f"Vector 2: {vec2}")
        print(f"Cosine Similarity: {similarity:.4f}")
        
        # Interpretation
        if similarity > 0.7:
            interpretation = "Very similar"
        elif similarity > 0.4:
            interpretation = "Somewhat similar"
        else:
            interpretation = "Not similar"
        print(f"Interpretation: {interpretation}")
    
    # TODO: Compare with sklearn
    print("\n" + "=" * 70)
    print("STEP 2: Comparison with sklearn")
    print("=" * 70)
    
    # Use all documents
    all_docs = [doc for pair in doc_pairs for doc in pair]
    
    # TODO: Vectorize using CountVectorizer
    vectorizer = CountVectorizer()
    vectors = vectorizer.fit_transform(all_docs)
    
    # TODO: Calculate similarity matrix
    similarity_matrix = sklearn_cosine(vectors)
    
    print("\nSimilarity Matrix:")
    print(similarity_matrix)
    
    # TODO: Key insights
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("1. Cosine similarity ranges from -1 to 1")
    print("2. 1 = identical direction (very similar)")
    print("3. 0 = orthogonal (unrelated)")
    print("4. -1 = opposite direction (rare in text)")
    print("5. Cosine ignores magnitude - only cares about direction")


if __name__ == "__main__":
    main()
