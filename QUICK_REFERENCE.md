# Quick Reference Guide ⚡

> Bookmark this page for instant access during hackathons.

## 🔥 Must-Have Free Credits

| Service | Free Tier | Sign Up |
|---------|-----------|----------|
| **Vultr** | $250-300 for 30 days | [vultr.com/promo/try250](https://www.vultr.com/promo/try250) |
| **Serper** | 2,500+ search queries | [serper.dev](https://serper.dev/) |
| **Twilio** | 1 phone number + $15 | [twilio.com](https://www.twilio.com/en-us) |
| **GitHub Student** | Copilot + $100+ credits | [education.github.com/pack](https://education.github.com/pack) |

## 📝 Copy-Paste Starters

### FastAPI + React Minimal
```bash
# Backend
pip install fastapi uvicorn
uvicorn main:app --reload

# Frontend
npx create-react-app frontend
cd frontend && npm start
```

### Next.js T3 Stack
```bash
npm create t3-app@latest
cd my-app
npm run dev
```

### Voice Agent (LiveKit + OpenAI)
```bash
pip install livekit livekit-plugins-openai
python agent.py start
```

## 🧑‍💻 Environment Variables Template

```bash
# .env
# Database
DATABASE_URL=postgresql://user:pass@host:5432/db

# AI APIs
OPENAI_API_KEY=sk-...
HUGGINGFACE_TOKEN=hf_...

# Search & Data
SERPER_API_KEY=...
FIRECRAWL_API_KEY=fc-...

# Communications
TWILIO_ACCOUNT_SID=AC...
TWILIO_AUTH_TOKEN=...
TWILIO_PHONE_NUMBER=+1...

# LiveKit
LIVEKIT_API_KEY=...
LIVEKIT_API_SECRET=...
LIVEKIT_URL=wss://...

# Deployment
VERCEL_TOKEN=...
```

## 🚨 Last-Minute Fixes

### Deployment Fails
```bash
# Use Ngrok to expose localhost
ngrok http 3000
# Give judges the ngrok URL
```

### CORS Issues
```python
# FastAPI
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

```javascript
// Express
const cors = require('cors');
app.use(cors());
```

### Database Connection Issues
```python
# Quick SQLite fallback
import sqlite3
conn = sqlite3.connect('hackathon.db')
```

## 🏆 Judging Day Checklist

- [ ] Record backup demo video (Loom)
- [ ] Test on mobile devices
- [ ] Prepare 3-minute pitch
- [ ] Have localhost running (+ Ngrok ready)
- [ ] Print architecture diagram
- [ ] List all APIs used (show free tiers)
- [ ] Prepare GitHub repo link
- [ ] Battery charged, charger ready

## 👨‍🏫 Pitch Structure (3 minutes)

**0:00-0:30** - Hook + Problem
- Shocking statistic OR personal story
- Why current solutions fail

**0:30-2:00** - Live Demo (60% of time)
- Show the core feature working
- Handle edge cases gracefully

**2:00-2:30** - Tech Stack + Innovation
- Highlight free/open-source tools used
- Mention any novel approaches

**2:30-3:00** - Business Model + Q&A
- How it scales
- Revenue potential
- Take questions

## 🔧 Debug Commands

```bash
# Check port usage
lsof -i :3000
kill -9 <PID>

# Reset node_modules
rm -rf node_modules package-lock.json
npm install

# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +

# Git reset (CAREFUL!)
git reset --hard HEAD
git clean -fd

# Docker cleanup
docker system prune -a
```

## 📊 Resource Limits

| Service | Rate Limit | Action if Hit |
|---------|------------|---------------|
| OpenAI Free | 3 RPM | Use Hugging Face |
| Serper | Depends on tier | Cache results |
| Vercel | 100 GB bandwidth | Use Netlify |
| Render Free | Sleeps after 15m | Keep-alive ping |

## 📞 Emergency Contacts

Save these in your phone:
- Teammate 1: [Phone]
- Teammate 2: [Phone]
- Faculty Mentor: [Phone]
- Venue WiFi Password: [Password]

---

**Print this page or save offline before hackathon starts!**
