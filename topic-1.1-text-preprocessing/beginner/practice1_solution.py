"""
Topic 1.1 - Beginner Practice 1 Solution
Tokenization Comparison

This solution demonstrates different tokenization strategies
and their trade-offs in vocabulary size and handling unknowns.
"""

# Sample texts
texts = [
    "Natural Language Processing is amazing!",
    "NLP techniques include tokenization.",
    "Machine learning models need preprocessed data."
]


def character_tokenize(text):
    """
    Tokenize text into individual characters
    
    Returns every character including spaces and punctuation.
    Useful for: spell checking, language modeling at character level
    """
    return list(text)


def word_tokenize(text):
    """
    Tokenize text into words (simple whitespace splitting)
    
    Note: This is basic. Production systems use smarter tokenizers
    that handle punctuation, contractions, etc.
    """
    return text.split()


def simple_subword_tokenize(text, max_word_length=5):
    """
    Simple subword tokenization: split long words into chunks
    
    This demonstrates the concept of subword tokenization.
    Real systems (BPE, WordPiece) learn optimal splits from data.
    
    Example: "tokenization" → ["token", "izati", "on"]
    """
    words = text.split()
    subwords = []
    
    for word in words:
        # If word is short enough, keep as is
        if len(word) <= max_word_length:
            subwords.append(word)
        else:
            # Split long word into chunks
            for i in range(0, len(word), max_word_length):
                chunk = word[i:i+max_word_length]
                subwords.append(chunk)
    
    return subwords


def calculate_vocabulary_size(tokens_list):
    """
    Calculate unique token count (vocabulary size)
    
    Using set automatically handles deduplication
    """
    return len(set(tokens_list))


def analyze_tokenization():
    """Compare different tokenization strategies"""
    print("=" * 70)
    print("TOKENIZATION COMPARISON")
    print("=" * 70)
    
    for i, text in enumerate(texts, 1):
        print(f"\nText {i}: \"{text}\"")
        print("-" * 70)
        
        # Apply all three tokenization methods
        char_tokens = character_tokenize(text)
        word_tokens = word_tokenize(text)
        subword_tokens = simple_subword_tokenize(text)
        
        # Print results
        print(f"Character tokens ({len(char_tokens)} tokens):")
        print(f"  {char_tokens[:20]}...")  # Show first 20 to avoid clutter
        
        print(f"\nWord tokens ({len(word_tokens)} tokens):")
        print(f"  {word_tokens}")
        
        print(f"\nSubword tokens ({len(subword_tokens)} tokens):")
        print(f"  {subword_tokens}")
    
    # Calculate overall vocabulary sizes
    print("\n" + "=" * 70)
    print("VOCABULARY SIZE COMPARISON")
    print("=" * 70)
    
    # Combine all texts
    all_text = " ".join(texts)
    
    # Calculate vocab size for each method
    char_vocab = calculate_vocabulary_size(character_tokenize(all_text))
    word_vocab = calculate_vocabulary_size(word_tokenize(all_text))
    subword_vocab = calculate_vocabulary_size(simple_subword_tokenize(all_text))
    
    print(f"Character-level vocabulary size: {char_vocab}")
    print(f"  → Small vocab, but very long sequences")
    
    print(f"\nWord-level vocabulary size: {word_vocab}")
    print(f"  → Large vocab grows with corpus size")
    
    print(f"\nSubword-level vocabulary size: {subword_vocab}")
    print(f"  → Balanced: smaller than word-level, more meaningful than char-level")
    
    # Demonstrate handling unknown words
    print("\n" + "=" * 70)
    print("HANDLING UNKNOWN WORDS")
    print("=" * 70)
    
    new_text = "Antidisestablishmentarianism is fascinating!"
    print(f"\nNew text: \"{new_text}\"")
    print(f"(Contains very long, potentially unknown word)")
    
    word_tokens_new = word_tokenize(new_text)
    subword_tokens_new = simple_subword_tokenize(new_text)
    
    print(f"\nWord tokenization:")
    print(f"  {word_tokens_new}")
    print(f"  → 'Antidisestablishmentarianism' is ONE token (unknown word problem)")
    
    print(f"\nSubword tokenization:")
    print(f"  {subword_tokens_new}")
    print(f"  → Long word split into manageable subwords")
    print(f"  → Model can understand meaning from parts!")


def main():
    analyze_tokenization()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("✓ Character tokenization: Small vocab (~100), very long sequences")
    print("  Use case: Languages without word boundaries, spell correction")
    print()
    print("✓ Word tokenization: Large vocab (10K-100K+), handles known words well")
    print("  Problem: Out-of-vocabulary (OOV) words, misspellings")
    print()
    print("✓ Subword tokenization: Medium vocab (5K-50K), handles unknowns")
    print("  Use case: LLMs (GPT, BERT use BPE/WordPiece)")
    print()
    print("✓ Why LLMs use subword tokenization:")
    print("  - Fixed vocabulary size regardless of corpus")
    print("  - Handles rare/new words by breaking into known subwords")
    print("  - Balances sequence length and vocab size")
    print("  - Works across multiple languages")


if __name__ == "__main__":
    main()
