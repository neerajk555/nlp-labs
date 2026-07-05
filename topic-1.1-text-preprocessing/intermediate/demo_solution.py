"""
Topic 1.1 - Intermediate Demo Solution
TF-IDF from Scratch vs sklearn

This solution implements TF-IDF from first principles
and compares it with sklearn's implementation.
"""

import math
from collections import Counter
import numpy as np


def compute_tf(document):
    """
    Compute Term Frequency for a document
    
    TF(t, d) = (Number of times term t appears in document d) / (Total terms in document d)
    
    This normalizes for document length - longer documents don't
    automatically get higher scores.
    """
    words = document.split()
    word_count = len(words)
    word_freq = Counter(words)
    
    # Normalize by document length
    tf_scores = {word: count / word_count for word, count in word_freq.items()}
    
    return tf_scores


def compute_idf(documents):
    """
    Compute Inverse Document Frequency across documents
    
    IDF(t) = log(Total documents / Documents containing term t)
    
    Intuition: Words appearing in fewer documents are more informative
    - If a word appears in all documents: IDF ≈ 0 (log(N/N) = log(1) = 0)
    - If a word appears in 1 document: IDF = log(N) (maximum)
    """
    num_docs = len(documents)
    
    # Count document frequency for each word
    doc_freq = Counter()
    for doc in documents:
        unique_words = set(doc.split())
        for word in unique_words:
            doc_freq[word] += 1
    
    # Calculate IDF scores
    idf_scores = {}
    for word, freq in doc_freq.items():
        # Add smoothing to avoid division by zero (though not needed here)
        idf_scores[word] = math.log(num_docs / freq)
    
    return idf_scores


def compute_tfidf(documents):
    """
    Compute TF-IDF vectors for all documents
    
    TF-IDF(t, d) = TF(t, d) × IDF(t)
    
    This combines:
    - How important is the word in THIS document? (TF)
    - How unique is the word across ALL documents? (IDF)
    """
    # Compute IDF once for all documents
    idf_scores = compute_idf(documents)
    
    tfidf_vectors = []
    for doc in documents:
        tf_scores = compute_tf(doc)
        
        # Multiply TF × IDF
        tfidf = {word: tf * idf_scores[word] for word, tf in tf_scores.items()}
        tfidf_vectors.append(tfidf)
    
    return tfidf_vectors


def compare_with_sklearn(documents):
    """Compare custom TF-IDF with sklearn implementation"""
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    # Custom implementation
    custom_tfidf = compute_tfidf(documents)
    
    # Sklearn implementation
    vectorizer = TfidfVectorizer()
    sklearn_tfidf = vectorizer.fit_transform(documents)
    
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
    print("TF-IDF IMPLEMENTATION FROM SCRATCH")
    print("=" * 70)
    
    print("\nDocuments:")
    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc}")
    
    # Demonstrate TF calculation
    print("\n" + "=" * 70)
    print("STEP 1: TERM FREQUENCY (TF) - Document 1")
    print("=" * 70)
    
    doc1_tf = compute_tf(documents[0])
    print(f"\nDocument 1: \"{documents[0]}\"")
    print(f"Total words: {len(documents[0].split())}")
    print("\nTF scores (normalized by document length):")
    for word, score in sorted(doc1_tf.items()):
        count = documents[0].split().count(word)
        print(f"  {word:<15} appears {count}x → TF = {score:.4f}")
    
    print("\n💡 'the' has high TF because it appears twice (2/6 = 0.333)")
    
    # Demonstrate IDF calculation
    print("\n" + "=" * 70)
    print("STEP 2: INVERSE DOCUMENT FREQUENCY (IDF)")
    print("=" * 70)
    
    idf_scores = compute_idf(documents)
    print("\nIDF scores (across all documents):")
    print(f"Total documents: {len(documents)}\n")
    
    for word, score in sorted(idf_scores.items(), key=lambda x: x[1], reverse=True):
        doc_count = sum(1 for doc in documents if word in doc)
        print(f"  {word:<15} appears in {doc_count}/{len(documents)} docs → IDF = {score:.4f}")
    
    print("\n💡 Interpretation:")
    print("   High IDF (>1.0): Rare, informative words (enemies, comfortable)")
    print("   Low IDF (<0.5): Common words (the, sat)")
    print("   Words in all docs: IDF → 0 (not discriminative)")
    
    # Compute TF-IDF
    print("\n" + "=" * 70)
    print("STEP 3: TF-IDF = TF × IDF")
    print("=" * 70)
    
    tfidf_scores = compute_tfidf(documents)
    
    for i, (doc, scores) in enumerate(zip(documents, tfidf_scores), 1):
        print(f"\nDocument {i}: \"{doc}\"")
        # Sort by TF-IDF score
        top_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
        print("  Keywords ranked by TF-IDF:")
        for word, score in top_words:
            tf = compute_tf(doc)[word]
            idf = idf_scores[word]
            print(f"    {word:<15} TF={tf:.3f} × IDF={idf:.3f} = {score:.4f}")
    
    print("\n💡 Notice:")
    print("   - Common words ('the', 'on') have low TF-IDF")
    print("   - Unique keywords ('comfortable', 'enemies') have high TF-IDF")
    print("   - This makes TF-IDF great for keyword extraction!")
    
    # Compare with sklearn
    print("\n" + "=" * 70)
    print("COMPARISON WITH SKLEARN")
    print("=" * 70)
    
    custom, sklearn_result, vectorizer = compare_with_sklearn(documents)
    
    print(f"\nSklearn TF-IDF matrix shape: {sklearn_result.shape}")
    print(f"  {sklearn_result.shape[0]} documents × {sklearn_result.shape[1]} features")
    
    feature_names = vectorizer.get_feature_names_out()
    print(f"\nFeature names (vocabulary): {list(feature_names)}")
    
    print("\nSklearn TF-IDF for Document 1:")
    doc1_sklearn = sklearn_result[0].toarray()[0]
    for word, score in zip(feature_names, doc1_sklearn):
        if score > 0:
            print(f"  {word:<15} {score:.4f}")
    
    print("\n⚠️  Slight differences from our implementation:")
    print("   - sklearn uses L2 normalization (unit vectors)")
    print("   - sklearn uses smoothed IDF: log((1+N)/(1+df)) + 1")
    print("   - Our version: simpler, more interpretable")
    print("   - Both capture same concept: rare words get higher weights")
    
    # Practical application
    print("\n" + "=" * 70)
    print("PRACTICAL APPLICATION: KEYWORD EXTRACTION")
    print("=" * 70)
    
    document = "Python is a great programming language for machine learning and data science"
    corpus = documents + [document]
    
    tfidf_result = compute_tfidf(corpus)
    doc_tfidf = tfidf_result[-1]
    
    print(f"\nNew document: \"{document}\"")
    print("\nTop 5 keywords:")
    for word, score in sorted(doc_tfidf.items(), key=lambda x: x[1], reverse=True)[:5]:
        print(f"  {word:<20} {score:.4f}")
    
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("✓ TF-IDF balances local (document) and global (corpus) importance")
    print("✓ Automatically downweights common words without stopword list")
    print("✓ Works well for: keyword extraction, document ranking, search")
    print("✓ Limitation: Still no semantic understanding (like BoW)")
    print("✓ Next step: Word embeddings for semantic similarity")


if __name__ == "__main__":
    main()
