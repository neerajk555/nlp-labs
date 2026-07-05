"""
Topic 1.1 - Beginner Practice 2
Bag of Words (BoW) Implementation

Learning Goals:
- Understand the Bag of Words representation
- Build a vocabulary from documents
- Convert text to BoW vectors
- Recognize BoW limitations (no word order, no semantics)

TODO: Implement the BoW class methods
"""

from collections import Counter


class BagOfWords:
    """Simple Bag of Words implementation"""
    
    def __init__(self):
        self.vocabulary = {}  # Maps word -> index
        self.word_counts = {}  # Maps word -> document frequency
    
    def fit(self, documents):
        """
        Build vocabulary from documents
        
        TODO:
        1. Extract all unique words from all documents
        2. Assign each word a unique index
        3. Count how many documents each word appears in
        
        Args:
            documents: List of strings (documents)
        """
        pass
    
    def transform(self, documents):
        """
        Convert documents to BoW vectors
        
        TODO:
        1. For each document, count word occurrences
        2. Create a vector of size len(vocabulary)
        3. Fill vector with counts based on vocabulary indices
        
        Args:
            documents: List of strings
            
        Returns:
            List of vectors (each vector is a list of counts)
        """
        pass
    
    def fit_transform(self, documents):
        """Fit and transform in one step"""
        self.fit(documents)
        return self.transform(documents)
    
    def get_feature_names(self):
        """Return list of words in vocabulary order"""
        # TODO: Return words sorted by their index
        pass


def simple_preprocess(text):
    """Basic preprocessing for BoW"""
    # TODO: Lowercase, remove punctuation, split into words
    import string
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
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
    
    # TODO: Preprocess documents
    processed_docs = [" ".join(simple_preprocess(doc)) for doc in documents]
    
    print("\nOriginal documents:")
    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc}")
    
    # TODO: Create BoW instance and fit
    bow = BagOfWords()
    bow.fit(processed_docs)
    
    # TODO: Get vocabulary
    vocab = bow.get_feature_names()
    print(f"\nVocabulary (size={len(vocab)}):")
    print(vocab)
    
    # TODO: Transform documents to vectors
    vectors = bow.transform(processed_docs)
    
    print("\n" + "=" * 70)
    print("BOW VECTORS")
    print("=" * 70)
    
    # TODO: Display vectors in readable format
    print(f"\n{'Document':<40} {'Vector'}")
    print("-" * 70)
    for doc, vec in zip(documents, vectors):
        print(f"{doc:<40} {vec}")
    
    # TODO: Show vocabulary mapping
    print("\n" + "=" * 70)
    print("VOCABULARY MAPPING")
    print("=" * 70)
    for word, idx in sorted(bow.vocabulary.items(), key=lambda x: x[1]):
        print(f"  {word:<15} → index {idx}")
    
    # TODO: Demonstrate BoW limitations
    print("\n" + "=" * 70)
    print("BOW LIMITATIONS DEMONSTRATION")
    print("=" * 70)
    
    # These sentences have different meanings but similar BoW
    sent1 = "dog bites man"
    sent2 = "man bites dog"
    
    print(f"\nSentence 1: \"{sent1}\"")
    print(f"Sentence 2: \"{sent2}\"")
    print("\nThese have VERY different meanings!")
    
    # TODO: Show their BoW representations are identical
    bow_temp = BagOfWords()
    vecs = bow_temp.fit_transform([sent1, sent2])
    
    print(f"\nBoW vector for sentence 1: {vecs[0]}")
    print(f"BoW vector for sentence 2: {vecs[1]}")
    print(f"\nVectors are identical: {vecs[0] == vecs[1]}")
    print("→ BoW loses word order and context!")


if __name__ == "__main__":
    main()
