"""
Topic 1.1 - Intermediate Practice 1 Solution
Stemming vs Lemmatization Analysis

This solution provides comprehensive comparison of stemming and lemmatization
with practical insights on when to use each.
"""

import time
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize

# Download required NLTK data (uncomment if needed)
try:
    wordnet.ensure_loaded()
except:
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    nltk.download('averaged_perceptron_tagger')
    nltk.download('punkt')


def stem_text(text):
    """
    Apply Porter Stemmer to text
    
    Porter Stemmer: Fast, rule-based algorithm
    - Removes suffixes using a series of rules
    - May produce non-words ("studies" → "studi")
    - Very fast, no dictionary lookup
    """
    stemmer = PorterStemmer()
    tokens = text.split()
    return [stemmer.stem(token) for token in tokens]


def lemmatize_text(text, use_pos=False):
    """
    Apply WordNet Lemmatizer to text
    
    Lemmatization: Dictionary-based approach
    - Returns actual word forms
    - Requires POS tags for best results
    - Slower but more accurate
    """
    lemmatizer = WordNetLemmatizer()
    tokens = text.split()
    
    if use_pos:
        # Get POS tags for better lemmatization
        pos_tags = pos_tag(tokens)
        return [
            lemmatizer.lemmatize(word, pos=get_wordnet_pos(tag))
            for word, tag in pos_tags
        ]
    else:
        # Default POS is noun
        return [lemmatizer.lemmatize(token) for token in tokens]


def get_wordnet_pos(treebank_tag):
    """
    Convert Penn Treebank POS tag to WordNet POS tag
    
    NLTK's pos_tag returns Penn Treebank tags (e.g., 'VB', 'NN', 'JJ')
    WordNet lemmatizer expects WordNet tags (wordnet.VERB, wordnet.NOUN, etc.)
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN  # Default to noun


def compare_methods(sentences):
    """Compare stemming vs lemmatization on multiple sentences"""
    print("\n" + "=" * 70)
    print("COMPARISON ON SENTENCES")
    print("=" * 70)
    
    for i, sentence in enumerate(sentences, 1):
        print(f"\nSentence {i}: \"{sentence}\"")
        print("-" * 70)
        
        # Apply all three methods
        stemmed = stem_text(sentence)
        lemma_no_pos = lemmatize_text(sentence, use_pos=False)
        lemma_with_pos = lemmatize_text(sentence, use_pos=True)
        
        print(f"Original:           {sentence.split()}")
        print(f"Stemmed:            {stemmed}")
        print(f"Lemma (no POS):     {lemma_no_pos}")
        print(f"Lemma (with POS):   {lemma_with_pos}")
        
        # Highlight differences
        original_words = sentence.split()
        differences = []
        for j, (orig, stem, lem_no, lem_yes) in enumerate(
            zip(original_words, stemmed, lemma_no_pos, lemma_with_pos)
        ):
            if stem != lem_yes:
                differences.append(f"  '{orig}': stem='{stem}' vs lemma='{lem_yes}'")
        
        if differences:
            print("\n⚠️  Key differences:")
            for diff in differences:
                print(diff)


def analyze_edge_cases():
    """Analyze specific cases where stemming and lemmatization differ"""
    test_cases = [
        ("Verb forms", ["running", "ran", "runs"], 'v'),
        ("Irregular adjective", ["better", "good", "best"], 'a'),
        ("Regular verb", ["studies", "studying", "studied"], 'v'),
        ("Irregular plural", ["feet", "foot"], 'n'),
        ("Related words", ["caring", "cares", "carefully"], 'v')
    ]
    
    print("\n" + "=" * 70)
    print("EDGE CASES ANALYSIS")
    print("=" * 70)
    
    stemmer = PorterStemmer()
    lemmatizer = WordNetLemmatizer()
    
    for case_name, words, pos_tag in test_cases:
        print(f"\n{case_name}:")
        print(f"{'Word':<15} {'Stemmed':<15} {'Lemma (noun)':<20} {'Lemma (correct POS)':<20}")
        print("-" * 70)
        
        # Convert pos_tag to WordNet POS
        if pos_tag == 'v':
            wn_pos = wordnet.VERB
        elif pos_tag == 'a':
            wn_pos = wordnet.ADJ
        elif pos_tag == 'n':
            wn_pos = wordnet.NOUN
        else:
            wn_pos = wordnet.NOUN
        
        for word in words:
            stemmed = stemmer.stem(word)
            lemma_noun = lemmatizer.lemmatize(word)
            lemma_pos = lemmatizer.lemmatize(word, pos=wn_pos)
            
            print(f"{word:<15} {stemmed:<15} {lemma_noun:<20} {lemma_pos:<20}")
        
        # Add explanation
        print(f"   💡 Insight: ", end="")
        if case_name == "Verb forms":
            print("Stemmer reduces all to common root; lemmatizer needs POS")
        elif case_name == "Irregular adjective":
            print("Lemmatizer correctly handles 'better'→'good'; stemmer doesn't")
        elif case_name == "Regular verb":
            print("Stemmer creates non-word; lemmatizer returns valid word")
        elif case_name == "Irregular plural":
            print("Lemmatizer recognizes 'feet'→'foot'; stemmer doesn't")
        else:
            print("Different words, even if related, get different forms")


def main():
    print("=" * 70)
    print("STEMMING VS LEMMATIZATION: COMPREHENSIVE ANALYSIS")
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
    
    # Compare methods
    compare_methods(sentences)
    
    # Analyze edge cases
    analyze_edge_cases()
    
    # Performance comparison
    print("\n" + "=" * 70)
    print("PERFORMANCE COMPARISON")
    print("=" * 70)
    
    large_text = " ".join(sentences * 1000)  # ~50,000 words
    print(f"\nProcessing {len(large_text.split())} words...")
    
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
    
    print(f"\n{'Method':<30} {'Time':<15} {'Relative Speed'}")
    print("-" * 70)
    print(f"{'Stemming':<30} {stem_time:.4f}s        Baseline (1.0x)")
    print(f"{'Lemmatization (no POS)':<30} {lemma_time_no_pos:.4f}s        {lemma_time_no_pos/stem_time:.1f}x slower")
    print(f"{'Lemmatization (with POS)':<30} {lemma_time_with_pos:.4f}s        {lemma_time_with_pos/stem_time:.1f}x slower")
    
    print("\n💡 Performance insights:")
    print(f"   - Stemming is fastest (rule-based, no lookups)")
    print(f"   - Lemmatization is {lemma_time_no_pos/stem_time:.0f}x slower (dictionary lookups)")
    print(f"   - Adding POS tagging makes it {lemma_time_with_pos/stem_time:.0f}x slower (extra NLP step)")
    
    # Decision guide
    print("\n" + "=" * 70)
    print("DECISION GUIDE: WHEN TO USE EACH")
    print("=" * 70)
    
    print("\n🚀 Use STEMMING when:")
    print("  ✓ Speed is critical (real-time systems, large-scale processing)")
    print("  ✓ Approximate matching is acceptable (search engines)")
    print("  ✓ Working with Information Retrieval (keyword matching)")
    print("  ✓ Memory/resources are limited")
    print("  ✓ Language doesn't have good lemmatization dictionaries")
    print("\n  Examples:")
    print("    - Search engines (Google, Elasticsearch)")
    print("    - Real-time social media analysis")
    print("    - Document clustering at scale")
    
    print("\n🎯 Use LEMMATIZATION when:")
    print("  ✓ Accuracy matters more than speed")
    print("  ✓ Output will be seen by humans (need readable words)")
    print("  ✓ Working with text generation or chatbots")
    print("  ✓ Semantic analysis is important")
    print("  ✓ POS information is available or worth computing")
    print("\n  Examples:")
    print("    - Sentiment analysis")
    print("    - Machine translation preprocessing")
    print("    - Question answering systems")
    print("    - Content summarization")
    
    print("\n⚖️  Trade-offs summary:")
    print(f"  {'Criterion':<25} {'Stemming':<20} {'Lemmatization'}")
    print("  " + "-" * 65)
    print(f"  {'Speed':<25} {'Fast':<20} {'Slower'}")
    print(f"  {'Accuracy':<25} {'Approximate':<20} {'Accurate'}")
    print(f"  {'Output format':<25} {'Non-words possible':<20} {'Real words'}")
    print(f"  {'Linguistic knowledge':<25} {'None (rules only)':<20} {'Dictionary + POS'}")
    print(f"  {'Typical use case':<25} {'Search/IR':<20} {'NLP/NLU'}")
    
    print("\n" + "=" * 70)
    print("PRODUCTION BEST PRACTICES")
    print("=" * 70)
    print("\n1. For RAG systems: Use lemmatization (better semantic matching)")
    print("2. For search engines: Use stemming (faster, good enough)")
    print("3. For chatbots: Use lemmatization with POS (natural language)")
    print("4. For classification: Test both, may not make big difference")
    print("5. Modern trend: Use subword tokenization instead (for LLMs)")


if __name__ == "__main__":
    main()
