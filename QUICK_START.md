# Quick Start Guide for NLP Labs

## 🚀 Getting Started in 5 Minutes

### Step 1: Clone and Setup

```bash
cd e:/ey-ai/nlp-labs
pip install -r requirements.txt
```

### Step 2: Configure Azure OpenAI

Create `.env` file from template:
```bash
copy .env.example .env
```

Edit `.env` with your credentials:
```env
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_API_KEY=your-key-here
AZURE_OPENAI_DEPLOYMENT_NAME=gpt-4
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-ada-002
```

### Step 3: Download NLTK Data (First Time Only)

```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
```

### Step 4: Run Your First Exercise

```bash
cd topic-1.1-text-preprocessing/beginner
python demo_exercise.py
```

---

## 📚 Learning Path

### For Complete Beginners
1. Start with Topic 1.1 Beginner exercises
2. Read the README in each topic folder
3. Complete exercises in order (demo → practice1 → practice2)
4. Compare your solutions with provided solution files

### For Intermediate Learners
1. Start with Topic 1.1 Intermediate or skim Beginner
2. Focus on implementation details and trade-offs
3. Experiment with different parameters
4. Try modifying exercises with your own data

### For Advanced Practitioners
1. Jump to Advanced exercises in any topic
2. Focus on production-ready implementations
3. Integrate with Azure services
4. Benchmark performance and optimize

---

## 🏗️ Lab Structure

```
nlp-labs/
├── README.md                    # Main overview
├── EXERCISE_CATALOG.md          # All 28 exercises listed
├── QUICK_START.md              # This file
├── requirements.txt             # Python dependencies
├── .env.example                 # Configuration template
├── generate_exercises.py        # Auto-generate remaining exercises
│
├── topic-1.1-text-preprocessing/
│   ├── README.md                # Topic overview and concepts
│   ├── beginner/
│   │   ├── demo_exercise.py           # Demo with TODOs
│   │   ├── demo_solution.py           # Complete solution
│   │   ├── practice1_exercise.py      # Practice with TODOs
│   │   ├── practice1_solution.py      # Complete solution
│   │   ├── practice2_exercise.py
│   │   └── practice2_solution.py
│   ├── intermediate/
│   │   └── (same structure - 6 files)
│   └── advanced/
│       └── (same structure - 6 files)
│
├── topic-1.2-semantic-similarity/
│   └── (same structure as 1.1)
│
├── topic-1.3-ner-classification/
│   └── (same structure as 1.1)
│
└── topic-1.4-consolidation/
    └── (same structure as 1.1)
```

**Total:** 4 topics × 3 levels × 3 exercises × 2 files = **72 files**

---

## 💻 Running Exercises

### Individual Exercise
```bash
python topic-1.1-text-preprocessing/beginner/demo_exercise.py
```

### View Solution
```bash
python topic-1.1-text-preprocessing/beginner/demo_solution.py
```

### Run All Beginner Exercises in a Topic
```bash
cd topic-1.1-text-preprocessing/beginner
python demo_solution.py
python practice1_solution.py
python practice2_solution.py
```

---

## 🎯 Exercise Format

Each exercise file has:

### Exercise File (`*_exercise.py`)
- **Header comment**: Learning goals and concepts
- **TODO markers**: Where you need to code
- **Skeleton code**: Structure and hints
- **Main function**: Test harness

### Solution File (`*_solution.py`)
- **Complete implementation**: Fully working code
- **Detailed comments**: Explaining each step
- **Insights**: Key takeaways and best practices
- **Extensions**: Ideas for further learning

---

## 📖 Suggested Timeline

### One Week Intensive
- **Day 1-2**: Topic 1.1 (All levels)
- **Day 3-4**: Topic 1.2 (All levels)
- **Day 5**: Topic 1.3 (Beginner + Intermediate)
- **Day 6**: Topic 1.3 (Advanced) + Topic 1.4 (Beginner)
- **Day 7**: Topic 1.4 (Intermediate + Advanced)

### Two Week Relaxed
- **Week 1**: Topics 1.1 and 1.2 (all levels)
- **Week 2**: Topics 1.3 and 1.4 (all levels)

### Self-Paced
- 1-2 exercises per day
- Complete in 2-4 weeks
- Focus on understanding over speed

---

## 🔧 Troubleshooting

### ImportError: No module named 'X'
```bash
pip install -r requirements.txt
```

### NLTK Data Not Found
```python
import nltk
nltk.download('all')  # Downloads all NLTK data
```

### Azure OpenAI Errors
- Check `.env` file exists and has correct values
- Verify Azure OpenAI deployment names match
- Ensure API key is valid and not expired

### Performance Issues
- For large corpora, consider using a subset for practice
- Use `%%time` in Jupyter notebooks to profile
- Check available RAM (some exercises use embeddings)

---

## 📊 Tracking Progress

### Create a Progress Tracker

```python
# progress_tracker.py
import json
from datetime import datetime

progress = {
    "topic-1.1": {"beginner": [], "intermediate": [], "advanced": []},
    "topic-1.2": {"beginner": [], "intermediate": [], "advanced": []},
    "topic-1.3": {"beginner": [], "intermediate": [], "advanced": []},
    "topic-1.4": {"beginner": [], "intermediate": [], "advanced": []},
}

def mark_complete(topic, level, exercise):
    progress[topic][level].append({
        "exercise": exercise,
        "completed": datetime.now().isoformat()
    })
    with open("my_progress.json", "w") as f:
        json.dump(progress, f, indent=2)
    print(f"✓ Marked {topic}/{level}/{exercise} as complete!")

# Usage
mark_complete("topic-1.1", "beginner", "demo")
```

---

## 🎓 Learning Tips

### Before Starting an Exercise
1. Read the topic README
2. Review the concepts mentioned
3. Look at the learning goals

### While Working on an Exercise
1. Try to implement before looking at hints
2. Run code frequently to test
3. Use print statements for debugging
4. Read error messages carefully

### After Completing an Exercise
1. Compare with solution
2. Understand differences in approach
3. Note any new techniques learned
4. Try the "Extensions" if provided

### If You Get Stuck
1. Re-read the concept explanation in README
2. Check the hints in TODO comments
3. Look at similar completed exercises
4. Review the solution (it's okay!)
5. Try to re-implement after understanding

---

## 🌟 Going Further

### After Completing All Exercises

1. **Build a Project**
   - Sentiment analysis on Twitter data
   - Document search engine
   - Named entity extraction tool
   - Question answering system

2. **Read Research Papers**
   - Word2Vec original paper (Mikolov et al.)
   - BERT paper (Devlin et al.)
   - RAG paper (Lewis et al.)

3. **Explore Advanced Topics**
   - Fine-tuning transformers
   - Building production RAG systems
   - Multi-lingual NLP
   - Zero-shot learning

4. **Contribute**
   - Add new exercises
   - Improve existing solutions
   - Create domain-specific variants
   - Share your projects

---

## 📞 Support & Resources

### Documentation
- **NLTK**: https://www.nltk.org/
- **spaCy**: https://spacy.io/
- **scikit-learn**: https://scikit-learn.org/
- **Gensim**: https://radimrehurek.com/gensim/
- **Azure OpenAI**: https://learn.microsoft.com/en-us/azure/ai-services/openai/

### Additional Learning
- **Textbooks**: "Speech and Language Processing" by Jurafsky & Martin
- **Courses**: Stanford CS224N, fast.ai NLP
- **Blogs**: Jay Alammar's blog, Lil'Log
- **Podcasts**: NLP Highlights, Gradient Dissent

---

## ✅ Completion Checklist

Track your progress:

### Topic 1.1: Text Preprocessing
- [ ] Beginner Demo
- [ ] Beginner Practice 1
- [ ] Beginner Practice 2
- [ ] Intermediate Demo
- [ ] Intermediate Practice 1
- [ ] Intermediate Practice 2
- [ ] Advanced Demo
- [ ] Advanced Practice 1
- [ ] Advanced Practice 2

### Topic 1.2: Semantic Similarity
- [ ] Beginner Demo
- [ ] Beginner Practice 1
- [ ] Beginner Practice 2
- [ ] Intermediate Demo
- [ ] Intermediate Practice 1
- [ ] Intermediate Practice 2
- [ ] Advanced Demo
- [ ] Advanced Practice 1
- [ ] Advanced Practice 2

### Topic 1.3: NER & Classification
- [ ] Beginner Demo
- [ ] Beginner Practice 1
- [ ] Beginner Practice 2
- [ ] Intermediate Demo
- [ ] Intermediate Practice 1
- [ ] Intermediate Practice 2
- [ ] Advanced Demo
- [ ] Advanced Practice 1
- [ ] Advanced Practice 2

### Topic 1.4: Consolidation
- [ ] Beginner Demo
- [ ] Beginner Practice 1
- [ ] Beginner Practice 2
- [ ] Intermediate Demo
- [ ] Intermediate Practice 1
- [ ] Intermediate Practice 2
- [ ] Advanced Demo
- [ ] Advanced Practice 1
- [ ] Advanced Practice 2

---

## 🎉 Congratulations!

When you complete all exercises, you'll have:
- ✅ Mastered core NLP preprocessing techniques
- ✅ Understood semantic similarity and retrieval
- ✅ Built NER and classification systems
- ✅ Connected traditional NLP to modern GenAI
- ✅ Ready to build production NLP/RAG systems!

**Next**: Build your own NLP project using these skills! 🚀
