"""
Topic 1.1 - Beginner Demo Solution
Basic Text Preprocessing Pipeline

This solution demonstrates a complete text preprocessing pipeline
with detailed explanations of each step.
"""

import re
import string

# Sample text for demonstration
sample_text = """
    The Quick BROWN fox jumps over the lazy dog! 
    Visit https://example.com for more info.
    Email me at contact@example.com. #NLP #AI
"""

# Common English stopwords
STOPWORDS = {'the', 'is', 'at', 'which', 'on', 'a', 'an', 'for', 'over', 'me'}


def remove_urls(text):
    """
    Remove URLs from text
    
    Uses regex pattern to match http:// or https:// followed by non-whitespace
    """
    pattern = r'https?://\S+'
    return re.sub(pattern, '', text)


def remove_emails(text):
    """
    Remove email addresses from text
    
    Matches pattern: characters@characters
    """
    pattern = r'\S+@\S+'
    return re.sub(pattern, '', text)


def remove_punctuation(text):
    """
    Remove punctuation from text
    
    Uses str.translate() with a translation table that maps
    all punctuation characters to None (removal)
    """
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


def remove_stopwords(words, stopwords=STOPWORDS):
    """
    Remove stopwords from list of words
    
    Uses list comprehension to filter out words in stopwords set.
    Set lookup is O(1) making this efficient.
    """
    return [word for word in words if word.lower() not in stopwords]


def preprocess_text(text, remove_stops=True):
    """
    Complete preprocessing pipeline
    
    Steps:
    1. Remove URLs - clean web-scraped content
    2. Remove emails - privacy and noise reduction
    3. Lowercase - normalize case ('The' and 'the' become same token)
    4. Remove punctuation - reduce vocabulary size
    5. Tokenize - split into words
    6. Remove stopwords - focus on content words
    
    Args:
        text: Input text string
        remove_stops: Whether to remove stopwords
        
    Returns:
        List of processed tokens
    """
    # Step 1: Remove URLs
    text = remove_urls(text)
    
    # Step 2: Remove emails
    text = remove_emails(text)
    
    # Step 3: Convert to lowercase
    text = text.lower()
    
    # Step 4: Remove punctuation
    text = remove_punctuation(text)
    
    # Step 5: Tokenize (simple whitespace splitting)
    # Note: More sophisticated tokenizers (spaCy, NLTK) handle edge cases better
    words = text.split()
    
    # Step 6: Remove stopwords
    if remove_stops:
        words = remove_stopwords(words)
    
    return words


def main():
    """Run the preprocessing demo"""
    print("=" * 60)
    print("TEXT PREPROCESSING DEMO")
    print("=" * 60)
    print("\nOriginal Text:")
    print(sample_text)
    print("\n" + "="*60 + "\n")
    
    # Process text with stopwords removed
    processed_with_stops_removed = preprocess_text(sample_text, remove_stops=True)
    
    # Process text keeping stopwords
    processed_with_stops_kept = preprocess_text(sample_text, remove_stops=False)
    
    print("Processed (stopwords removed):")
    print(processed_with_stops_removed)
    print(f"\nWord count: {len(processed_with_stops_removed)}")
    
    print("\n" + "="*60 + "\n")
    
    print("Processed (stopwords kept):")
    print(processed_with_stops_kept)
    print(f"\nWord count: {len(processed_with_stops_kept)}")
    
    # Calculate reduction
    if len(processed_with_stops_kept) > 0:
        reduction = ((len(processed_with_stops_kept) - len(processed_with_stops_removed)) 
                     / len(processed_with_stops_kept) * 100)
        print(f"\nStopword removal reduced vocabulary by {reduction:.1f}%")
    
    # Show what was removed
    removed_words = set(processed_with_stops_kept) - set(processed_with_stops_removed)
    print(f"\nStopwords removed: {removed_words}")
    
    print("\n" + "="*60)
    print("KEY INSIGHTS:")
    print("="*60)
    print("1. URLs and emails are noise for most NLP tasks")
    print("2. Lowercasing reduces vocabulary size (Quick, quick, QUICK → quick)")
    print("3. Stopword removal focuses on content words")
    print("4. Trade-off: removing stopwords loses context ('not good' → 'good')")


if __name__ == "__main__":
    main()
