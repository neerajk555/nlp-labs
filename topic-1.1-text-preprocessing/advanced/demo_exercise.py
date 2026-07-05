"""
Topic 1.1 - Advanced Demo Exercise
Production-Ready Text Preprocessing Pipeline

Learning Goals:
- Build robust preprocessing pipeline with error handling
- Handle multiple languages and special cases
- Implement configurable pipeline with logging
- Optimize for performance

TODO: Complete the ProductionPreprocessor class
"""

import re
import logging
import unicodedata
from typing import List, Dict, Callable, Optional
from dataclasses import dataclass
import time


@dataclass
class PreprocessingConfig:
    """Configuration for preprocessing pipeline"""
    lowercase: bool = True
    remove_urls: bool = True
    remove_emails: bool = True
    remove_html: bool = True
    remove_punctuation: bool = False
    remove_numbers: bool = False
    remove_stopwords: bool = True
    min_word_length: int = 1
    max_word_length: int = 50
    normalize_unicode: bool = True
    custom_replacements: Dict[str, str] = None


class ProductionPreprocessor:
    """
    Production-ready text preprocessing pipeline
    
    Features:
    - Configurable steps
    - Error handling
    - Logging
    - Performance monitoring
    - Batch processing
    """
    
    def __init__(self, config: PreprocessingConfig):
        self.config = config
        self.logger = logging.getLogger(__name__)
        self.stats = {'processed': 0, 'errors': 0, 'total_time': 0}
        
        # TODO: Initialize stopwords (load from NLTK or custom list)
        self.stopwords = set([
            'the', 'is', 'at', 'which', 'on', 'a', 'an', 'and', 'or', 'but',
            'in', 'with', 'to', 'for', 'of', 'as', 'by'
        ])
    
    def preprocess(self, text: str) -> str:
        """
        Main preprocessing function
        
        TODO: Implement full pipeline with error handling
        1. Validate input
        2. Apply each preprocessing step based on config
        3. Handle errors gracefully
        4. Log processing info
        5. Update stats
        """
        pass
    
    def _normalize_unicode(self, text: str) -> str:
        """
        Normalize unicode characters
        
        TODO: Convert to NFKD form and remove combining characters
        Hint: Use unicodedata.normalize() and unicodedata.combining()
        """
        pass
    
    def _remove_html(self, text: str) -> str:
        """
        Remove HTML tags
        
        TODO: Remove HTML tags using regex
        Pattern: <[^>]+>
        """
        pass
    
    def _remove_urls(self, text: str) -> str:
        """Remove URLs"""
        # TODO: Implement comprehensive URL removal
        # Handle: http://, https://, www., ftp://, etc.
        pass
    
    def _remove_emails(self, text: str) -> str:
        """Remove email addresses"""
        # TODO: Robust email regex
        pass
    
    def _remove_punctuation(self, text: str) -> str:
        """Remove punctuation while preserving sentence structure"""
        # TODO: Remove punctuation but keep spaces
        pass
    
    def _remove_numbers(self, text: str) -> str:
        """Remove numbers"""
        # TODO: Remove standalone numbers, optionally keep numbers in words (e.g., "covid19")
        pass
    
    def _apply_custom_replacements(self, text: str) -> str:
        """Apply custom text replacements"""
        # TODO: Apply replacements from config
        pass
    
    def _remove_stopwords(self, text: str) -> str:
        """Remove stopwords"""
        # TODO: Split, filter, rejoin
        pass
    
    def _filter_by_length(self, text: str) -> str:
        """Filter words by length"""
        # TODO: Remove words shorter than min or longer than max
        pass
    
    def preprocess_batch(self, texts: List[str], 
                        n_jobs: int = 1) -> List[str]:
        """
        Preprocess multiple texts
        
        TODO: Implement batch processing with optional parallelization
        Consider using multiprocessing for large batches
        """
        pass
    
    def get_stats(self) -> Dict:
        """Return preprocessing statistics"""
        return self.stats.copy()
    
    def reset_stats(self):
        """Reset statistics"""
        self.stats = {'processed': 0, 'errors': 0, 'total_time': 0}


def benchmark_preprocessing(texts: List[str], config: PreprocessingConfig):
    """
    Benchmark preprocessing performance
    
    TODO: Measure throughput and latency
    """
    pass


def main():
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    print("=" * 70)
    print("PRODUCTION TEXT PREPROCESSING PIPELINE")
    print("=" * 70)
    
    # Sample texts with various edge cases
    texts = [
        "Check out https://example.com for more info! 🚀",
        "<p>HTML tags should be removed</p>",
        "Contact: user@example.com or call 555-1234",
        "UPPERCASE and MixedCase text",
        "Special chars: @#$%^&*() should be handled",
        "   Extra    spaces   should   be   normalized   ",
        "café résumé naïve — unicode handling",
        "Numbers: 123, 456.78, 1st, 2nd",
        "",  # Empty string
        None,  # None value
    ]
    
    # TODO: Create different configurations
    config_minimal = PreprocessingConfig(
        lowercase=True,
        remove_urls=True,
        remove_emails=True
    )
    
    config_aggressive = PreprocessingConfig(
        lowercase=True,
        remove_urls=True,
        remove_emails=True,
        remove_html=True,
        remove_punctuation=True,
        remove_numbers=True,
        remove_stopwords=True,
        min_word_length=2
    )
    
    # TODO: Process with different configs
    print("\n" + "=" * 70)
    print("MINIMAL PREPROCESSING")
    print("=" * 70)
    
    preprocessor_min = ProductionPreprocessor(config_minimal)
    # Process and display results
    
    print("\n" + "=" * 70)
    print("AGGRESSIVE PREPROCESSING")
    print("=" * 70)
    
    preprocessor_agg = ProductionPreprocessor(config_aggressive)
    # Process and display results
    
    # TODO: Show statistics
    print("\n" + "=" * 70)
    print("PROCESSING STATISTICS")
    print("=" * 70)
    
    # TODO: Benchmark performance
    print("\n" + "=" * 70)
    print("PERFORMANCE BENCHMARK")
    print("=" * 70)
    
    large_corpus = texts * 1000
    benchmark_preprocessing(large_corpus, config_aggressive)
    
    print("\n" + "=" * 70)
    print("BEST PRACTICES")
    print("=" * 70)
    print("\n1. Always validate input (handle None, empty strings)")
    print("2. Use logging for debugging production issues")
    print("3. Make pipeline configurable (different tasks need different preprocessing)")
    print("4. Handle unicode correctly for international text")
    print("5. Monitor performance and memory usage")
    print("6. Consider caching for repeated preprocessing")
    print("7. Use batch processing for large datasets")


if __name__ == "__main__":
    main()
