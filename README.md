# NLP Fundamentals - Hands-On Lab Exercises

This repository contains comprehensive hands-on exercises for NLP fundamentals, designed for use with VS Code and Azure OpenAI.

## 📁 Lab Structure

Each topic folder contains:
- **README.md**: Concept overview and exercise descriptions
- **beginner/**: 1 demo + 2 practice exercises
- **intermediate/**: 1 demo + 2 practice exercises
- **advanced/**: 1 demo + 2 practice exercises

Each exercise includes:
- `*_exercise.py`: Starter code with TODO markers
- `*_solution.py`: Complete solution with explanations

## 📚 Topics

### [Topic 1.1: Text Preprocessing and Representations](./topic-1.1-text-preprocessing/)
Tokenization, stemming, lemmatization, BoW, TF-IDF, word embeddings

### [Topic 1.2: Semantic Similarity and Information Retrieval](./topic-1.2-semantic-similarity/)
Cosine similarity, vector space models, BM25, hybrid search

### [Topic 1.3: NER, Text Classification, and NLP Evaluation](./topic-1.3-ner-classification/)
Named entity recognition, sentiment analysis, evaluation metrics

### [Topic 1.4: Concept Consolidation and Bridge to GenAI](./topic-1.4-consolidation/)
End-to-end pipelines connecting NLP to modern GenAI systems

## 🚀 Setup Instructions

### 1. Install Required Packages

```bash
pip install -r requirements.txt
```

### 2. Configure Azure OpenAI

Create a `.env` file in the root directory:

```env
AZURE_OPENAI_ENDPOINT=your-endpoint-here
AZURE_OPENAI_API_KEY=your-api-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=your-deployment-name
AZURE_OPENAI_API_VERSION=2024-02-15-preview
```

### 3. Run Exercises

Navigate to any exercise file and run:

```bash
python beginner/demo_exercise.py
```

## 📖 Learning Path

1. Start with **beginner demos** to understand core concepts
2. Complete **beginner practice** exercises independently
3. Progress through **intermediate** and **advanced** levels
4. Compare your solutions with provided solution files

## 💡 Tips

- Read the README in each topic folder before starting exercises
- Try solving exercises before looking at solutions
- Experiment with different parameters and datasets
- Use VS Code's Python debugger to step through code

## 📝 Exercise Difficulty Levels

- **Beginner**: Core concepts, guided implementation, small datasets
- **Intermediate**: Multiple techniques, real-world data, comparison tasks
- **Advanced**: Production-ready code, optimization, integration with Azure OpenAI

## 🆘 Support

- Check solution files for detailed explanations
- Review topic README files for concept refreshers
- Use Azure OpenAI documentation for API details
