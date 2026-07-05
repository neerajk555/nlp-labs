# NLP Labs - Complete Exercise Catalog

## Overview
This catalog lists all 28 exercises across 4 topics (7 exercises per topic).
Each exercise includes starter code with TODOs and complete solutions.

---

## Topic 1.1: Text Preprocessing and Representations

### Beginner Level (3 exercises)
✅ **Demo**: Basic text preprocessing pipeline
- File: `topic-1.1-text-preprocessing/beginner/demo_exercise.py`
- Concepts: Lowercasing, punctuation removal, stopwords
- Dataset: Sample sentences

✅ **Practice 1**: Tokenization comparison  
- File: `topic-1.1-text-preprocessing/beginner/practice1_exercise.py`
- Concepts: Character, word, subword tokenization
- Dataset: Short texts

✅ **Practice 2**: Bag of Words implementation
- File: `topic-1.1-text-preprocessing/beginner/practice2_exercise.py`
- Concepts: BoW representation, vocabulary building
- Dataset: Small document collection

### Intermediate Level (3 exercises)
✅ **Demo**: TF-IDF from scratch vs sklearn
- File: `topic-1.1-text-preprocessing/intermediate/demo_exercise.py`
- Concepts: TF-IDF calculation, keyword extraction
- Dataset: Document corpus

✅ **Practice 1**: Stemming vs lemmatization analysis
- File: `topic-1.1-text-preprocessing/intermediate/practice1_exercise.py`
- Concepts: Porter Stemmer, WordNet Lemmatizer, trade-offs
- Dataset: Varied linguistic examples

✅ **Practice 2**: Word2Vec training and exploration
- File: `topic-1.1-text-preprocessing/intermediate/practice2_exercise.py`
- Concepts: CBOW vs Skip-gram, semantic similarity
- Dataset: Custom corpus

### Advanced Level (3 exercises)
🔨 **Demo**: Production preprocessing pipeline
- File: `topic-1.1-text-preprocessing/advanced/demo_exercise.py`
- Concepts: Error handling, logging, configurable pipeline
- Dataset: Real-world messy text

🔨 **Practice 1**: Subword tokenization for LLMs
- File: `topic-1.1-text-preprocessing/advanced/practice1_exercise.py`
- Concepts: BPE, WordPiece, SentencePiece
- Dataset: Multi-language text

🔨 **Practice 2**: Embedding comparison (Word2Vec vs GloVe vs Azure OpenAI)
- File: `topic-1.1-text-preprocessing/advanced/practice2_exercise.py`
- Concepts: Pre-trained embeddings, Azure OpenAI API
- Dataset: Semantic similarity tasks

---

## Topic 1.2: Semantic Similarity and Information Retrieval

### Beginner Level (3 exercises)
📝 **Demo**: Cosine similarity calculation
- Concepts: Vector representations, similarity metrics
- Dataset: Simple text pairs

📝 **Practice 1**: Building an inverted index
- Concepts: Index construction, term lookup
- Dataset: Document collection

📝 **Practice 2**: BM25 keyword search
- Concepts: BM25 formula, ranking documents
- Dataset: Search queries + documents

### Intermediate Level (3 exercises)
📝 **Demo**: Semantic vs lexical similarity comparison
- Concepts: Embeddings for semantic search
- Dataset: Paraphrase detection

📝 **Practice 1**: Distance metrics comparison (Euclidean, Manhattan, Cosine)
- Concepts: Vector space models, metric properties
- Dataset: High-dimensional vectors

📝 **Practice 2**: Hybrid search (keyword + vector)
- Concepts: Combining BM25 and embeddings
- Dataset: Q&A dataset

### Advanced Level (3 exercises)
📝 **Demo**: Production search system with FAISS
- Concepts: Approximate nearest neighbors, indexing
- Dataset: Large document corpus

📝 **Practice 1**: Re-ranking with cross-encoders
- Concepts: Bi-encoder + cross-encoder pipeline
- Dataset: MS MARCO or similar

📝 **Practice 2**: Hybrid search with Azure AI Search
- Concepts: Azure integration, vector + keyword search
- Dataset: Enterprise documents

---

## Topic 1.3: NER, Text Classification, and NLP Evaluation

### Beginner Level (3 exercises)
📝 **Demo**: Rule-based NER
- Concepts: Regex patterns, entity extraction
- Dataset: News articles

📝 **Practice 1**: Sentiment analysis with sklearn
- Concepts: Classification pipeline, feature extraction
- Dataset: Movie reviews

📝 **Practice 2**: Evaluation metrics calculation
- Concepts: Precision, recall, F1, confusion matrix
- Dataset: Classification results

### Intermediate Level (3 exercises)
📝 **Demo**: ML-based NER with spaCy
- Concepts: Pre-trained models, entity types
- Dataset: Multi-domain text

📝 **Practice 1**: Multi-class text classification
- Concepts: Feature engineering, model comparison
- Dataset: News categories

📝 **Practice 2**: Error analysis workshop
- Concepts: Confusion matrix, failure modes
- Dataset: Misclassified examples

### Advanced Level (3 exercises)
📝 **Demo**: LLM-based NER with prompt engineering
- Concepts: Few-shot learning, Azure OpenAI
- Dataset: Custom entity types

📝 **Practice 1**: Fine-tuning BERT for classification
- Concepts: Transfer learning, Hugging Face
- Dataset: Domain-specific classification

📝 **Practice 2**: Comprehensive evaluation pipeline
- Concepts: Cross-validation, statistical testing
- Dataset: Multiple datasets

---

## Topic 1.4: Concept Consolidation and Bridge to GenAI

### Beginner Level (3 exercises)
📝 **Demo**: End-to-end NLP pipeline
- Concepts: Preprocessing → Features → Model → Evaluation
- Dataset: Simple classification task

📝 **Practice 1**: From BoW to embeddings comparison
- Concepts: Feature evolution, performance impact
- Dataset: Same task, different representations

📝 **Practice 2**: Building a simple RAG pipeline
- Concepts: Retrieval + generation basics
- Dataset: FAQ documents

### Intermediate Level (3 exercises)
📝 **Demo**: RAG with vector database
- Concepts: Chunking, embedding, retrieval
- Dataset: Technical documentation

📝 **Practice 1**: Prompt engineering for NLP tasks
- Concepts: Zero-shot, few-shot classification
- Dataset: Various NLP tasks

📝 **Practice 2**: Evaluation: Traditional NLP vs GenAI
- Concepts: Comparing F1, BLEU, ROUGE, LLM-as-judge
- Dataset: Multiple task outputs

### Advanced Level (3 exercises)
📝 **Demo**: Production RAG system
- Concepts: Azure AI Search, OpenAI embeddings
- Dataset: Enterprise knowledge base

📝 **Practice 1**: Advanced prompt engineering
- Concepts: Chain-of-thought, ReAct, tool use
- Dataset: Complex reasoning tasks

📝 **Practice 2**: GenAI evaluation framework
- Concepts: Relevance, faithfulness, answer quality
- Dataset: RAG system outputs

---

## Progress Summary

| Topic | Beginner | Intermediate | Advanced | Total |
|-------|----------|--------------|----------|-------|
| 1.1 Text Preprocessing | ✅ 3/3 | ✅ 3/3 | 🔨 1/3 | 7/7 |
| 1.2 Semantic Similarity | 📝 0/3 | 📝 0/3 | 📝 0/3 | 0/7 |
| 1.3 NER & Classification | 📝 0/3 | 📝 0/3 | 📝 0/3 | 0/7 |
| 1.4 Consolidation | 📝 0/3 | 📝 0/3 | 📝 0/3 | 0/7 |

Legend: ✅ Complete | 🔨 In Progress | 📝 Planned

---

## File Structure

```
nlp-labs/
├── README.md
├── requirements.txt
├── .env.example
├── EXERCISE_CATALOG.md (this file)
│
├── topic-1.1-text-preprocessing/
│   ├── README.md
│   ├── beginner/
│   │   ├── demo_exercise.py
│   │   ├── demo_solution.py
│   │   ├── practice1_exercise.py
│   │   ├── practice1_solution.py
│   │   ├── practice2_exercise.py
│   │   └── practice2_solution.py
│   ├── intermediate/
│   │   └── (same structure)
│   └── advanced/
│       └── (same structure)
│
├── topic-1.2-semantic-similarity/
│   └── (same structure)
│
├── topic-1.3-ner-classification/
│   └── (same structure)
│
└── topic-1.4-consolidation/
    └── (same structure)
```

---

## Next Steps

To complete the remaining exercises:

1. **Topic 1.1 Advanced** (2 exercises remaining)
2. **Topic 1.2** (all 7 exercises)
3. **Topic 1.3** (all 7 exercises)  
4. **Topic 1.4** (all 7 exercises)

Would you like me to:
- Continue generating all remaining exercises?
- Focus on a specific topic?
- Generate templates for rapid completion?
