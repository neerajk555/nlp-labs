"""
Topic 1.1 - Beginner Practice 2 Solution
Bag of Words (BoW) Implementation

This solution implements a complete BoW system from scratch
and demonstrates its strengths and limitations.
"""

from collections import Counter
import string


class BagOfWords:
    """
    Simple Bag of Words implementation
    
    Converts text documents into fixed-length vectors based on word counts.
    Each dimension represents a word in the vocabulary.
    """
    
    def __init__(self):
        self.vocabulary = {}  # Maps word -> index
        self.word_counts = {}  # Maps word -> document frequency
    
    def fit(self, documents):
        """
        Build vocabulary from documents
        
        Steps:
        1. Collect all unique words across documents
        2. Assign sequential indices to words (sorted for consistency)
        3. Count document frequency for each word
        """
        # Collect all words
        all_words = set()
        for doc in documents:
            words = doc.split()
            all_words.update(words)
        
        # Build vocabulary with sorted words (for reproducibility)
        self.vocabulary = {word: idx for idx, word in enumerate(sorted(all_words))}
        
        # Count document frequency (number of docs containing each word)
        self.word_counts = Counter()
        for doc in documents:
            unique_words = set(doc.split())
            for word in unique_words:
                self.word_counts[word] += 1
    
    def transform(self, documents):
        """
        Convert documents to BoW vectors
        
        Each vector has length = vocabulary size
        Vector[i] = count of word at index i in the document
        """
        vectors = []
        vocab_size = len(self.vocabulary)
        
        for doc in documents:
            # Initialize zero vector
            vector = [0] * vocab_size
            
            # Count words in document
            word_counts = Counter(doc.split())
            
            # Fill vector with counts
            for word, count in word_counts.items():
                if word in self.vocabulary:
                    idx = self.vocabulary[word]
                    vector[idx] = count
            
            vectors.append(vector)
        
        return vectors
    
    def fit_transform(self, documents):
        """Convenience method: fit and transform in one step"""
        self.fit(documents)
        return self.transform(documents)
    
    def get_feature_names(self):
        """
        Return list of words in vocabulary order
        
        Useful for interpreting vectors
        """
        # Sort by index to get words in order
        sorted_vocab = sorted(self.vocabulary.items(), key=lambda x: x[1])
        return [word for word, idx in sorted_vocab]


def simple_preprocess(text):
    """Basic preprocessing for BoW"""
    # Lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split into words
    return text.split()


def main():
    # Sample documents
    documents = [
        "I love machine learning",
        "Machine learning is amazing",
        "I love deep learning",
        "Deep learning is a subset of machine learning"
    ]
    
    print("=" * 70)
    print("BAG OF WORDS DEMONSTRATION")
    print("=" * 70)
    
    # Preprocess documents
    processed_docs = [" ".join(simple_preprocess(doc)) for doc in documents]
    
    print("\nOriginal documents:")
    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc}")
    
    print("\nProcessed documents:")
    for i, doc in enumerate(processed_docs, 1):
        print(f"{i}. {doc}")
    
    # Create and fit BoW
    bow = BagOfWords()
    bow.fit(processed_docs)
    
    # Get vocabulary
    vocab = bow.get_feature_names()
    print(f"\nVocabulary (size={len(vocab)}):")
    print(vocab)
    
    # Transform documents to vectors
    vectors = bow.transform(processed_docs)
    
    print("\n" + "=" * 70)
    print("BOW VECTORS")
    print("=" * 70)
    print("\nEach vector shows word counts in vocabulary order")
    print(f"Vector length = vocabulary size = {len(vocab)}\n")
    
    print(f"{'Document':<45} {'Vector'}")
    print("-" * 70)
    for doc, vec in zip(documents, vectors):
        print(f"{doc:<45} {vec}")
    
    # Show vocabulary mapping
    print("\n" + "=" * 70)
    print("VOCABULARY MAPPING")
    print("=" * 70)
    print("\nWord → Position in vector\n")
    for word, idx in sorted(bow.vocabulary.items(), key=lambda x: x[1]):
        doc_freq = bow.word_counts[word]
        print(f"  {word:<15} → index {idx}  (appears in {doc_freq} documents)")
    
    # Demonstrate BoW limitations
    print("\n" + "=" * 70)
    print("BOW LIMITATIONS DEMONSTRATION")
    print("=" * 70)
    
    # These sentences have different meanings but identical BoW
    sent1 = "dog bites man"
    sent2 = "man bites dog"
    
    print(f"\nSentence 1: \"{sent1}\"")
    print(f"Sentence 2: \"{sent2}\"")
    print("\n⚠️  These have VERY different meanings!")
    print("   Sentence 1: Normal occurrence")
    print("   Sentence 2: Newsworthy event!")
    
    # Show their BoW representations
    bow_temp = BagOfWords()
    vecs = bow_temp.fit_transform([sent1, sent2])
    
    print(f"\nVocabulary: {bow_temp.get_feature_names()}")
    print(f"BoW vector for sentence 1: {vecs[0]}")
    print(f"BoW vector for sentence 2: {vecs[1]}")
    print(f"\n❌ Vectors are identical: {vecs[0] == vecs[1]}")
    print("   → BoW completely loses word order!")
    
    # Additional limitation: no semantics
    print("\n" + "-" * 70)
    print("SEMANTIC LIMITATION")
    print("-" * 70)
    
    sent3 = "The movie was good"
    sent4 = "The movie was excellent"
    sent5 = "The movie was terrible"
    
    bow_sem = BagOfWords()
    vecs_sem = bow_sem.fit_transform([sent3, sent4, sent5])
    
    print(f"\nSentence 3: \"{sent3}\"")
    print(f"Sentence 4: \"{sent4}\"")
    print(f"Sentence 5: \"{sent5}\"")
    
    print(f"\nVectors:")
    for sent, vec in zip([sent3, sent4, sent5], vecs_sem):
        print(f"  {sent:<30} {vec}")
    
    print("\n❌ 'good' and 'excellent' are treated as completely different")
    print("❌ 'good' and 'terrible' have same distance as 'good' and 'excellent'")
    print("   → BoW has no semantic understanding!")
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS")
    print("=" * 70)
    print("✓ BoW strengths:")
    print("  - Simple to implement and understand")
    print("  - Works well for simple classification tasks")
    print("  - Fast and memory-efficient")
    print()
    print("✗ BoW limitations:")
    print("  - Loses word order ('dog bites man' = 'man bites dog')")
    print("  - No semantic understanding ('good' ≠ 'excellent')")
    print("  - High dimensionality (vocab size can be huge)")
    print("  - Sparse vectors (most values are 0)")
    print()
    print("💡 Solutions:")
    print("  - TF-IDF: Weight words by importance")
    print("  - Word embeddings: Capture semantic similarity")
    print("  - N-grams: Capture some word order (bigrams, trigrams)")


if __name__ == "__main__":
    main()
