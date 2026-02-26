# Hackathon Resources 🚀

> Battle-tested toolkit from real hackathon projects. Skip setup, focus on innovation.

[![GitHub Stars](https://img.shields.io/github/stars/azlan18/Hackathon-Resources)](https://github.com/azlan18/Hackathon-Resources/stargazers)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

A comprehensive collection of tools, APIs, platforms, and resources that have proven valuable in actual hackathons. These are personally tested recommendations from building voice agents, ML apps, and full-stack projects under tight deadlines.

## 📚 Table of Contents

- [Frontend Components](#-frontend-components)
- [Data & APIs](#-data--apis)
- [AI & Machine Learning](#-ai--machine-learning)
- [Voice & Communications](#-voice--communications)
- [Deployment & Infrastructure](#-deployment--infrastructure)
- [Contributing](#-contributing)

---

## 🎨 Frontend Components

Beautiful, animated, production-ready components to polish your UI quickly.

### [React Bits](https://www.reactbits.dev/)
**110+ animated React components**
- Text animations, particle backgrounds, interactive effects
- Minimal dependencies with extensive prop customization
- Available in 4 variants: JS+CSS, JS+Tailwind, TS+CSS, TS+Tailwind
- Full source code access for unlimited modifications
- MIT license - free for commercial use

**Why use it:** Perfect for portfolios and landing pages that need to make a visual impact without reinventing animation logic.

### [Aceternity UI](https://ui.aceternity.com/)
**200+ free copy-paste components**
- Built with Tailwind CSS and Framer Motion
- Animated modals, expandable cards, 3D effects
- Smooth transitions that significantly improve UX
- Highly customizable despite being ready-made

**Why use it:** When you need stunning, professional components that judges will remember. Saves hours of CSS animation work.

---

## 🔍 Data & APIs

Tools for crawling, searching, and creating datasets with real data patterns.

### [Firecrawl](https://www.firecrawl.dev/)
**Turn entire websites into LLM-ready data**
- **Scrape**: Get single pages in markdown, structured data, HTML, or screenshots
- **Crawl**: Recursively scrape entire websites with all subpages
- **Map**: Instantly get all URLs from a website (extremely fast)
- **Extract**: Use AI to get structured data from pages

```python
from firecrawl import Firecrawl
firecrawl = Firecrawl(api_key="fc-YOUR_API_KEY")

# Scrape a website
doc = firecrawl.scrape("https://example.com", formats=["markdown", "html"])
print(doc.markdown)
```

**Why use it:** Essential for RAG applications, creating training datasets, or when you need clean data from messy websites.

### [Serper.dev](https://serper.dev/)
**Lightning-fast Google Search API**
- Industry-leading SERP API with 1-2 second response times
- **2,500+ free credits** for new signups
- Pricing: $0.30-$1.00 per 1,000 queries (10x cheaper than alternatives)
- Returns structured JSON with organic results, images, videos, knowledge graphs

**Why use it:** Perfect for adding real-time search to your hackathon app. Generous free tier means you won't hit limits mid-demo.

### [Parallel.ai](https://parallel.ai/)
**Advanced web research and search APIs for AI agents**
- **Deep Research Mode**: Multi-hop accuracy of 48% vs GPT-4's 14%
- **Multiple Agent Modes**: Fast, hyper-fast, comprehensive research
- **Scraping & Page Extraction**: Get structured data from any page
- SOC 2 Type II certified for enterprise use
- Structured JSON outputs for easy integration

**Why use it:** When you need an AI that can actually research topics deeply. Beats major LLMs in multi-step reasoning tasks.

---

## 🤖 AI & Machine Learning

Tools to integrate AI capabilities without training models from scratch.

### [Hugging Face](https://huggingface.co/)
**The home of machine learning**
- **45,000+ models** from leading AI providers through unified API
- Text, image, video, audio, and 3D modalities
- **Inference API**: Run models without managing infrastructure
- Free community features + paid compute starting at $0.60/hour for GPU
- Extensive libraries: Transformers, Diffusers, Tokenizers, TRL, PEFT

**Why use it:** One-stop shop for any ML task. From text classification to image generation, there's a pre-trained model ready to use.

### [Langflow](https://www.langflow.org/)
**No-code AI agent and RAG app builder**
- **Visual drag-and-drop** interface for building LLM workflows
- Python-based and agnostic to any model, API, or database
- **Instant API deployment**: Turn your flow into an API endpoint
- Pre-built components for agents, RAG, vector stores, tools
- **Multi-agent orchestration** with conversation management
- Free cloud service to get started in minutes

```python
# Deploy your Langflow as API and call it
import requests
response = requests.post(
    "https://your-langflow-api.com/run",
    json={"input": "Your prompt here"}
)
```

**Why use it:** Build complex AI agents without writing boilerplate code. Perfect when you want to focus on logic, not infrastructure.

### Vector Databases

For detailed information on Pinecone (cloud) and ChromaDB (local) vector databases for RAG systems, see the [AI/ML directory](./ai-ml/README.md#vector-databases-for-rag).

---

## 🎙️ Voice & Communications

Build real-time voice agents and integrate calling functionality.

### [LiveKit](https://livekit.io/)
**Open-source real-time voice AI framework**
- **Complete STT-LLM-TTS pipeline** with turn detection and interruption handling
- **WebRTC-based** real-time audio/video streaming
- Plugins for major AI providers (OpenAI, AssemblyAI, etc.)
- **Room architecture**: Multiple participants can join same session
- Python and JavaScript SDKs
- Self-hosted or cloud deployment options

**Architecture:**
1. Browser/app joins LiveKit room
2. Python agent joins same room as participant
3. Audio streams bidirectionally via WebRTC
4. Agent handles STT → LLM → TTS in real-time
5. Structured events sync UI instantly

**Why use it:** Industry-standard for voice AI. Used in production by companies building voice-first applications. Handles all the hard parts of real-time audio.

### [Twilio](https://www.twilio.com/en-us)
**Calling, SMS, and OTP integration**
- **Free tier**: 1 free phone number + $15 credits for new accounts
- **Test credentials** available for development without charges
- Easy integration with LiveKit for voice agents
- APIs for voice calling, SMS, WhatsApp, OTP verification
- Extensive documentation and SDK support

```python
from twilio.rest import Client
client = Client(account_sid, auth_token)

# Make a call
call = client.calls.create(
    to="+1234567890",
    from_="+0987654321",
    url="http://your-voice-agent-webhook.com"
)
```

**Why use it:** Seamlessly add calling to your voice agents. Free credits are enough for entire hackathon. Well-documented and reliable.

---

## 🚀 Deployment & Infrastructure

Free hosting and VPS platforms to deploy your projects.

### [Vultr](https://www.vultr.com/promo/try250)
**$250-300 free cloud credits**
- **$300 free for 30 days** for new users
- High-performance SSD cloud servers with global data centers
- **1-click apps**: WordPress, Docker, Minecraft hosting
- DDoS protection & 100% SLA uptime
- Pay-as-you-go or monthly plans

**Use cases:**
- Testing cloud servers before committing
- Hosting ML models or backends during hackathon
- Running game servers or staging environments

**How to claim:**
1. Sign up with new email (existing accounts ineligible)
2. Use promo codes: `FLY300VULTR` or `250VULTRFLY`
3. Credits auto-apply or manually enter in Billing → Promo Code
4. Deploy servers immediately without upfront charges

**Why use it:** Generous credits let you run GPU instances or heavy workloads for entire hackathon without cost worries.

---

## 🤝 Contributing

Found a great tool that helped you win a hackathon? PRs welcome!

**What to include:**
- Tool name and official link
- What it does (1-2 sentences)
- Why it's valuable for hackathons
- Free tier details or pricing
- Personal experience if applicable

**Focus areas:**
- India-specific tools (e.g., Razorpay test mode)
- Emerging AI platforms
- Developer tools with generous free tiers
- Real-time/WebRTC technologies
- Data processing and ETL tools

---

## 📝 License

MIT License - feel free to use these resources in your projects.

## 🌟 Star History

If this repo helped you ship faster, give it a star! ⭐

---

**Built with ❤️ for the hackathon community**

*Resources compiled from personal experience building voice agents, ML apps, and full-stack projects.*
