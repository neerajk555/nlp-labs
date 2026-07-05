"""
Topic 1.1 - Beginner Demo Exercise
Basic Text Preprocessing Pipeline

Learning Goals:
- Understand the steps in a basic text preprocessing pipeline
- Apply lowercasing, punctuation removal, and stopword removal
- See the impact of each preprocessing step

TODO: Complete the functions marked with TODO comments
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
    """Remove URLs from text"""
    # TODO: Use regex to remove URLs starting with http:// or https://
    # Pattern: r'https?://\S+'
    # Hint: Use re.sub() to replace URLs with empty string
    pass


def remove_emails(text):
    """Remove email addresses from text"""
    # TODO: Use regex to remove email patterns
    # Pattern: r'\S+@\S+'
    pass


def remove_punctuation(text):
    """Remove punctuation from text"""
    # TODO: Use str.translate() with string.punctuation
    # Create translation table: str.maketrans('', '', string.punctuation)
    pass


def remove_stopwords(words, stopwords=STOPWORDS):
    """Remove stopwords from list of words"""
    # TODO: Filter out words that are in the stopwords set
    # Return a list of words not in stopwords
    pass


def preprocess_text(text, remove_stops=True):
    """
    Complete preprocessing pipeline
    
    Steps:
    1. Remove URLs
    2. Remove emails
    3. Lowercase
    4. Remove punctuation
    5. Tokenize (split into words)
    6. Remove stopwords (if enabled)
    """
    # TODO: Step 1 - Remove URLs
    text = remove_urls(text)
    
    # TODO: Step 2 - Remove emails
    
    # TODO: Step 3 - Convert to lowercase
    
    # TODO: Step 4 - Remove punctuation
    
    # TODO: Step 5 - Tokenize (split by whitespace)
    words = None  # Replace with actual tokenization
    
    # TODO: Step 6 - Remove stopwords
    if remove_stops:
        words = remove_stopwords(words)
    
    return words


def main():
    """Run the preprocessing demo"""
    print("Original Text:")
    print(sample_text)
    print("\n" + "="*60 + "\n")
    
    # TODO: Process text with stopwords removed
    processed_with_stops_removed = preprocess_text(sample_text, remove_stops=True)
    
    # TODO: Process text keeping stopwords
    processed_with_stops_kept = preprocess_text(sample_text, remove_stops=False)
    
    print("Processed (stopwords removed):")
    print(processed_with_stops_removed)
    print(f"\nWord count: {len(processed_with_stops_removed)}")
    
    print("\n" + "="*60 + "\n")
    
    print("Processed (stopwords kept):")
    print(processed_with_stops_kept)
    print(f"\nWord count: {len(processed_with_stops_kept)}")
    
    # Calculate reduction
    # TODO: Calculate percentage of words removed by stopword filtering
    reduction = 0  # Calculate actual reduction
    print(f"\nStopword removal reduced vocabulary by {reduction:.1f}%")


if __name__ == "__main__":
    main()
