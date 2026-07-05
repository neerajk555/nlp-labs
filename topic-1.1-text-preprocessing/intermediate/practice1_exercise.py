"""
Topic 1.1 - Intermediate Practice 1
Stemming vs Lemmatization Analysis

Learning Goals:
- Understand differences between stemming and lemmatization
- Compare Porter Stemmer and WordNet Lemmatizer
- Analyze trade-offs: speed vs accuracy
- Know when to use each in production

TODO: Implement comparison functions and analysis
"""

import time
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet

# Download required NLTK data (run once)
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# nltk.download('averaged_perceptron_tagger')


def stem_text(text):
    """
    Apply Porter Stemmer to text
    
    TODO:
    1. Initialize PorterStemmer
    2. Tokenize text
    3. Apply stemmer to each token
    4. Return list of stemmed tokens
    """
    pass


def lemmatize_text(text, use_pos=False):
    """
    Apply WordNet Lemmatizer to text
    
    TODO:
    1. Initialize WordNetLemmatizer
    2. Tokenize text
    3. If use_pos is True, get POS tags and convert to WordNet format
    4. Apply lemmatizer (with POS if available)
    5. Return list of lemmatized tokens
    
    Hint: Default POS is 'n' (noun) if not specified
    """
    pass


def get_wordnet_pos(treebank_tag):
    """
    Convert Penn Treebank POS tag to WordNet POS tag
    
    TODO: Map POS tags:
    - 'J' (adjective) → wordnet.ADJ
    - 'V' (verb) → wordnet.VERB
    - 'N' (noun) → wordnet.NOUN
    - 'R' (adverb) → wordnet.ADV
    - default → wordnet.NOUN
    """
    pass


def compare_methods(sentences):
    """
    Compare stemming vs lemmatization on multiple sentences
    
    TODO:
    1. For each sentence, apply:
       - Stemming
       - Lemmatization without POS
       - Lemmatization with POS
    2. Measure processing time
    3. Display results
    """
    pass


def analyze_edge_cases():
    """
    Analyze specific cases where stemming and lemmatization differ
    
    TODO: Test on words with different linguistic properties
    """
    test_words = [
        "running", "ran", "runs",           # Verb forms
        "better", "good", "best",           # Irregular adjective
        "studies", "studying", "studied",   # Regular verb
        "feet", "foot",                     # Irregular plural
        "caring", "cares", "carefully"      # Related words
    ]
    
    print("=" * 70)
    print("EDGE CASES ANALYSIS")
    print("=" * 70)
    
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    
    # TODO: Compare results for each word
    print(f"\n{'Word':<15} {'Stemmed':<15} {'Lemma (no POS)':<20} {'Lemma (with POS)':<20}")
    print("-" * 70)
    
    # Your implementation here


def main():
    print("=" * 70)
    print("STEMMING VS LEMMATIZATION COMPARISON")
    print("=" * 70)
    
    # Test sentences
    sentences = [
        "The runners were running faster than the cars were driving",
        "He studies better when his studying environment is comfortable",
        "The meeting was cancelled and will be rescheduled",
        "My feet are sore from walking",
        "She carefully cares for the caring nurses"
    ]
    
    print("\nTest sentences:")
    for i, sent in enumerate(sentences, 1):
        print(f"{i}. {sent}")
    
    # TODO: Compare methods
    compare_methods(sentences)
    
    # TODO: Analyze edge cases
    analyze_edge_cases()
    
    # TODO: Performance comparison
    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON")
    print("=" * 70)
    
    large_text = " ".join(sentences * 1000)  # Repeat for performance test
    
    # Measure stemming time
    start = time.time()
    stemmed = stem_text(large_text)
    stem_time = time.time() - start
    
    # Measure lemmatization time (without POS)
    start = time.time()
    lemmatized_no_pos = lemmatize_text(large_text, use_pos=False)
    lemma_time_no_pos = time.time() - start
    
    # Measure lemmatization time (with POS)
    start = time.time()
    lemmatized_with_pos = lemmatize_text(large_text, use_pos=True)
    lemma_time_with_pos = time.time() - start
    
    print(f"\nProcessing {len(large_text.split())} words:")
    print(f"  Stemming:                {stem_time:.4f}s")
    print(f"  Lemmatization (no POS):  {lemma_time_no_pos:.4f}s  ({lemma_time_no_pos/stem_time:.1f}x slower)")
    print(f"  Lemmatization (w/ POS):  {lemma_time_with_pos:.4f}s  ({lemma_time_with_pos/stem_time:.1f}x slower)")
    
    print("\n" + "=" * 70)
    print("WHEN TO USE EACH")
    print("=" * 70)
    print("\nUse STEMMING when:")
    print("  ✓ Speed is critical (real-time processing)")
    print("  ✓ Approximate matching is acceptable")
    print("  ✓ Working with search/IR systems")
    print("  ✓ Memory is limited")
    print("\nUse LEMMATIZATION when:")
    print("  ✓ Accuracy matters more than speed")
    print("  ✓ Need human-readable output")
    print("  ✓ Working with chatbots, text generation")
    print("  ✓ POS information is available or can be computed")


if __name__ == "__main__":
    main()
