from dotenv import load_dotenv

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions
from livekit.plugins import (
    noise_cancellation,
    silero,
)
from livekit.plugins import openai
from prompts.prompts import AGENT_INSTRUCTION, SESSION_INSTRUCTION
from tools.get_weather import get_weather
from tools.search_web import search_web
from tools.send_email import send_email
load_dotenv()


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(
            instructions=AGENT_INSTRUCTION,
            llm=openai.LLM(
                model="gpt-5-nano",
                #temperature=0.8,
            ),
            tts=openai.TTS(
                model="gpt-4o-mini-tts",
                voice="onyx",
            ),
            stt=openai.STT(
                model="gpt-4o-mini-transcribe"
            ),
            vad=silero.VAD.load(),
            tools=[
                get_weather,
                search_web,
                send_email
            ],

        )
        


async def entrypoint(ctx: agents.JobContext):
    session = AgentSession(
        
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            video_enabled=False,
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions=SESSION_INSTRUCTION,
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))