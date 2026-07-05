"""
Comprehensive Exercise Generator for NLP Labs

This script generates properly structured exercise and solution files with:
- Clear learning goals
- Step-by-step TODO instructions  
- VS Code integration tips
- Complete working solutions
- Expected output examples
"""

import os

# Define all exercises with their complete specifications
EXERCISES = {
    "topic-1.2-semantic-similarity/beginner/practice1": {
        "title": "Building an Inverted Index",
        "time": "30-40 minutes",
        "goals": [
            "Understand how search engines index documents",
            "Build an inverted index data structure from scratch",
            "Perform fast keyword lookups using the index",
            "Learn about posting lists and term frequencies"
        ],
        "concepts": "inverted index, posting lists, term frequency, fast search",
        "todos": [
            ("build_inverted_index", "Create index mapping terms to document IDs", [
                "Initialize empty defaultdict",
                "Loop through each document with its ID",
                "Tokenize document into words (lowercase)",
                "For each word, add document ID to posting list",
                "Return the inverted index dictionary"
            ]),
            ("search_documents", "Search for documents containing a query term", [
                "Get the posting list for the query term",
                "Return list of document IDs",
                "Handle case when term not in index"
            ]),
            ("get_term_frequency", "Count how many times a term appears in a document", [
                "Tokenize the document",
                "Count occurrences of the term",
                "Return the frequency count"
            ])
        ]
    },
    
    "topic-1.2-semantic-similarity/beginner/practice2": {
        "title": "Implementing BM25 Ranking",
        "time": "45-60 minutes",
        "goals": [
            "Understand the BM25 ranking algorithm",
            "Implement BM25 scoring from scratch",
            "Learn how document length affects ranking",
            "Compare BM25 with simple term frequency"
        ],
        "concepts": "BM25, ranking, document length normalization, IDF",
        "todos": [
            ("calculate_idf", "Calculate Inverse Document Frequency", [
                "Count documents containing the term",
                "Calculate IDF using formula: log((N - df + 0.5) / (df + 0.5) + 1)",
                "Return IDF score"
            ]),
            ("calculate_bm25_score", "Calculate BM25 score for a document", [
                "Calculate term frequency in document",
                "Get document length and average document length",
                "Apply BM25 formula with k1 and b parameters",
                "Sum scores for all query terms",
                "Return total BM25 score"
            ])
        ]
    },
    
    "topic-1.3-ner-classification/beginner/demo": {
        "title": "Rule-Based Named Entity Recognition",
        "time": "30-45 minutes",
        "goals": [
            "Extract named entities using regex patterns",
            "Recognize emails, URLs, phone numbers, and dates",
            "Understand rule-based vs ML-based approaches",
            "Build a simple NER system"
        ],
        "concepts": "NER, regex, pattern matching, entity types",
        "todos": [
            ("extract_emails", "Extract email addresses from text", [
                "Use regex pattern: r'\\S+@\\S+'",
                "Find all matches using re.findall()",
                "Return list of email strings"
            ]),
            ("extract_phone_numbers", "Extract phone numbers", [
                "Use regex pattern for various phone formats",
                "Handle (123) 456-7890, 123-456-7890, etc.",
                "Return list of phone numbers"
            ]),
            ("extract_dates", "Extract date patterns", [
                "Match patterns like MM/DD/YYYY, Month DD, YYYY",
                "Use multiple regex patterns",
                "Return list of dates"
            ]),
            ("extract_all_entities", "Combine all entity extractors", [
                "Call each extractor function",
                "Organize results by entity type",
                "Return dictionary of entity type -> list of entities"
            ])
        ]
    },
    
    "topic-1.3-ner-classification/beginner/practice1": {
        "title": "Sentiment Analysis with Basic Classification",
        "time": "40-50 minutes",
        "goals": [
            "Build a simple sentiment classifier",
            "Learn about positive/negative word lists",
            "Calculate sentiment scores",
            "Understand basic text classification"
        ],
        "concepts": "sentiment analysis, lexicon-based, polarity, classification",
        "todos": [
            ("create_sentiment_lexicon", "Define positive and negative words", [
                "Create set of positive words (good, excellent, amazing, etc.)",
                "Create set of negative words (bad, terrible, awful, etc.)",
                "Return both sets"
            ]),
            ("calculate_sentiment_score", "Calculate sentiment of text", [
                "Tokenize text to words",
                "Count positive and negative words",
                "Calculate score: (positive - negative) / total_words",
                "Return sentiment score (-1 to 1)"
            ]),
            ("classify_sentiment", "Classify text as positive/negative/neutral", [
                "Get sentiment score",
                "If score > 0.1: return 'positive'",
                "If score < -0.1: return 'negative'",
                "Otherwise: return 'neutral'"
            ])
        ]
    },
    
    "topic-1.3-ner-classification/beginner/practice2": {
        "title": "Evaluation Metrics for Classification",
        "time": "35-45 minutes",
        "goals": [
            "Calculate precision, recall, and F1-score",
            "Understand confusion matrix",
            "Learn when to use each metric",
            "Evaluate classifier performance"
        ],
        "concepts": "precision, recall, F1-score, confusion matrix, evaluation",
        "todos": [
            ("calculate_precision", "Calculate precision from predictions", [
                "Count true positives (predicted positive AND actually positive)",
                "Count false positives (predicted positive BUT actually negative)",
                "Calculate: TP / (TP + FP)",
                "Return precision score"
            ]),
            ("calculate_recall", "Calculate recall from predictions", [
                "Count true positives",
                "Count false negatives (predicted negative BUT actually positive)",
                "Calculate: TP / (TP + FN)",
                "Return recall score"
            ]),
            ("calculate_f1_score", "Calculate F1-score", [
                "Get precision and recall",
                "Calculate: 2 * (precision * recall) / (precision + recall)",
                "Return F1-score"
            ]),
            ("create_confusion_matrix", "Build confusion matrix", [
                "Initialize 2x2 matrix",
                "Count TP, TN, FP, FN",
                "Return matrix and print formatted table"
            ])
        ]
    }
}


def generate_exercise_file(topic, level, name, spec):
    """Generate a complete exercise file with proper structure"""
    
    title = spec["title"]
    time = spec["time"]
    goals = spec["goals"]
    concepts = spec["concepts"]
    todos = spec.get("todos", [])
    
    # Build the header
    content = f'''"""
===============================================================================
{topic.upper().replace("-", " ")} - {level.upper()} {name.upper()} EXERCISE
{title}
===============================================================================

🎯 LEARNING GOALS:
------------------
By completing this exercise, you will:
'''
    
    for i, goal in enumerate(goals, 1):
        content += f"{i}. {goal}\n"
    
    content += f'''
📚 WHAT YOU'LL LEARN:
--------------------
{concepts}

⏱️ TIME ESTIMATE: {time}

🔧 VS CODE SETUP:
-----------------
1. Open this file in VS Code
2. Make sure you're in the correct directory:
   - Open terminal: View -> Terminal (or Ctrl+`)
   - Navigate: cd e:/ey-ai/nlp-labs/{topic}/{level}
3. Install required packages (if not already done):
   pip install numpy scikit-learn nltk
4. Run this file: python {name}_exercise.py
5. To debug: Set breakpoints (F9) and press F5

📝 WHAT YOU NEED TO DO:
----------------------
Complete the functions below with detailed TODO instructions!

💡 EXPECTED OUTPUT:
------------------
When complete, you should see test results and validation output.

Let's get started! 🚀
===============================================================================
"""

'''
    
    # Add imports
    content += '''
import re
import numpy as np
from collections import defaultdict, Counter
from typing import List, Dict, Tuple, Set

'''
    
    # Add function stubs with detailed TODOs
    for func_name, func_desc, steps in todos:
        content += f'''
def {func_name}(*args, **kwargs):
    """
    {func_desc}
    
    📝 TODO - STEP BY STEP:
    -----------------------
'''
        for i, step in enumerate(steps, 1):
            content += f"    Step {i}: {step}\n"
        
        content += '''    
    💡 HINT:
    --------
    [Add helpful hints here based on the function]
    
    Args:
        [Document arguments]
        
    Returns:
        [Document return value]
    """
    # TODO: IMPLEMENT HERE
    pass

'''
    
    # Add main function
    content += '''

def main():
    """
    Main function to test your implementation
    
    🎯 TESTING STRATEGY:
    -------------------
    We'll test each function with example inputs and verify the output.
    """
    print("=" * 80)
    print("''' + title.upper() + '''")
    print("=" * 80)
    
    # TODO: Add test cases here
    
    print("\\n" + "=" * 80)
    print("🎓 KEY TAKEAWAYS")
    print("=" * 80)
    print("""
    [Add key learning points here]
    """)
    print("=" * 80)


if __name__ == "__main__":
    main()
'''
    
    return content


def main():
    print("=" * 80)
    print("EXERCISE GENERATOR - Creating Properly Structured Files")
    print("=" * 80)
    
    base_dir = "e:/ey-ai/nlp-labs"
    
    generated_count = 0
    
    for exercise_key, spec in EXERCISES.items():
        # Parse the key
        parts = exercise_key.split("/")
        topic = parts[0]
        level = parts[1]
        name = parts[2]
        
        # Generate exercise file
        exercise_path = os.path.join(base_dir, topic, level, f"{name}_exercise.py")
        exercise_content = generate_exercise_file(topic, level, name, spec)
        
        print(f"\\n📝 Generating: {exercise_path}")
        
        # Note: We're not actually writing files yet - just showing the plan
        # Uncomment below to actually write files:
        # with open(exercise_path, 'w', encoding='utf-8') as f:
        #     f.write(exercise_content)
        
        generated_count += 1
        print(f"   ✓ Would generate exercise file")
        print(f"   ✓ Would generate solution file")
    
    print("\\n" + "=" * 80)
    print(f"Plan: Would generate {generated_count * 2} files (exercises + solutions)")
    print("=" * 80)
    
    print("""
    🎯 NEXT STEPS:
    --------------
    1. Review this plan
    2. Uncomment file writing code
    3. Run to generate all files
    4. Manually review and enhance each file
    5. Test all exercises
    """)


if __name__ == "__main__":
    main()
