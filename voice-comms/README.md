# Voice & Communications

## Real-Time Voice AI

### LiveKit
- **URL**: https://livekit.io/
- **GitHub**: https://github.com/livekit/agents
- **Features**:
  - Complete STT-LLM-TTS pipeline
  - WebRTC-based real-time streaming
  - Turn detection & interruption handling
  - Plugins for OpenAI, AssemblyAI, Deepgram, etc.
  - Python & JavaScript SDKs

**Architecture:**
```
┌─────────────┐         ┌──────────────┐
│   Browser   │◄───────►│  LiveKit     │
│   (User)    │  WebRTC │  Room        │
└─────────────┘         └──────┬───────┘
                               │
                        ┌──────▼───────┐
                        │  Python      │
                        │  Agent       │
                        │  (STT→LLM    │
                        │   →TTS)      │
                        └──────────────┘
```

**Basic Agent Example:**
```python
import asyncio
from livekit import rtc
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.voice import VoicePipeline
from livekit.plugins import openai, deepgram, elevenlabs

async def entrypoint(ctx: JobContext):
    await ctx.connect()
    
    pipeline = VoicePipeline(
        stt=deepgram.STT(),
        llm=openai.LLM(model="gpt-4"),
        tts=elevenlabs.TTS(voice="Rachel"),
    )
    
    pipeline.start(ctx.room)
    await asyncio.sleep(3600)  # Keep alive

if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))
```

## Calling & Messaging

### Twilio
- **URL**: https://www.twilio.com/en-us
- **Free Tier**: 1 phone number + $15 credits
- **Test Mode**: Available for dev without charges
- **Features**: Voice, SMS, WhatsApp, OTP verification

**Voice Call Example:**
```python
from twilio.rest import Client

client = Client(account_sid, auth_token)

call = client.calls.create(
    to="+1234567890",
    from_="+0987654321",
    url="http://your-webhook.com/voice",  # TwiML instructions
    method="POST"
)

print(f"Call SID: {call.sid}")
```

**Integrate with LiveKit:**
1. Twilio receives call
2. Webhook creates LiveKit room
3. Connects caller to LiveKit agent
4. Agent handles conversation via STT-LLM-TTS
5. Audio streams back to caller

## Use Cases
- Customer service voice bots
- Interview automation
- Voice-first ordering systems
- Real-time transcription services
- Interactive voice response (IVR)
