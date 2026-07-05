"""
Topic 1.1 - Intermediate Practice 2
Word2Vec Training and Exploration

Learning Goals:
- Train Word2Vec from scratch on custom corpus
- Understand CBOW vs Skip-gram architectures
- Explore semantic relationships in embeddings
- Compare with pre-trained embeddings

TODO: Implement Word2Vec training and analysis
"""

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity


# Sample corpus for training
CORPUS = [
    "the cat sat on the mat",
    "the dog sat on the log",
    "cats and dogs are animals",
    "the mat is comfortable",
    "dogs love to play outside",
    "cats love to sleep inside",
    "animals need food and water",
    "the comfortable mat is soft",
    "dogs are loyal pets",
    "cats are independent pets"
] * 100  # Repeat for better training


def prepare_corpus(sentences):
    """
    Prepare corpus for Word2Vec training
    
    TODO:
    1. Tokenize each sentence
    2. Lowercase all words
    3. Return list of token lists
    
    Format: [['the', 'cat', 'sat'], ['the', 'dog', 'sat'], ...]
    """
    pass


def train_word2vec(sentences, vector_size=50, window=5, min_count=1, 
                   sg=0, epochs=100):
    """
    Train Word2Vec model
    
    TODO:
    1. Initialize Word2Vec with given parameters
    2. Train model on sentences
    3. Return trained model
    
    Parameters:
    - vector_size: Dimensionality of word vectors
    - window: Maximum distance between current and predicted word
    - min_count: Minimum word frequency
    - sg: Training algorithm (0=CBOW, 1=Skip-gram)
    - epochs: Number of training iterations
    """
    pass


def explore_embeddings(model):
    """
    Explore learned word embeddings
    
    TODO:
    1. Find most similar words
    2. Perform word arithmetic (king - man + woman = ?)
    3. Calculate word similarities
    4. Identify odd-one-out
    """
    print("=" * 70)
    print("EXPLORING WORD EMBEDDINGS")
    print("=" * 70)
    
    # TODO: Get vocabulary
    vocab = list(model.wv.key_to_index.keys())
    print(f"\nVocabulary size: {len(vocab)}")
    print(f"Sample words: {vocab[:10]}")
    
    # TODO: Find similar words
    print("\n" + "-" * 70)
    print("SIMILAR WORDS")
    print("-" * 70)
    
    test_words = ['cat', 'dog', 'comfortable']
    for word in test_words:
        if word in model.wv:
            # TODO: Find top 5 similar words
            similar = None
            print(f"\nMost similar to '{word}':")
            for sim_word, score in similar:
                print(f"  {sim_word:<15} {score:.4f}")
    
    # TODO: Word arithmetic
    print("\n" + "-" * 70)
    print("WORD ARITHMETIC")
    print("-" * 70)
    
    # Try: dog - dogs + cats = ?
    try:
        result = None  # Calculate: dog - dogs + cats
        print("\ndog - dogs + cats = ?")
        for word, score in result[:5]:
            print(f"  {word:<15} {score:.4f}")
    except Exception as e:
        print(f"Error: {e}")
    
    # TODO: Calculate similarity between word pairs
    print("\n" + "-" * 70)
    print("WORD PAIR SIMILARITIES")
    print("-" * 70)
    
    word_pairs = [
        ('cat', 'dog'),
        ('cat', 'animal'),
        ('mat', 'comfortable'),
        ('cat', 'water')
    ]
    
    for word1, word2 in word_pairs:
        if word1 in model.wv and word2 in model.wv:
            # TODO: Calculate cosine similarity
            sim = None
            print(f"  {word1} <-> {word2}: {sim:.4f}")


def compare_cbow_vs_skipgram(sentences):
    """
    Compare CBOW vs Skip-gram architectures
    
    TODO:
    1. Train both CBOW and Skip-gram models
    2. Compare their embeddings
    3. Analyze differences
    """
    pass


def visualize_embeddings(model, words):
    """
    Visualize embeddings using dimensionality reduction
    
    TODO (Optional - requires matplotlib):
    1. Extract embedding vectors for given words
    2. Reduce to 2D using PCA or t-SNE
    3. Create scatter plot
    """
    pass


def main():
    print("=" * 70)
    print("WORD2VEC TRAINING DEMONSTRATION")
    print("=" * 70)
    
    # TODO: Prepare corpus
    sentences = prepare_corpus(CORPUS)
    print(f"\nCorpus prepared: {len(sentences)} sentences")
    print(f"Sample: {sentences[0]}")
    
    # TODO: Train Word2Vec model (CBOW)
    print("\n" + "=" * 70)
    print("TRAINING WORD2VEC (CBOW)")
    print("=" * 70)
    
    model_cbow = train_word2vec(
        sentences,
        vector_size=50,
        window=5,
        min_count=2,
        sg=0,  # CBOW
        epochs=100
    )
    
    print(f"✓ Model trained!")
    print(f"  Vector size: {model_cbow.vector_size}")
    print(f"  Vocabulary size: {len(model_cbow.wv)}")
    
    # TODO: Explore embeddings
    explore_embeddings(model_cbow)
    
    # TODO: Compare CBOW vs Skip-gram
    print("\n" + "=" * 70)
    print("CBOW VS SKIP-GRAM COMPARISON")
    print("=" * 70)
    
    compare_cbow_vs_skipgram(sentences)
    
    # TODO: Key insights
    print("\n" + "=" * 70)
    print("KEY INSIGHTS")
    print("=" * 70)
    print("\n1. Word2Vec captures semantic similarity (cat ~ dog)")
    print("2. Context window determines what's considered 'similar'")
    print("3. CBOW: Faster training, good for frequent words")
    print("4. Skip-gram: Better for rare words, larger vocab")
    print("5. Larger corpus → better embeddings")
    print("6. In production: Use pre-trained embeddings (GloVe, FastText)")


if __name__ == "__main__":
    main()
