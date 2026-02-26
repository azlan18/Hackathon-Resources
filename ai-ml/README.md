# AI & Machine Learning

## Model Platforms

### Hugging Face
- **URL**: https://huggingface.co/
- **Models**: 45,000+ from leading AI providers
- **Modalities**: Text, image, video, audio, 3D
- **Pricing**: Free community tier + GPU compute from $0.60/hour
- **Libraries**: Transformers, Diffusers, Tokenizers, TRL, PEFT

**Quick Start:**
```python
from transformers import pipeline

# Text classification
classifier = pipeline("sentiment-analysis")
result = classifier("I love this hackathon!")

# Image generation
from diffusers import StableDiffusionPipeline
pipe = StableDiffusionPipeline.from_pretrained("stabilityai/stable-diffusion-2-1")
image = pipe("A beautiful sunset over mountains").images[0]
```

## Vector Databases for RAG

### Pinecone (Cloud)
- **URL**: https://www.pinecone.io/
- **Type**: Fully managed serverless vector database
- **Pricing**: 
  - **Starter**: Free tier with single pod
  - **Standard**: $50/month minimum (usage-based)
  - **Enterprise**: $500/month minimum
- **Best For**: Production RAG systems, scaling to millions of vectors

**Key Features:**
- Automatic scaling with no infrastructure management
- Multi-region deployment for global apps
- Hybrid search with sparse-dense vectors
- SLAs and compliance certifications (SOC 2, GDPR)
- Sub-100ms query latency at scale

**Quick Start:**
```python
import pinecone
from pinecone import Pinecone, ServerlessSpec

# Initialize
pc = Pinecone(api_key="YOUR_API_KEY")

# Create index
index = pc.create_index(
    name="hackathon-rag",
    dimension=1536,  # OpenAI embedding size
    metric="cosine",
    spec=ServerlessSpec(cloud="aws", region="us-east-1")
)

# Upsert vectors
index.upsert(vectors=[
    ("doc1", [0.1, 0.2, ...], {"text": "Document content"}),
    ("doc2", [0.3, 0.4, ...], {"text": "Another document"})
])

# Query
results = index.query(
    vector=[0.1, 0.2, ...],
    top_k=5,
    include_metadata=True
)
```

**Why Use It:**
- Zero DevOps overhead - focus on your app, not infrastructure
- Handles scaling from thousands to billions of vectors automatically
- Reliable for production with managed backups and failover
- Perfect when you need SLAs and compliance for customer-facing apps

### ChromaDB (Local)
- **URL**: https://www.trychroma.com/
- **Type**: Open-source embedded vector database
- **Pricing**: Free (self-hosted)
- **Best For**: Local development, prototyping, small-scale RAG systems

**Key Features:**
- Runs in-process with your Python app (zero network latency)
- No separate server or cloud account needed
- SQLite-based persistence to local disk
- Built-in embedding functions (OpenAI, Sentence Transformers)
- Metadata filtering for hybrid search

**Quick Start:**
```python
import chromadb
from chromadb.utils import embedding_functions

# Initialize client (persistent storage)
client = chromadb.PersistentClient(path="./chroma_db")

# Create collection with embedding function
openai_ef = embedding_functions.OpenAIEmbeddingFunction(
    api_key="YOUR_OPENAI_KEY",
    model_name="text-embedding-ada-002"
)

collection = client.get_or_create_collection(
    name="hackathon_docs",
    embedding_function=openai_ef
)

# Add documents (embeddings generated automatically)
collection.add(
    documents=["Document 1 content", "Document 2 content"],
    ids=["doc1", "doc2"],
    metadatas=[{"source": "file1.pdf"}, {"source": "file2.pdf"}]
)

# Query
results = collection.query(
    query_texts=["What is the main topic?"],
    n_results=5,
    include=["documents", "metadatas", "distances"]
)
```

**Why Use It:**
- Zero setup - `pip install chromadb` and you're running
- Perfect for hackathons - no API keys, accounts, or billing
- Works offline (great for testing on airplanes!)
- In-process means no network latency during development
- Easy to iterate on embedding strategies and chunking approaches

### Pinecone vs ChromaDB: When to Use What

| Aspect | ChromaDB | Pinecone |
|--------|----------|----------|
| **Setup Time** | Seconds (`pip install`) | Minutes (account signup) |
| **Local Development** | Native, works offline | Requires internet |
| **Production Scale** | Manual scaling required | Automatic scaling |
| **Cost** | Free (self-hosted) | $50+/month |
| **Latency** | Zero (in-process) | Network round-trip |
| **Reliability** | DIY backups | Managed SLAs |
| **Best For** | Prototyping, small apps | Production, scaling |

**Recommendation:**
- **Start with ChromaDB** for hackathons and MVP development
- **Migrate to Pinecone** when you need production reliability and scale
- ChromaDB handles up to ~100K vectors comfortably on local machines
- Pinecone excels at millions+ vectors with high concurrency

## No-Code Platforms

### Langflow
- **URL**: https://www.langflow.org/
- **Features**:
  - Visual drag-and-drop for LLM workflows
  - Python-based, agnostic to models/APIs/databases
  - Multi-agent orchestration
  - Instant API deployment
  - Free cloud service

**Architecture:**
1. Build flow visually with components (LLMs, vector stores, tools)
2. Test in playground with step-by-step control
3. Deploy as API endpoint
4. Call from your application

**API Usage:**
```python
import requests

response = requests.post(
    "https://your-langflow-api.com/run",
    json={
        "input": "Your prompt here",
        "tweaks": {}  # Optional parameter overrides
    }
)

result = response.json()
print(result["output"])
```

## When to Use What
- **Hugging Face**: Need specific pre-trained models or fine-tuning
- **ChromaDB**: Local RAG development and small-scale production
- **Pinecone**: Production RAG at scale with reliability requirements
- **Langflow**: Building agent workflows without coding infrastructure
- **LangChain** (from faculty PDF): When you need full programmatic control
