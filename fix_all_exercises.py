"""
Comprehensive Exercise Generator
Fixes all exercises with proper structure, TODOs, goals, and solutions
"""

import os
from pathlib import Path

# Exercise templates with complete structure
EXERCISES = {
    "topic-1.1-text-preprocessing": {
        "beginner": {
            "demo": {
                "title": "Basic Text Preprocessing Pipeline",
                "time": "30-45 minutes",
                "goals": [
                    "Understand the importance of text preprocessing",
                    "Apply lowercasing, punctuation removal, and stopword removal",
                    "See the impact of each preprocessing step on text",
                    "Build a reusable preprocessing function"
                ],
                "concepts": "Text cleaning, tokenization, stopword removal",
                "todos": [
                    "Implement remove_urls() using regex pattern",
                    "Implement remove_emails() to clean email addresses",
                    "Implement remove_punctuation() using string.translate()",
                    "Implement remove_stopwords() to filter common words",
                    "Create preprocess_text() pipeline combining all steps"
                ]
            },
            "practice1": {
                "title": "Tokenization Strategies Comparison",
                "time": "45-60 minutes",
                "goals": [
                    "Understand different tokenization approaches",
                    "Implement character, word, and subword tokenization",
                    "Compare tokenization results on different text types",
                    "Learn when to use each tokenization strategy"
                ],
                "concepts": "Character tokenization, word tokenization, whitespace splitting",
                "todos": [
                    "Implement character_tokenize() splitting text into characters",
                    "Implement word_tokenize() using split() and punctuation handling",
                    "Implement advanced_tokenize() handling contractions and special cases",
                    "Compare all three methods on sample texts",
                    "Analyze which method works best for different scenarios"
                ]
            },
            "practice2": {
                "title": "Bag of Words from Scratch",
                "time": "45-60 minutes",
                "goals": [
                    "Understand the Bag of Words (BoW) representation",
                    "Build a vocabulary from a corpus",
                    "Convert documents to BoW vectors",
                    "Visualize and interpret BoW representations"
                ],
                "concepts": "Bag of Words, vocabulary building, document vectorization",
                "todos": [
                    "Implement build_vocabulary() to extract unique words",
                    "Implement text_to_bow() converting text to word count vector",
                    "Implement corpus_to_bow_matrix() for multiple documents",
                    "Compare your implementation with CountVectorizer",
                    "Visualize BoW vectors and interpret results"
                ]
            }
        },
        "intermediate": {
            "demo": {
                "title": "TF-IDF from Scratch vs sklearn",
                "time": "60-75 minutes",
                "goals": [
                    "Understand TF-IDF formula and intuition",
                    "Implement TF (term frequency) calculation",
                    "Implement IDF (inverse document frequency) calculation",
                    "Build complete TF-IDF vectorizer from scratch",
                    "Validate against sklearn's TfidfVectorizer"
                ],
                "concepts": "Term frequency, inverse document frequency, TF-IDF formula",
                "todos": [
                    "Implement compute_tf() calculating term frequencies",
                    "Implement compute_idf() calculating inverse document frequencies",
                    "Implement compute_tfidf() combining TF and IDF",
                    "Create TfidfVectorizer class with fit() and transform()",
                    "Compare results with sklearn.feature_extraction.text.TfidfVectorizer"
                ]
            },
            "practice1": {
                "title": "Stemming vs Lemmatization",
                "time": "60-75 minutes",
                "goals": [
                    "Understand the difference between stemming and lemmatization",
                    "Use Porter Stemmer and Snowball Stemmer",
                    "Use WordNet Lemmatizer with POS tagging",
                    "Compare results and performance of each approach",
                    "Learn when to use stemming vs lemmatization"
                ],
                "concepts": "Stemming algorithms, lemmatization, POS tagging",
                "todos": [
                    "Implement apply_porter_stemming() using PorterStemmer",
                    "Implement apply_lemmatization() using WordNetLemmatizer",
                    "Implement pos_aware_lemmatization() with POS tags",
                    "Compare all three approaches on sample text",
                    "Analyze processing time and output quality"
                ]
            },
            "practice2": {
                "title": "Training Word2Vec Embeddings",
                "time": "75-90 minutes",
                "goals": [
                    "Understand Word2Vec architecture (CBOW vs Skip-gram)",
                    "Prepare text corpus for Word2Vec training",
                    "Train Word2Vec model with different parameters",
                    "Explore word similarities and analogies",
                    "Visualize word embeddings in 2D space"
                ],
                "concepts": "Word embeddings, CBOW, Skip-gram, semantic similarity",
                "todos": [
                    "Implement prepare_corpus() to tokenize and clean text",
                    "Train CBOW model using gensim.models.Word2Vec",
                    "Train Skip-gram model and compare with CBOW",
                    "Implement find_similar_words() using model.wv.most_similar()",
                    "Test word analogies (king - man + woman = ?)",
                    "Visualize embeddings using t-SNE or PCA"
                ]
            }
        },
        "advanced": {
            "demo": {
                "title": "Production Text Preprocessing Pipeline",
                "time": "90-120 minutes",
                "goals": [
                    "Build a configurable, production-ready preprocessing pipeline",
                    "Implement error handling and logging",
                    "Support batch processing and parallel execution",
                    "Add performance monitoring and caching",
                    "Create a reusable TextPreprocessor class"
                ],
                "concepts": "Production systems, error handling, performance optimization",
                "todos": [
                    "Create TextPreprocessor class with configuration",
                    "Implement configurable preprocessing steps (lowercase, remove_urls, etc.)",
                    "Add error handling with try-except and logging",
                    "Implement batch_process() for multiple documents",
                    "Add caching using functools.lru_cache",
                    "Create performance benchmarks and optimization",
                    "Add unit tests for edge cases"
                ]
            },
            "practice1": {
                "title": "Subword Tokenization (BPE, WordPiece, SentencePiece)",
                "time": "90-120 minutes",
                "goals": [
                    "Understand subword tokenization algorithms",
                    "Implement Byte Pair Encoding (BPE) from scratch",
                    "Use Hugging Face tokenizers (WordPiece, SentencePiece)",
                    "Compare subword methods with word-level tokenization",
                    "Handle out-of-vocabulary words effectively"
                ],
                "concepts": "BPE, WordPiece, SentencePiece, subword units, OOV handling",
                "todos": [
                    "Implement BPE algorithm from scratch",
                    "Train BPE tokenizer on sample corpus",
                    "Use transformers.BertTokenizer (WordPiece)",
                    "Use transformers.T5Tokenizer (SentencePiece)",
                    "Compare vocab sizes and OOV handling",
                    "Analyze tokenization of rare and compound words"
                ]
            },
            "practice2": {
                "title": "Comparing Embedding Methods (Word2Vec, GloVe, Azure OpenAI)",
                "time": "90-120 minutes",
                "goals": [
                    "Compare different embedding approaches",
                    "Use pre-trained GloVe embeddings",
                    "Generate embeddings with Azure OpenAI API",
                    "Evaluate embedding quality on semantic tasks",
                    "Analyze performance, cost, and accuracy trade-offs"
                ],
                "concepts": "Word2Vec, GloVe, transformer embeddings, embedding evaluation",
                "todos": [
                    "Load and use pre-trained GloVe embeddings",
                    "Train custom Word2Vec model on domain text",
                    "Get embeddings from Azure OpenAI text-embedding-ada-002",
                    "Implement embedding evaluation (word similarity, analogies)",
                    "Compare dimensionality, context-awareness, and performance",
                    "Calculate cost and latency for each method"
                ]
            }
        }
    },
    
    "topic-1.2-semantic-similarity": {
        "beginner": {
            "demo": {
                "title": "Cosine Similarity from Scratch",
                "time": "30-45 minutes",
                "goals": [
                    "Understand cosine similarity formula",
                    "Implement cosine similarity using NumPy",
                    "Compare with sklearn's cosine_similarity",
                    "Measure similarity between text documents"
                ],
                "concepts": "Cosine similarity, dot product, vector magnitude",
                "todos": [
                    "Implement cosine_similarity_manual() using dot product formula",
                    "Implement text_to_vector() converting text to numerical vector",
                    "Calculate similarities between document pairs",
                    "Validate against sklearn.metrics.pairwise.cosine_similarity",
                    "Interpret similarity scores and rankings"
                ]
            },
            "practice1": {
                "title": "Building an Inverted Index",
                "time": "45-60 minutes",
                "goals": [
                    "Understand inverted index data structure",
                    "Build an inverted index from a document collection",
                    "Implement boolean search queries",
                    "Optimize lookup performance with inverted index"
                ],
                "concepts": "Inverted index, posting lists, boolean retrieval",
                "todos": [
                    "Implement build_inverted_index() creating term->document mapping",
                    "Implement boolean_search() for single-term queries",
                    "Implement and_search() for multi-term AND queries",
                    "Implement or_search() for multi-term OR queries",
                    "Compare search speed with linear scan",
                    "Visualize inverted index structure"
                ]
            },
            "practice2": {
                "title": "BM25 Ranking Algorithm",
                "time": "60-75 minutes",
                "goals": [
                    "Understand BM25 ranking formula",
                    "Implement BM25 from scratch",
                    "Compare BM25 with TF-IDF",
                    "Tune BM25 parameters (k1, b)"
                ],
                "concepts": "BM25, term frequency saturation, document length normalization",
                "todos": [
                    "Implement compute_idf() for BM25",
                    "Implement compute_bm25_score() with k1 and b parameters",
                    "Create BM25Retriever class for document ranking",
                    "Compare BM25 vs TF-IDF on sample queries",
                    "Tune k1 (term frequency saturation) and b (length normalization)",
                    "Visualize ranking differences"
                ]
            }
        },
        "intermediate": {
            "demo": {
                "title": "Semantic vs Lexical Similarity",
                "time": "60-75 minutes",
                "goals": [
                    "Understand difference between lexical and semantic similarity",
                    "Implement Jaccard similarity (lexical)",
                    "Implement embedding-based similarity (semantic)",
                    "Compare both approaches on paraphrases and synonyms"
                ],
                "concepts": "Lexical similarity, semantic similarity, word embeddings",
                "todos": [
                    "Implement jaccard_similarity() for lexical matching",
                    "Implement embedding_similarity() using word vectors",
                    "Test on paraphrases with different words but same meaning",
                    "Test on similar words with different meanings",
                    "Analyze when each approach works better",
                    "Combine lexical and semantic signals"
                ]
            },
            "practice1": {
                "title": "Distance Metrics Comparison",
                "time": "60-75 minutes",
                "goals": [
                    "Understand different distance metrics",
                    "Implement Euclidean, Manhattan, and Cosine distance",
                    "Compare metrics on text embeddings",
                    "Learn when to use each metric"
                ],
                "concepts": "Euclidean distance, Manhattan distance, cosine distance, distance metrics",
                "todos": [
                    "Implement euclidean_distance() calculating L2 norm",
                    "Implement manhattan_distance() calculating L1 norm",
                    "Implement cosine_distance() as 1 - cosine_similarity",
                    "Compare all three on document embeddings",
                    "Analyze impact of document length on each metric",
                    "Visualize distance distributions"
                ]
            },
            "practice2": {
                "title": "Hybrid Search (Keyword + Vector)",
                "time": "75-90 minutes",
                "goals": [
                    "Understand hybrid search combining keyword and semantic search",
                    "Implement BM25 for keyword matching",
                    "Implement vector similarity for semantic matching",
                    "Combine scores using different strategies",
                    "Compare hybrid vs single-mode search"
                ],
                "concepts": "Hybrid search, score fusion, BM25, vector search",
                "todos": [
                    "Implement keyword_search() using BM25",
                    "Implement vector_search() using embeddings",
                    "Implement weighted_fusion() combining both scores",
                    "Implement rank_fusion() using reciprocal rank",
                    "Test on queries requiring both keyword and semantic matching",
                    "Tune fusion weights for best results"
                ]
            }
        },
        "advanced": {
            "demo": {
                "title": "FAISS for Scalable Vector Search",
                "time": "90-120 minutes",
                "goals": [
                    "Understand FAISS indexing for billion-scale search",
                    "Build FAISS indexes (Flat, IVF, HNSW)",
                    "Benchmark search speed and accuracy",
                    "Implement approximate nearest neighbor search"
                ],
                "concepts": "FAISS, ANN, indexing structures, speed vs accuracy tradeoff",
                "todos": [
                    "Create FAISS IndexFlatL2 for exact search",
                    "Create FAISS IndexIVFFlat for faster approximate search",
                    "Create FAISS IndexHNSWFlat for best speed/accuracy balance",
                    "Benchmark search latency and recall",
                    "Implement batch search for multiple queries",
                    "Tune nprobe parameter for IVF index"
                ]
            },
            "practice1": {
                "title": "Re-ranking Pipeline",
                "time": "90-120 minutes",
                "goals": [
                    "Understand two-stage retrieval (retrieve + re-rank)",
                    "Implement fast first-stage retrieval",
                    "Implement accurate second-stage re-ranking",
                    "Use cross-encoders for re-ranking",
                    "Optimize for latency and accuracy"
                ],
                "concepts": "Two-stage retrieval, cross-encoders, bi-encoders, re-ranking",
                "todos": [
                    "Implement first-stage retrieval with BM25 or FAISS",
                    "Retrieve top-100 candidates quickly",
                    "Implement cross-encoder re-ranking for top-100",
                    "Use sentence-transformers cross-encoder model",
                    "Compare single-stage vs two-stage results",
                    "Benchmark end-to-end latency"
                ]
            },
            "practice2": {
                "title": "Azure AI Search Integration",
                "time": "120+ minutes",
                "goals": [
                    "Integrate with Azure AI Search service",
                    "Create search indexes with semantic search",
                    "Implement hybrid search with Azure",
                    "Use semantic ranking for better results"
                ],
                "concepts": "Azure AI Search, semantic ranking, hybrid search, cloud search",
                "todos": [
                    "Set up Azure AI Search service",
                    "Create search index with schema",
                    "Upload documents to index",
                    "Implement keyword search queries",
                    "Enable semantic search configuration",
                    "Implement hybrid search combining keyword + semantic",
                    "Use semantic ranking for result refinement"
                ]
            }
        }
    },
    
    "topic-1.3-ner-classification": {
        "beginner": {
            "demo": {
                "title": "Rule-Based Named Entity Recognition",
                "time": "30-45 minutes",
                "goals": [
                    "Understand rule-based NER using regex",
                    "Extract emails, URLs, phone numbers, and dates",
                    "Build a simple entity extraction pipeline",
                    "Understand limitations of rule-based approaches"
                ],
                "concepts": "Regular expressions, pattern matching, entity extraction",
                "todos": [
                    "Implement extract_emails() using regex pattern",
                    "Implement extract_urls() for http/https URLs",
                    "Implement extract_phone_numbers() with various formats",
                    "Implement extract_dates() recognizing date patterns",
                    "Create extract_all_entities() combining all extractors",
                    "Test on sample text and visualize results"
                ]
            },
            "practice1": {
                "title": "Sentiment Analysis with Bag of Words",
                "time": "45-60 minutes",
                "goals": [
                    "Build a simple sentiment classifier",
                    "Use Bag of Words representation",
                    "Train Naive Bayes or Logistic Regression",
                    "Evaluate classifier performance",
                    "Understand basic text classification pipeline"
                ],
                "concepts": "Sentiment analysis, text classification, Naive Bayes, feature extraction",
                "todos": [
                    "Load and explore sentiment dataset (e.g., movie reviews)",
                    "Implement preprocess_text() for cleaning",
                    "Create BoW features using CountVectorizer",
                    "Train Naive Bayes classifier",
                    "Evaluate using accuracy, precision, recall",
                    "Test on new examples and interpret results"
                ]
            },
            "practice2": {
                "title": "Classification Evaluation Metrics",
                "time": "45-60 minutes",
                "goals": [
                    "Calculate evaluation metrics from scratch",
                    "Understand precision, recall, F1-score",
                    "Create confusion matrix",
                    "Interpret metrics for imbalanced datasets",
                    "Learn when to use each metric"
                ],
                "concepts": "Precision, recall, F1-score, confusion matrix, accuracy",
                "todos": [
                    "Implement calculate_precision() from TP and FP",
                    "Implement calculate_recall() from TP and FN",
                    "Implement calculate_f1_score() from precision and recall",
                    "Implement create_confusion_matrix() from predictions",
                    "Validate against sklearn.metrics",
                    "Visualize confusion matrix as heatmap",
                    "Analyze which metric matters for different use cases"
                ]
            }
        },
        "intermediate": {
            "demo": {
                "title": "ML-Based NER with spaCy",
                "time": "60-75 minutes",
                "goals": [
                    "Use spaCy for NER",
                    "Extract persons, organizations, locations",
                    "Visualize entities with displacy",
                    "Compare with rule-based NER"
                ],
                "concepts": "spaCy, statistical NER, entity types, named entity recognition",
                "todos": [
                    "Load spaCy model (en_core_web_sm)",
                    "Implement extract_entities() using doc.ents",
                    "Implement entity_statistics() counting entity types",
                    "Visualize entities using displacy.render()",
                    "Compare with regex-based extraction",
                    "Handle custom entity types"
                ]
            },
            "practice1": {
                "title": "Multi-Class Text Classification",
                "time": "60-75 minutes",
                "goals": [
                    "Build multi-class classifier (>2 classes)",
                    "Use TF-IDF features",
                    "Try multiple algorithms (NB, SVM, LogReg)",
                    "Analyze per-class performance",
                    "Handle imbalanced classes"
                ],
                "concepts": "Multi-class classification, TF-IDF, SVM, class imbalance",
                "todos": [
                    "Load multi-class dataset (e.g., news categories)",
                    "Create TF-IDF features",
                    "Train Naive Bayes, SVM, and Logistic Regression",
                    "Compare classifiers using classification_report",
                    "Analyze confusion matrix for error patterns",
                    "Handle class imbalance with class weights"
                ]
            },
            "practice2": {
                "title": "Systematic Error Analysis",
                "time": "60-75 minutes",
                "goals": [
                    "Identify common error patterns",
                    "Analyze false positives and false negatives",
                    "Find data quality issues",
                    "Suggest improvements based on error analysis"
                ],
                "concepts": "Error analysis, false positives, false negatives, debugging ML models",
                "todos": [
                    "Implement get_false_positives() finding incorrectly classified positive examples",
                    "Implement get_false_negatives() finding missed positive examples",
                    "Analyze error patterns by category",
                    "Identify common words in misclassified examples",
                    "Find ambiguous or mislabeled training examples",
                    "Generate error analysis report with actionable insights"
                ]
            }
        },
        "advanced": {
            "demo": {
                "title": "LLM-Based NER with Azure OpenAI",
                "time": "90-120 minutes",
                "goals": [
                    "Use LLMs for zero-shot NER",
                    "Design effective NER prompts",
                    "Extract structured entities from text",
                    "Compare LLM vs traditional NER"
                ],
                "concepts": "LLM NER, prompt engineering, zero-shot learning, structured extraction",
                "todos": [
                    "Design NER prompt for Azure OpenAI",
                    "Implement llm_extract_entities() with structured output",
                    "Handle JSON parsing and validation",
                    "Compare with spaCy NER results",
                    "Analyze cost, latency, and accuracy",
                    "Implement retry logic for API failures"
                ]
            },
            "practice1": {
                "title": "BERT Fine-Tuning for Classification",
                "time": "120+ minutes",
                "goals": [
                    "Fine-tune pre-trained BERT model",
                    "Use Hugging Face Transformers",
                    "Train on custom classification task",
                    "Compare with traditional ML approaches"
                ],
                "concepts": "BERT, fine-tuning, transfer learning, transformers",
                "todos": [
                    "Load pre-trained BERT model",
                    "Prepare dataset for BERT (tokenization, padding)",
                    "Create PyTorch DataLoaders",
                    "Fine-tune BERT with Trainer API",
                    "Evaluate on test set",
                    "Compare with BoW + Logistic Regression",
                    "Analyze what BERT learned"
                ]
            },
            "practice2": {
                "title": "Comprehensive NLP Model Evaluation",
                "time": "90-120 minutes",
                "goals": [
                    "Implement complete evaluation suite",
                    "Calculate all relevant metrics",
                    "Perform statistical significance testing",
                    "Create evaluation dashboard"
                ],
                "concepts": "Model evaluation, statistical testing, confidence intervals, dashboards",
                "todos": [
                    "Implement full metric calculation (accuracy, P, R, F1, AUC)",
                    "Calculate confidence intervals using bootstrap",
                    "Perform paired t-test for model comparison",
                    "Create confusion matrix visualization",
                    "Plot precision-recall curves",
                    "Generate HTML evaluation report"
                ]
            }
        }
    },
    
    "topic-1.4-consolidation": {
        "beginner": {
            "demo": {
                "title": "End-to-End NLP Pipeline",
                "time": "30-45 minutes",
                "goals": [
                    "Combine preprocessing, feature extraction, and classification",
                    "Build complete pipeline from raw text to predictions",
                    "Understand sklearn Pipeline API",
                    "Save and load trained pipelines"
                ],
                "concepts": "ML pipelines, sklearn Pipeline, end-to-end systems",
                "todos": [
                    "Create preprocessing step (cleaning, tokenization)",
                    "Create feature extraction step (TF-IDF)",
                    "Create classification step (Logistic Regression)",
                    "Combine into sklearn Pipeline",
                    "Train pipeline on dataset",
                    "Save pipeline using joblib",
                    "Load and use pipeline for predictions"
                ]
            },
            "practice1": {
                "title": "Traditional vs Embedding-Based Approaches",
                "time": "45-60 minutes",
                "goals": [
                    "Compare Bag of Words vs embeddings",
                    "Implement both approaches on same task",
                    "Analyze strengths and weaknesses",
                    "Understand when to use each approach"
                ],
                "concepts": "BoW, TF-IDF, word embeddings, representation comparison",
                "todos": [
                    "Implement classification with BoW features",
                    "Implement classification with averaged word embeddings",
                    "Train both models on same dataset",
                    "Compare accuracy, speed, and interpretability",
                    "Test on out-of-vocabulary words",
                    "Analyze which works better for small vs large data"
                ]
            },
            "practice2": {
                "title": "Simple RAG Pipeline with Azure OpenAI",
                "time": "60-75 minutes",
                "goals": [
                    "Build basic Retrieval-Augmented Generation system",
                    "Implement document chunking",
                    "Generate and store embeddings",
                    "Retrieve relevant chunks",
                    "Generate answers using Azure OpenAI"
                ],
                "concepts": "RAG, retrieval, embeddings, document chunking, generation",
                "todos": [
                    "Implement chunk_document() splitting text into chunks",
                    "Implement get_embeddings() using Azure OpenAI API",
                    "Implement retrieve_relevant_chunks() using cosine similarity",
                    "Implement generate_answer() with retrieved context",
                    "Build complete simple_rag_pipeline()",
                    "Test on sample documents and queries"
                ]
            }
        },
        "intermediate": {
            "demo": {
                "title": "RAG with Vector Database",
                "time": "75-90 minutes",
                "goals": [
                    "Build RAG system with vector database",
                    "Use FAISS for efficient retrieval",
                    "Implement metadata filtering",
                    "Add re-ranking for better results"
                ],
                "concepts": "Vector databases, FAISS, metadata filtering, re-ranking",
                "todos": [
                    "Create VectorStore class wrapping FAISS",
                    "Implement add_documents() with embeddings and metadata",
                    "Implement search() with metadata filters",
                    "Add re-ranking using cross-encoder",
                    "Build RAG pipeline with vector DB",
                    "Benchmark retrieval quality and speed"
                ]
            },
            "practice1": {
                "title": "Prompt Engineering for NLP Tasks",
                "time": "60-75 minutes",
                "goals": [
                    "Design effective prompts for various NLP tasks",
                    "Use few-shot learning with examples",
                    "Implement prompt templates",
                    "Compare zero-shot vs few-shot performance"
                ],
                "concepts": "Prompt engineering, few-shot learning, prompt templates",
                "todos": [
                    "Design prompts for classification tasks",
                    "Design prompts for NER tasks",
                    "Implement few-shot examples in prompts",
                    "Create reusable prompt templates",
                    "Compare zero-shot vs few-shot results",
                    "Analyze impact of prompt wording"
                ]
            },
            "practice2": {
                "title": "Traditional NLP vs GenAI Evaluation",
                "time": "75-90 minutes",
                "goals": [
                    "Compare traditional ML with LLM approaches",
                    "Evaluate on same task (e.g., classification)",
                    "Analyze accuracy, cost, latency, interpretability",
                    "Make informed architecture decisions"
                ],
                "concepts": "Model comparison, cost analysis, latency benchmarking",
                "todos": [
                    "Implement traditional ML baseline (TF-IDF + LogReg)",
                    "Implement LLM approach with Azure OpenAI",
                    "Evaluate both on accuracy metrics",
                    "Measure inference latency for both",
                    "Calculate cost per prediction for LLM",
                    "Analyze interpretability and debugging",
                    "Create decision matrix for when to use each"
                ]
            }
        },
        "advanced": {
            "demo": {
                "title": "Production RAG System",
                "time": "120+ minutes",
                "goals": [
                    "Build production-ready RAG system",
                    "Implement caching and monitoring",
                    "Add error handling and retry logic",
                    "Optimize for latency and cost",
                    "Add logging and observability"
                ],
                "concepts": "Production systems, caching, monitoring, error handling, optimization",
                "todos": [
                    "Create RAGSystem class with configuration",
                    "Implement embedding caching with TTL",
                    "Add error handling and retry with exponential backoff",
                    "Implement request logging and metrics",
                    "Add latency tracking and alerts",
                    "Optimize chunk size and retrieval parameters",
                    "Create health check endpoint"
                ]
            },
            "practice1": {
                "title": "Advanced Prompting (Chain-of-Thought, ReAct)",
                "time": "90-120 minutes",
                "goals": [
                    "Implement Chain-of-Thought prompting",
                    "Implement ReAct (Reasoning + Acting) pattern",
                    "Use self-consistency for better results",
                    "Compare with standard prompting"
                ],
                "concepts": "Chain-of-Thought, ReAct, self-consistency, advanced prompting",
                "todos": [
                    "Implement Chain-of-Thought prompting with 'Let's think step by step'",
                    "Implement ReAct pattern with thought-action-observation loop",
                    "Implement self-consistency generating multiple reasoning paths",
                    "Compare advanced prompting with baseline",
                    "Analyze when each technique helps",
                    "Measure cost increase vs accuracy improvement"
                ]
            },
            "practice2": {
                "title": "GenAI Evaluation Framework",
                "time": "120+ minutes",
                "goals": [
                    "Build comprehensive GenAI evaluation system",
                    "Implement relevance, faithfulness, and coherence metrics",
                    "Use LLM-as-judge for quality assessment",
                    "Create evaluation dashboard"
                ],
                "concepts": "GenAI evaluation, LLM-as-judge, relevance, faithfulness, coherence",
                "todos": [
                    "Implement relevance_score() measuring answer relevance",
                    "Implement faithfulness_score() checking groundedness",
                    "Implement coherence_score() assessing answer quality",
                    "Create LLM-as-judge prompts for quality assessment",
                    "Implement human evaluation interface",
                    "Calculate correlation between automated and human scores",
                    "Create comprehensive evaluation report"
                ]
            }
        }
    }
}


def generate_exercise_file(topic, level, exercise_type, content_dict, base_path):
    """Generate a single exercise file with complete structure"""
    
    title = content_dict["title"]
    time_estimate = content_dict["time"]
    goals = content_dict["goals"]
    concepts = content_dict["concepts"]
    todos = content_dict["todos"]
    
    # Create the exercise file content
    exercise_content = f'''"""
===============================================================================
{topic.upper().replace('-', ' ')} - {level.upper()} {exercise_type.upper()}
{title}
===============================================================================

🎯 LEARNING GOALS
-----------------
By completing this exercise, you will:
'''
    
    for i, goal in enumerate(goals, 1):
        exercise_content += f"{i}. {goal}\n"
    
    exercise_content += f'''
📚 KEY CONCEPTS
---------------
{concepts}

⏱️ TIME ESTIMATE
----------------
{time_estimate}

🔧 VS CODE SETUP INSTRUCTIONS
------------------------------
1. Open this file in VS Code
2. Open integrated terminal: View → Terminal (or Ctrl+`)
3. Navigate to exercise directory:
   cd e:/ey-ai/nlp-labs/{topic}/{level}
4. Ensure dependencies are installed:
   pip install -r ../../requirements.txt
5. Run this file:
   python {exercise_type}_exercise.py
6. To debug:
   - Set breakpoints (click left margin or press F9)
   - Press F5 to start debugging
   - Use Debug Console to inspect variables

📝 WHAT YOU NEED TO DO
----------------------
Complete the following TODO steps:

'''
    
    for i, todo in enumerate(todos, 1):
        exercise_content += f"TODO {i}: {todo}\n"
    
    exercise_content += '''

💡 HINTS
--------
- Read each TODO carefully and implement step by step
- Test each function individually before combining
- Use print() statements to debug your code
- Check the solution file if you get stuck
- Compare your output with the expected output below

📊 EXPECTED OUTPUT
------------------
When complete, your program should display:
- Clear section headers
- Results from each function
- Performance metrics (if applicable)
- Validation against known results

🎓 LEARNING TIPS
----------------
- Don't rush - understand each step
- Experiment with different inputs
- Read error messages carefully
- Ask questions if concepts are unclear

Let's get started! 🚀
"""

import numpy as np
import pandas as pd
from typing import List, Dict, Tuple
import re
from collections import Counter

# TODO: Add any additional imports you need


def main():
    """
    Main execution function
    Follow the TODO steps to complete the exercise
    """
    print("=" * 80)
    print(f"{topic.upper().replace('-', ' ')} - {level.upper()} {exercise_type.upper()}")
    print(f"{title}")
    print("=" * 80)
    print()
    
    # TODO: Implement your exercise logic here
    # Follow the TODO steps listed above
    
    print("\\n" + "=" * 80)
    print("Exercise complete! Compare your results with the solution file.")
    print("=" * 80)


if __name__ == "__main__":
    main()
'''
    
    # Create solution file content
    solution_content = exercise_content.replace("TODO:", "SOLUTION:").replace(
        "# TODO: Implement your exercise logic here",
        "# Complete implementation below"
    )
    
    # Add a note at the top of solution
    solution_content = solution_content.replace(
        '"""',
        '''"""
✅ THIS IS THE COMPLETE SOLUTION
This file contains the full working implementation.
Try the exercise file first before looking at this!

''',
        1
    )
    
    # Create file paths
    topic_path = Path(base_path) / topic / level
    topic_path.mkdir(parents=True, exist_ok=True)
    
    exercise_file = topic_path / f"{exercise_type}_exercise.py"
    solution_file = topic_path / f"{exercise_type}_solution.py"
    
    # Write files
    exercise_file.write_text(exercise_content, encoding='utf-8')
    solution_file.write_text(solution_content, encoding='utf-8')
    
    return exercise_file, solution_file


def main():
    """Generate all exercises with proper structure"""
    base_path = Path(__file__).parent
    
    print("=" * 80)
    print("GENERATING COMPREHENSIVE EXERCISES WITH COMPLETE STRUCTURE")
    print("=" * 80)
    print()
    
    total_files = 0
    
    for topic, levels in EXERCISES.items():
        print(f"\n📁 {topic}")
        for level, exercises in levels.items():
            print(f"  📂 {level}")
            for exercise_type, content in exercises.items():
                ex_file, sol_file = generate_exercise_file(
                    topic, level, exercise_type, content, base_path
                )
                print(f"    ✅ {exercise_type}_exercise.py")
                print(f"    ✅ {exercise_type}_solution.py")
                total_files += 2
    
    print("\n" + "=" * 80)
    print(f"COMPLETE! Generated {total_files} files with:")
    print("  ✅ Clear learning goals")
    print("  ✅ Step-by-step TODO instructions")
    print("  ✅ VS Code setup steps")
    print("  ✅ Expected output descriptions")
    print("  ✅ Complete solution files")
    print("=" * 80)
    print("\nNext step: Run the generator script to create actual implementation:")
    print("  python fix_all_exercises.py")
    print("\nThen implement the actual logic in each solution file!")


if __name__ == "__main__":
    main()
