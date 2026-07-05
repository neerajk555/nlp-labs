"""
Lab Exercise Generator
Generates skeleton files for all NLP lab exercises

Run this script to create all remaining exercise files with proper structure.
"""

import os
from pathlib import Path


# Exercise templates
EXERCISE_TEMPLATE = '''"""
{title}

Learning Goals:
{learning_goals}

TODO: Complete the implementation
"""

{imports}


{skeleton_code}


def main():
    """Main execution function"""
    print("=" * 70)
    print("{title_upper}")
    print("=" * 70)
    
    # TODO: Implement exercise logic
    pass


if __name__ == "__main__":
    main()
'''

SOLUTION_TEMPLATE = '''"""
{title} - Solution

This solution demonstrates {concepts}
"""

{imports}


{solution_code}


def main():
    """Main execution with complete implementation"""
    print("=" * 70)
    print("{title_upper}")
    print("=" * 70)
    
    {main_code}


if __name__ == "__main__":
    main()
'''


# Exercise definitions
EXERCISES = {
    "topic-1.2-semantic-similarity": {
        "beginner": [
            {
                "name": "practice1",
                "title": "Building an Inverted Index",
                "concepts": "Index construction, term lookup, posting lists",
                "imports": "from collections import defaultdict\nfrom typing import List, Dict, Set",
            },
            {
                "name": "practice2",
                "title": "BM25 Implementation",
                "concepts": "BM25 formula, document ranking, keyword search",
                "imports": "import math\nfrom collections import Counter",
            },
        ],
        "intermediate": [
            {
                "name": "demo",
                "title": "Semantic vs Lexical Similarity",
                "concepts": "Embeddings, word overlap metrics, semantic comparison",
                "imports": "from openai import AzureOpenAI\nimport numpy as np",
            },
            {
                "name": "practice1",
                "title": "Distance Metrics Comparison",
                "concepts": "Euclidean, Manhattan, Cosine distance",
                "imports": "import numpy as np\nfrom scipy.spatial import distance",
            },
            {
                "name": "practice2",
                "title": "Hybrid Search Implementation",
                "concepts": "Combining BM25 and vector search",
                "imports": "from rank_bm25 import BM25Okapi\nimport numpy as np",
            },
        ],
        "advanced": [
            {
                "name": "demo",
                "title": "Scalable Search with FAISS",
                "concepts": "Approximate nearest neighbors, indexing strategies",
                "imports": "import faiss\nimport numpy as np",
            },
            {
                "name": "practice1",
                "title": "Re-ranking Pipeline",
                "concepts": "Bi-encoder retrieval, cross-encoder re-ranking",
                "imports": "from transformers import AutoTokenizer, AutoModel",
            },
            {
                "name": "practice2",
                "title": "Azure AI Search Integration",
                "concepts": "Azure SDK, vector search, hybrid retrieval",
                "imports": "from azure.search.documents import SearchClient\nfrom openai import AzureOpenAI",
            },
        ],
    },
    "topic-1.3-ner-classification": {
        "beginner": [
            {
                "name": "demo",
                "title": "Rule-based NER",
                "concepts": "Regex patterns, entity extraction, rule systems",
                "imports": "import re\nfrom typing import List, Tuple",
            },
            {
                "name": "practice1",
                "title": "Sentiment Analysis with sklearn",
                "concepts": "Classification pipeline, TF-IDF features, logistic regression",
                "imports": "from sklearn.pipeline import Pipeline\nfrom sklearn.feature_extraction.text import TfidfVectorizer\nfrom sklearn.linear_model import LogisticRegression",
            },
            {
                "name": "practice2",
                "title": "Evaluation Metrics Calculation",
                "concepts": "Precision, recall, F1, confusion matrix",
                "imports": "from sklearn.metrics import precision_recall_fscore_support, confusion_matrix\nimport numpy as np",
            },
        ],
        "intermediate": [
            {
                "name": "demo",
                "title": "ML-based NER with spaCy",
                "concepts": "Pre-trained models, entity types, visualization",
                "imports": "import spacy\nfrom spacy import displacy",
            },
            {
                "name": "practice1",
                "title": "Multi-class Text Classification",
                "concepts": "Multiple classifiers, feature engineering, comparison",
                "imports": "from sklearn.naive_bayes import MultinomialNB\nfrom sklearn.ensemble import RandomForestClassifier\nfrom sklearn.svm import SVC",
            },
            {
                "name": "practice2",
                "title": "Error Analysis Workshop",
                "concepts": "Confusion matrix analysis, failure mode identification",
                "imports": "import pandas as pd\nimport seaborn as sns\nimport matplotlib.pyplot as plt",
            },
        ],
        "advanced": [
            {
                "name": "demo",
                "title": "LLM-based NER with Prompt Engineering",
                "concepts": "Few-shot learning, prompt design, Azure OpenAI",
                "imports": "from openai import AzureOpenAI\nimport json",
            },
            {
                "name": "practice1",
                "title": "Fine-tuning BERT for Classification",
                "concepts": "Transfer learning, Hugging Face, model training",
                "imports": "from transformers import BertTokenizer, BertForSequenceClassification, Trainer",
            },
            {
                "name": "practice2",
                "title": "Comprehensive Evaluation Pipeline",
                "concepts": "Cross-validation, statistical testing, multiple metrics",
                "imports": "from sklearn.model_selection import cross_val_score\nfrom scipy import stats",
            },
        ],
    },
    "topic-1.4-consolidation": {
        "beginner": [
            {
                "name": "demo",
                "title": "End-to-end NLP Pipeline",
                "concepts": "Preprocessing, feature extraction, training, evaluation",
                "imports": "from sklearn.pipeline import Pipeline\nfrom sklearn.feature_extraction.text import TfidfVectorizer",
            },
            {
                "name": "practice1",
                "title": "From BoW to Embeddings Comparison",
                "concepts": "Feature evolution, performance comparison",
                "imports": "from sklearn.feature_extraction.text import CountVectorizer\nfrom gensim.models import Word2Vec",
            },
            {
                "name": "practice2",
                "title": "Building a Simple RAG Pipeline",
                "concepts": "Retrieval + generation, basic RAG architecture",
                "imports": "from openai import AzureOpenAI\nimport numpy as np",
            },
        ],
        "intermediate": [
            {
                "name": "demo",
                "title": "RAG with Vector Database",
                "concepts": "Chunking strategies, embedding, retrieval",
                "imports": "import faiss\nfrom openai import AzureOpenAI",
            },
            {
                "name": "practice1",
                "title": "Prompt Engineering for NLP Tasks",
                "concepts": "Zero-shot, few-shot classification, prompt templates",
                "imports": "from openai import AzureOpenAI\nimport json",
            },
            {
                "name": "practice2",
                "title": "Traditional NLP vs GenAI Evaluation",
                "concepts": "Comparing metrics, LLM-as-judge",
                "imports": "from sklearn.metrics import f1_score\nfrom openai import AzureOpenAI",
            },
        ],
        "advanced": [
            {
                "name": "demo",
                "title": "Production RAG System",
                "concepts": "Azure AI Search, monitoring, error handling",
                "imports": "from azure.search.documents import SearchClient\nfrom openai import AzureOpenAI\nimport logging",
            },
            {
                "name": "practice1",
                "title": "Advanced Prompt Engineering",
                "concepts": "Chain-of-thought, ReAct, tool use",
                "imports": "from openai import AzureOpenAI\nimport json",
            },
            {
                "name": "practice2",
                "title": "GenAI Evaluation Framework",
                "concepts": "Relevance, faithfulness, answer quality metrics",
                "imports": "from openai import AzureOpenAI\nimport pandas as pd",
            },
        ],
    },
}


def create_exercise_file(topic, level, exercise_info, is_solution=False):
    """Generate exercise or solution file"""
    
    name = exercise_info["name"]
    title = f"Topic {topic.split('-')[1]} - {level.title()} {'Demo' if name == 'demo' else f'Practice {name[-1]}'}"
    
    if not is_solution:
        title += " Exercise"
    else:
        title += " Solution"
    
    learning_goals_text = f"- {exercise_info['concepts']}"
    
    template = SOLUTION_TEMPLATE if is_solution else EXERCISE_TEMPLATE
    
    content = template.format(
        title=title,
        title_upper=title.upper(),
        learning_goals=learning_goals_text,
        concepts=exercise_info['concepts'],
        imports=exercise_info['imports'],
        skeleton_code="# TODO: Implement functions here\n",
        solution_code="# Complete implementation\n",
        main_code="# Complete main logic\n    pass"
    )
    
    # Determine file path
    suffix = "_solution" if is_solution else "_exercise"
    filename = f"{name}{suffix}.py"
    filepath = Path(f"e:/ey-ai/nlp-labs/{topic}/{level}/{filename}")
    
    # Create directory if needed
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Write file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return filepath


def generate_all_exercises():
    """Generate all exercise files"""
    print("Generating NLP Lab Exercises...")
    print("=" * 70)
    
    generated = []
    
    for topic, levels in EXERCISES.items():
        print(f"\nTopic: {topic}")
        
        for level, exercises in levels.items():
            print(f"  Level: {level}")
            
            for exercise_info in exercises:
                # Generate exercise file
                ex_file = create_exercise_file(topic, level, exercise_info, is_solution=False)
                print(f"    ✓ Created: {ex_file.name}")
                generated.append(str(ex_file))
                
                # Generate solution file
                sol_file = create_exercise_file(topic, level, exercise_info, is_solution=True)
                print(f"    ✓ Created: {sol_file.name}")
                generated.append(str(sol_file))
    
    print("\n" + "=" * 70)
    print(f"Generated {len(generated)} files")
    print("\nNext steps:")
    print("1. Review generated files")
    print("2. Fill in TODO sections in exercise files")
    print("3. Complete implementation in solution files")
    print("4. Test all exercises")
    
    return generated


if __name__ == "__main__":
    files = generate_all_exercises()
    
    # Save file list
    with open("e:/ey-ai/nlp-labs/generated_files.txt", "w") as f:
        f.write("\n".join(files))
    
    print("\n✓ File list saved to generated_files.txt")
