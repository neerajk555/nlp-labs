"""
Topic 1.1 - Intermediate Demo Exercise
TF-IDF from Scratch vs sklearn

Learning Goals:
- Understand TF-IDF formula and intuition
- Implement TF-IDF from scratch
- Compare with sklearn's TfidfVectorizer
- Interpret TF-IDF scores

TODO: Implement TF-IDF calculation functions
"""

import math
from collections import Counter
import numpy as np


def compute_tf(document):
    """
    Compute Term Frequency for a document
    
    TF(t, d) = (Number of times term t appears in document d) / (Total terms in document d)
    
    TODO: 
    1. Count word occurrences in document
    2. Calculate total words
    3. Return dictionary of {word: tf_score}
    """
    pass


def compute_idf(documents):
    """
    Compute Inverse Document Frequency across documents
    
    IDF(t) = log(Total documents / Documents containing term t)
    
    TODO:
    1. Count how many documents each term appears in
    2. Calculate IDF score for each term
    3. Return dictionary of {word: idf_score}
    
    Hint: Use math.log() for logarithm
    """
    pass


def compute_tfidf(documents):
    """
    Compute TF-IDF vectors for all documents
    
    TF-IDF(t, d) = TF(t, d) × IDF(t)
    
    TODO:
    1. Compute IDF scores for all terms
    2. For each document:
       - Compute TF scores
       - Multiply TF × IDF for each term
    3. Return list of TF-IDF dictionaries
    """
    pass


def compare_with_sklearn(documents):
    """
    Compare custom TF-IDF with sklearn implementation
    
    TODO:
    1. Compute TF-IDF using custom implementation
    2. Compute TF-IDF using sklearn
    3. Compare results
    """
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    # TODO: Use custom implementation
    custom_tfidf = None
    
    # TODO: Use sklearn
    vectorizer = TfidfVectorizer()
    sklearn_tfidf = None
    
    return custom_tfidf, sklearn_tfidf, vectorizer


def main():
    # Sample documents
    documents = [
        "the cat sat on the mat",
        "the dog sat on the log",
        "cats and dogs are enemies",
        "the mat is comfortable"
    ]
    
    print("=" * 70)
    print("TF-IDF IMPLEMENTATION")
    print("=" * 70)
    
    print("\nDocuments:")
    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc}")
    
    # TODO: Compute TF for first document
    print("\n" + "=" * 70)
    print("TERM FREQUENCY (TF) - Document 1")
    print("=" * 70)
    
    doc1_tf = compute_tf(documents[0])
    print("\nTF scores (Document 1):")
    for word, score in sorted(doc1_tf.items()):
        print(f"  {word:<15} {score:.4f}")
    
    # TODO: Compute IDF across all documents
    print("\n" + "=" * 70)
    print("INVERSE DOCUMENT FREQUENCY (IDF)")
    print("=" * 70)
    
    idf_scores = compute_idf(documents)
    print("\nIDF scores (across all documents):")
    for word, score in sorted(idf_scores.items(), key=lambda x: x[1], reverse=True):
        print(f"  {word:<15} {score:.4f}")
    
    print("\n💡 Interpretation:")
    print("   High IDF = rare word (appears in few documents)")
    print("   Low IDF = common word (appears in many documents)")
    
    # TODO: Compute TF-IDF for all documents
    print("\n" + "=" * 70)
    print("TF-IDF SCORES")
    print("=" * 70)
    
    tfidf_scores = compute_tfidf(documents)
    
    for i, (doc, scores) in enumerate(zip(documents, tfidf_scores), 1):
        print(f"\nDocument {i}: \"{doc}\"")
        # Sort by TF-IDF score
        top_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:5]
        print("  Top 5 keywords (by TF-IDF):")
        for word, score in top_words:
            print(f"    {word:<15} {score:.4f}")
    
    # TODO: Compare with sklearn
    print("\n" + "=" * 70)
    print("COMPARISON WITH SKLEARN")
    print("=" * 70)
    
    custom, sklearn_result, vectorizer = compare_with_sklearn(documents)
    
    # TODO: Display comparison
    print("\nSklearn TF-IDF shape:", sklearn_result.shape)
    print("Feature names:", vectorizer.get_feature_names_out()[:10], "...")
    
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("1. TF-IDF upweights rare, informative words")
    print("2. TF-IDF downweights common words like 'the', 'is', 'and'")
    print("3. Higher TF-IDF = more important keyword for that document")
    print("4. Useful for: keyword extraction, document ranking, search")


if __name__ == "__main__":
    main()
