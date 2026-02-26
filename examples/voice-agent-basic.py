#!/usr/bin/env python
"""
Basic LiveKit Voice Agent Example
Personal experience: Used in voice-based interview automation
"""

import asyncio
import os
from livekit import rtc
from livekit.agents import JobContext, WorkerOptions, cli
from livekit.agents.voice import VoicePipeline
from livekit.plugins import openai, deepgram, elevenlabs

async def entrypoint(ctx: JobContext):
    """Main entry point for voice agent"""
    
    # Connect to the LiveKit room
    await ctx.connect()
    
    # Initialize the voice pipeline
    # This handles: Audio In -> STT -> LLM -> TTS -> Audio Out
    pipeline = VoicePipeline(
        stt=deepgram.STT(model="nova-2"),  # Speech-to-Text
        llm=openai.LLM(
            model="gpt-4-turbo",
            temperature=0.7,
            instructions="""You are a friendly voice assistant helping with
            a product demo at a hackathon. Be concise and helpful.
            Keep responses under 50 words."""
        ),
        tts=elevenlabs.TTS(
            voice="Rachel",
            model="eleven_turbo_v2"
        ),
    )
    
    # Start the pipeline
    pipeline.start(ctx.room)
    
    print(f"Agent started in room: {ctx.room.name}")
    
    # Keep agent alive
    await asyncio.sleep(3600)  # 1 hour max

if __name__ == "__main__":
    # Run with: python voice-agent-basic.py start
    cli.run_app(
        WorkerOptions(
            entrypoint_fnc=entrypoint,
            api_key=os.getenv("LIVEKIT_API_KEY"),
            api_secret=os.getenv("LIVEKIT_API_SECRET"),
            ws_url=os.getenv("LIVEKIT_URL"),
        )
    )
