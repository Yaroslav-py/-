import os
import httpx
from openai import AsyncOpenAI
from dotenv import load_dotenv


load_dotenv()
client = AsyncOpenAI(base_url="https://openrouter.ai/api/v1",
                     api_key=os.getenv('CHAT_API'),
                     http_client=httpx.AsyncClient(proxy=os.getenv('PROXY'),
                                                   transport=httpx.HTTPTransport(
                                                       local_address='0.0.0.0'))
                     )


async def gpt_text(req, model):
    completion = await client.chat.completions.create(
        messages=[{'role': 'user', 'content': req}],
        model=model
    )
    return completion.choices[0].message.content

#asyncio.run(gpt_text('Hello world на с++','google/gemini-2.0-flash-001'))