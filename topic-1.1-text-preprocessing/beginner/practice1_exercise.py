"""
Topic 1.1 - Beginner Practice 1
Tokenization Comparison

Learning Goals:
- Compare character, word, and simple subword tokenization
- Understand vocabulary size implications
- Handle unknown words

TODO: Complete the tokenization functions
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
    
    TODO: Return a list of all characters in the text (including spaces)
    Hint: list(text) or [char for char in text]
    """
    pass


def word_tokenize(text):
    """
    Tokenize text into words (simple whitespace splitting)
    
    TODO: Split text by whitespace and return list of words
    Hint: text.split()
    """
    pass


def simple_subword_tokenize(text, max_word_length=5):
    """
    Simple subword tokenization: split long words into chunks
    
    This is a simplified version. Real subword tokenization (BPE, WordPiece)
    is more sophisticated.
    
    Example: "tokenization" → ["token", "izati", "on"]
    
    TODO: 
    1. Split text into words
    2. For each word:
       - If length <= max_word_length, keep as is
       - If length > max_word_length, split into chunks of max_word_length
    3. Return list of subword tokens
    """
    pass


def calculate_vocabulary_size(tokens_list):
    """
    Calculate unique token count (vocabulary size)
    
    TODO: Return the number of unique tokens
    Hint: len(set(tokens_list))
    """
    pass


def analyze_tokenization():
    """
    Compare different tokenization strategies
    
    TODO: For each text in texts:
    1. Apply all three tokenization methods
    2. Calculate vocabulary size for each method
    3. Print comparison results
    """
    print("=" * 70)
    print("TOKENIZATION COMPARISON")
    print("=" * 70)
    
    for i, text in enumerate(texts, 1):
        print(f"\nText {i}: \"{text}\"")
        print("-" * 70)
        
        # TODO: Apply character tokenization
        char_tokens = None
        
        # TODO: Apply word tokenization
        word_tokens = None
        
        # TODO: Apply subword tokenization
        subword_tokens = None
        
        # TODO: Print results for each method
        print(f"Character tokens ({len(char_tokens)} tokens):")
        print(f"  {char_tokens[:20]}...")  # Show first 20
        
        print(f"\nWord tokens ({len(word_tokens)} tokens):")
        print(f"  {word_tokens}")
        
        print(f"\nSubword tokens ({len(subword_tokens)} tokens):")
        print(f"  {subword_tokens}")
    
    # TODO: Calculate overall vocabulary sizes
    print("\n" + "=" * 70)
    print("VOCABULARY SIZE COMPARISON")
    print("=" * 70)
    
    # Combine all texts
    all_text = " ".join(texts)
    
    # TODO: Calculate vocab size for each method
    char_vocab = None
    word_vocab = None
    subword_vocab = None
    
    print(f"Character-level vocabulary size: {char_vocab}")
    print(f"Word-level vocabulary size: {word_vocab}")
    print(f"Subword-level vocabulary size: {subword_vocab}")
    
    # TODO: Demonstrate handling unknown words
    print("\n" + "=" * 70)
    print("HANDLING UNKNOWN WORDS")
    print("=" * 70)
    
    new_text = "Antidisestablishmentarianism is fascinating!"
    print(f"New text: \"{new_text}\"")
    
    # TODO: Show how each tokenization handles the long unknown word


def main():
    analyze_tokenization()
    
    print("\n" + "=" * 70)
    print("KEY TAKEAWAYS:")
    print("=" * 70)
    print("1. Character tokenization: Small vocab, long sequences")
    print("2. Word tokenization: Large vocab, struggles with unknown words")
    print("3. Subword tokenization: Balanced approach, handles unknowns")
    print("4. LLMs use subword tokenization (BPE, WordPiece) for this reason!")


if __name__ == "__main__":
    main()
