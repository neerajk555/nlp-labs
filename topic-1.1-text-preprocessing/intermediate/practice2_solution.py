"""
Topic 1.1 - Intermediate Practice 2 Solution
Word2Vec Training and Exploration

This solution demonstrates training Word2Vec from scratch,
exploring semantic relationships, and comparing CBOW vs Skip-gram.
"""

from gensim.models import Word2Vec
import numpy as np
from sklearn.decomposition import PCA
import warnings
warnings.filterwarnings('ignore')


# Sample corpus for training (repeated for better learning)
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
    "cats are independent pets",
    "pets need love and care",
    "water is essential for animals",
    "soft mats are comfortable",
    "loyal dogs protect their owners"
] * 100  # Repeat for sufficient training data


def prepare_corpus(sentences):
    """
    Prepare corpus for Word2Vec training
    
    Word2Vec expects list of token lists, not strings
    """
    tokenized = []
    for sentence in sentences:
        tokens = sentence.lower().split()
        tokenized.append(tokens)
    return tokenized


def train_word2vec(sentences, vector_size=50, window=5, min_count=1, 
                   sg=0, epochs=100):
    """
    Train Word2Vec model
    
    Parameters explained:
    - vector_size: Dimensionality of embeddings (50-300 typical)
    - window: Context window size (5-10 typical)
    - min_count: Ignore words appearing less than this
    - sg: 0=CBOW (predict word from context), 1=Skip-gram (predict context from word)
    - epochs: Training iterations
    """
    model = Word2Vec(
        sentences=sentences,
        vector_size=vector_size,
        window=window,
        min_count=min_count,
        sg=sg,
        epochs=epochs,
        workers=4,  # Parallel processing
        seed=42  # Reproducibility
    )
    return model


def explore_embeddings(model):
    """Explore learned word embeddings"""
    print("=" * 70)
    print("EXPLORING WORD EMBEDDINGS")
    print("=" * 70)
    
    # Get vocabulary
    vocab = list(model.wv.key_to_index.keys())
    print(f"\nVocabulary size: {len(vocab)}")
    print(f"Words in vocabulary: {sorted(vocab)}")
    
    # Find similar words
    print("\n" + "-" * 70)
    print("SEMANTIC SIMILARITY")
    print("-" * 70)
    
    test_words = ['cat', 'dog', 'comfortable', 'love']
    for word in test_words:
        if word in model.wv:
            similar = model.wv.most_similar(word, topn=5)
            print(f"\nMost similar to '{word}':")
            for sim_word, score in similar:
                print(f"  {sim_word:<15} similarity: {score:.4f}")
    
    # Word arithmetic (vector operations)
    print("\n" + "-" * 70)
    print("WORD ARITHMETIC (Analogies)")
    print("-" * 70)
    
    # Try semantic operations
    analogies = [
        (['dog', 'loyal'], ['cat'], "dog is to loyal as cat is to ?"),
        (['dogs', 'play'], ['cats'], "dogs play as cats ... ?"),
    ]
    
    for positive, negative, description in analogies:
        try:
            # Check if all words exist
            if all(w in model.wv for w in positive + negative):
                result = model.wv.most_similar(positive=positive, negative=negative, topn=3)
                print(f"\n{description}")
                print(f"  Formula: {' + '.join(positive)} - {' - '.join(negative)}")
                print(f"  Results:")
                for word, score in result:
                    print(f"    {word:<15} {score:.4f}")
        except Exception as e:
            print(f"  Could not compute: {e}")
    
    # Calculate similarity between specific word pairs
    print("\n" + "-" * 70)
    print("WORD PAIR SIMILARITIES")
    print("-" * 70)
    
    word_pairs = [
        ('cat', 'dog'),      # Related animals
        ('cat', 'cats'),     # Singular/plural
        ('mat', 'comfortable'),  # Associated concepts
        ('cat', 'water'),    # Weakly related
        ('love', 'care'),    # Synonyms
        ('inside', 'outside')  # Antonyms
    ]
    
    print("\nSemantic relatedness (0=unrelated, 1=identical):")
    for word1, word2 in word_pairs:
        if word1 in model.wv and word2 in model.wv:
            sim = model.wv.similarity(word1, word2)
            print(f"  {word1:<12} <-> {word2:<12}: {sim:.4f}")
    
    # Demonstrate embedding vector
    print("\n" + "-" * 70)
    print("EMBEDDING VECTORS")
    print("-" * 70)
    
    word = 'cat'
    if word in model.wv:
        vector = model.wv[word]
        print(f"\nEmbedding vector for '{word}':")
        print(f"  Dimensions: {len(vector)}")
        print(f"  First 10 values: {vector[:10]}")
        print(f"  Mean: {vector.mean():.4f}, Std: {vector.std():.4f}")


def compare_cbow_vs_skipgram(sentences):
    """Compare CBOW vs Skip-gram architectures"""
    print("\n" + "=" * 70)
    print("ARCHITECTURE COMPARISON: CBOW vs SKIP-GRAM")
    print("=" * 70)
    
    # Train both models
    print("\nTraining CBOW model...")
    model_cbow = train_word2vec(sentences, sg=0, epochs=100)
    
    print("Training Skip-gram model...")
    model_sg = train_word2vec(sentences, sg=1, epochs=100)
    
    print("\n" + "-" * 70)
    print("MODEL CHARACTERISTICS")
    print("-" * 70)
    
    print(f"\nCBOW:")
    print(f"  Architecture: Predicts target word from context")
    print(f"  Training: Faster (one prediction per context)")
    print(f"  Best for: Frequent words, smaller datasets")
    
    print(f"\nSkip-gram:")
    print(f"  Architecture: Predicts context words from target")
    print(f"  Training: Slower (multiple predictions per word)")
    print(f"  Best for: Rare words, larger datasets")
    
    # Compare on specific words
    print("\n" + "-" * 70)
    print("SIMILARITY COMPARISON")
    print("-" * 70)
    
    test_words = ['cat', 'dog', 'love']
    
    for word in test_words:
        if word in model_cbow.wv and word in model_sg.wv:
            print(f"\nWord: '{word}'")
            
            cbow_similar = model_cbow.wv.most_similar(word, topn=3)
            sg_similar = model_sg.wv.most_similar(word, topn=3)
            
            print(f"  CBOW top 3:")
            for w, score in cbow_similar:
                print(f"    {w:<15} {score:.4f}")
            
            print(f"  Skip-gram top 3:")
            for w, score in sg_similar:
                print(f"    {w:<15} {score:.4f}")
    
    # Compare vector correlations
    print("\n" + "-" * 70)
    print("VECTOR AGREEMENT")
    print("-" * 70)
    
    # For words in both vocabularies, compare vectors
    common_words = set(model_cbow.wv.key_to_index.keys()) & set(model_sg.wv.key_to_index.keys())
    
    if len(common_words) > 0:
        correlations = []
        for word in list(common_words)[:10]:  # Sample 10 words
            vec_cbow = model_cbow.wv[word]
            vec_sg = model_sg.wv[word]
            corr = np.corrcoef(vec_cbow, vec_sg)[0, 1]
            correlations.append(corr)
            print(f"  {word:<15} vector correlation: {corr:.4f}")
        
        print(f"\nAverage correlation: {np.mean(correlations):.4f}")
        print("(Higher = models learned similar representations)")


def visualize_embeddings_2d(model, words=None):
    """
    Visualize embeddings in 2D using PCA
    
    Note: This is a simplified visualization. In reality, embeddings
    are high-dimensional and 2D projections lose information.
    """
    if words is None:
        # Use all words in vocabulary
        words = list(model.wv.key_to_index.keys())[:20]  # Limit to 20 for clarity
    
    # Filter words that exist in model
    valid_words = [w for w in words if w in model.wv]
    
    if len(valid_words) < 2:
        print("Not enough words for visualization")
        return
    
    # Extract vectors
    vectors = np.array([model.wv[word] for word in valid_words])
    
    # Reduce to 2D using PCA
    pca = PCA(n_components=2)
    vectors_2d = pca.fit_transform(vectors)
    
    print("\n" + "-" * 70)
    print("2D PROJECTION (PCA)")
    print("-" * 70)
    print(f"\nExplained variance: {pca.explained_variance_ratio_.sum():.2%}")
    print("\nWord coordinates in 2D space:")
    for word, (x, y) in zip(valid_words, vectors_2d):
        print(f"  {word:<15} ({x:6.3f}, {y:6.3f})")
    
    print("\n💡 In a plot, semantically similar words would cluster together")
    print("   Example: 'cat' and 'dog' should be near each other")


def main():
    print("=" * 70)
    print("WORD2VEC TRAINING: COMPLETE DEMONSTRATION")
    print("=" * 70)
    
    # Prepare corpus
    sentences = prepare_corpus(CORPUS)
    print(f"\nCorpus prepared:")
    print(f"  Total sentences: {len(sentences)}")
    print(f"  Sample sentence: {sentences[0]}")
    print(f"  Unique words: {len(set(word for sent in sentences for word in sent))}")
    
    # Train Word2Vec model (CBOW)
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
    
    print(f"\n✓ Model trained successfully!")
    print(f"  Architecture: CBOW")
    print(f"  Vector size: {model_cbow.vector_size}")
    print(f"  Vocabulary size: {len(model_cbow.wv)}")
    print(f"  Window size: {model_cbow.window}")
    
    # Explore embeddings
    explore_embeddings(model_cbow)
    
    # Compare CBOW vs Skip-gram
    compare_cbow_vs_skipgram(sentences)
    
    # Visualize (optional)
    visualize_embeddings_2d(model_cbow)
    
    # Key insights
    print("\n" + "=" * 70)
    print("KEY INSIGHTS & BEST PRACTICES")
    print("=" * 70)
    
    print("\n✓ Word2Vec Strengths:")
    print("  - Captures semantic similarity automatically")
    print("  - Dense representations (vs sparse BoW/TF-IDF)")
    print("  - Supports arithmetic operations on meanings")
    print("  - Efficient to train and use")
    
    print("\n✗ Limitations:")
    print("  - Requires large corpus for good results")
    print("  - One vector per word (no context-sensitivity)")
    print("  - Out-of-vocabulary words have no representation")
    print("  - Doesn't capture word order beyond local context")
    
    print("\n💡 Production Recommendations:")
    print("  1. Use pre-trained embeddings:")
    print("     - Word2Vec: Google News (300D, 3M words)")
    print("     - GloVe: Wikipedia+Gigaword (50-300D)")
    print("     - FastText: Handles unknown words via subwords")
    print("  2. Fine-tune on domain-specific data if needed")
    print("  3. For modern NLP: Use contextual embeddings (BERT, GPT)")
    print("  4. For RAG systems: Use Azure OpenAI embeddings")
    
    print("\n📊 Hyperparameter Guidelines:")
    print(f"  {'Parameter':<20} {'Typical Range':<20} {'Effect'}")
    print("  " + "-" * 65)
    print(f"  {'vector_size':<20} {'50-300':<20} {'Higher = more nuance, slower'}")
    print(f"  {'window':<20} {'5-10':<20} {'Larger = more context'}")
    print(f"  {'min_count':<20} {'1-5':<20} {'Higher = smaller vocab'}")
    print(f"  {'epochs':<20} {'5-20':<20} {'More = better learning'}")
    print(f"  {'sg':<20} {'0 (CBOW) or 1':<20} {'CBOW faster, SG better'}")


if __name__ == "__main__":
    main()
